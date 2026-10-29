import streamlit as st
import requests
import xml.etree.ElementTree as ET
def search_hira_diseases(search_text, api_key):
    """건강보험심사평가원 API에서 질병명칭과 코드를 검색합니다."""

    params = {
        "ServiceKey": api_key,
        "pageNo": "1",
        "numOfRows": "20",
        "SICK_NM": search_text,
    }

    response = requests.get(
        HIRA_DISEASE_API_URL,
        params=params,
        timeout=15,
    )

    response.raise_for_status()

    root = ET.fromstring(response.content)

    # API가 반환한 오류 확인
    result_code = get_xml_value(
        root,
        ["resultCode", "RESULTCODE"],
    )
    result_message = get_xml_value(
        root,
        ["resultMsg", "RESULTMSG"],
    )

    if result_code and result_code not in ["00", "0000"]:
        raise ValueError(
            f"API 응답 오류: {result_code} - {result_message}"
        )

    items = []

    for item in root.iter():
        tag_name = item.tag.split("}")[-1].lower()

        if tag_name != "item":
            continue

        disease_code = get_xml_value(
            item,
            ["sickCd", "SICK_CD"],
        )
        disease_name = get_xml_value(
            item,
            ["sickNm", "SICK_NM"],
        )
        english_name = get_xml_value(
            item,
            ["engNm", "ENG_NM", "engSickNm"],
        )

        if disease_name or disease_code:
            items.append({
                "질병명": disease_name or "정보 없음",
                "상병코드": disease_code or "정보 없음",
                "영문명": english_name or "정보 없음",
            })

    # 중복 결과 제거
    unique_items = []
    seen = set()

    for item in items:
        identity = (
            item["상병코드"],
            item["질병명"],
        )

        if identity not in seen:
            seen.add(identity)
            unique_items.append(item)

    return unique_items


# =========================================================
# 공공 질병 검색 화면
# =========================================================

st.divider()
st.header("🔎 공공 질병명·상병코드 검색")

st.write(
    "건강보험심사평가원 질병정보서비스를 이용해 "
    "질병명과 상병코드를 검색합니다."
)

st.caption(
    "검색 결과는 공공 API에서 제공하는 정보입니다. "
    "이 결과만으로 질환의 해부학적 위치나 치료·수술 과정을 "
    "확정하지 않습니다."
)

with st.form("hira_disease_search_form"):
    hira_search_text = st.text_input(
        "검색할 질병명",
        placeholder="예: 충수염, 장폐색, 탈장",
    )

    hira_search_button = st.form_submit_button(
        "공공 질병정보 검색",
        use_container_width=True,
    )

if hira_search_button:
    if not hira_search_text.strip():
        st.warning("검색할 질병명을 입력해 주세요.")

    else:
        hira_api_key = st.secrets["HIRA_API_KEY"]

        if not hira_api_key:
            st.error(
                "HIRA API 인증키를 찾을 수 없습니다. "
                "Streamlit Secrets에 HIRA_API_KEY를 등록해 주세요."
            )

        else:
            try:
                with st.spinner("공공 질병정보를 검색하고 있습니다..."):
                    hira_results = search_hira_diseases(
                        hira_search_text.strip(),
                        hira_api_key,
                    )

                if hira_results:
                    st.success(
                        f"{len(hira_results)}개의 결과를 찾았습니다."
                    )

                    for index, disease in enumerate(hira_results):
                        with st.container(border=True):
                            st.markdown(
                                f"**{index + 1}. "
                                f"{disease['질병명']}**"
                            )

                            st.write(
                                f"상병코드: {disease['상병코드']}"
                            )

                            st.write(
                                f"영문명: {disease['영문명']}"
                            )

                            # 기존 VITRA 시각화 데이터에 등록된 질환인지 확인
                            matched_disease = None

                            for registered_name, info in DISEASE_DATA.items():
                                if (
                                    disease["질병명"] == registered_name
                                    or disease["질병명"]
                                    in info["keywords"]
                                ):
                                    matched_disease = registered_name
                                    break

                            if matched_disease:
                                st.success(
                                    f"VITRA 등록 질환: {matched_disease}"
                                )
                                st.caption(
                                    "기존 VITRA의 질환 시각화 데이터에 "
                                    "연결할 수 있는 질환입니다."
                                )
                            else:
                                st.info(
                                    "질병명·코드 조회 가능 / "
                                    "VITRA 시각화 정보는 아직 미등록"
                                )

                else:
                    st.info(
                        "검색 결과가 없습니다. "
                        "질병명의 일부만 입력해 다시 검색해 보세요."
                    )

            except requests.exceptions.Timeout:
                st.error(
                    "API 응답 시간이 초과되었습니다. "
                    "잠시 후 다시 시도해 주세요."
                )

            except requests.exceptions.RequestException as error:
                st.error(
                    "API 연결에 실패했습니다. "
                    "인증키와 API 주소, 네트워크 상태를 확인해 주세요."
                )
                st.caption(str(error))

            except ET.ParseError:
                st.error(
                    "API 응답을 XML로 읽을 수 없습니다. "
                    "인증키나 API 응답 형식을 확인해 주세요."
                )

            except ValueError as error:
                st.error(str(error))

            except Exception as error:
                st.error("검색 중 예상하지 못한 오류가 발생했습니다.")
                st.caption(str(error))



# =========================================================
# VITRA 8차시: HIRA 질병정보 API 연결
# main.py 맨 아래에 추가
# =========================================================

import requests
import xml.etree.ElementTree as ET

import requests
import xml.etree.ElementTree as ET
import streamlit as st

HIRA_DISEASE_API_URL = (
    "https://apis.data.go.kr/"
    "B551182/diseaseInfoService1/getDissNameCodeList1"
)


def get_xml_value(element, names):
    names = {name.lower() for name in names}

    for child in element.iter():
        tag = child.tag.split("}")[-1].lower()

        if tag in names and child.text:
            return child.text.strip()

    return ""


def search_hira_disease(search_text):
    api_key = st.secrets.get("HIRA_API_KEY", "")

    if not api_key:
        return [], "Streamlit Secrets에서 HIRA_API_KEY를 확인해 주세요."

    params = {
        "ServiceKey": api_key,
        "pageNo": 1,
        "numOfRows": 20,
        "sickType": "1",
        "medTp": "1",
        "diseaseType": "SICK_NM",
        "searchText": search_text.strip(),
    }

    try:
        response = requests.get(
            HIRA_DISEASE_API_URL,
            params=params,
            timeout=15,
        )

        if response.status_code != 200:
            return [], (
                f"API 요청 실패 (HTTP {response.status_code}). "
                "요청 주소와 매개변수를 확인해 주세요."
            )

        root = ET.fromstring(response.content)

        result_code = get_xml_value(root, ["resultCode"])
        result_message = get_xml_value(root, ["resultMsg"])

        if result_code and result_code not in ("00", "0000"):
            return [], (
                f"API 응답 오류: {result_code} - "
                f"{result_message or '요청을 처리하지 못했습니다.'}"
            )

        items = []

        for item in root.iter():
            if item.tag.split("}")[-1].lower() != "item":
                continue

            disease_code = get_xml_value(
                item, ["sickCd", "SICK_CD"]
            )
            disease_name = get_xml_value(
                item, ["sickNm", "SICK_NM"]
            )
            english_name = get_xml_value(
                item, ["engNm", "ENG_NM", "engSickNm"]
            )

            if disease_name or disease_code:
                items.append({
                    "질병명": disease_name or "정보 없음",
                    "상병코드": disease_code or "정보 없음",
                    "영문명": english_name or "정보 없음",
                })

        if not items:
            return [], "검색 결과가 없습니다. 검색어를 확인해 주세요."

        return items, None

    except requests.RequestException:
        return [], "API 연결에 실패했습니다. 네트워크를 확인해 주세요."
    except ET.ParseError:
        return [], "API 응답을 XML로 읽지 못했습니다."


# Streamlit 화면
st.subheader("HIRA 질병정보 검색")

search_text = st.text_input(
    "질병명 입력",
    placeholder="예: 충수염",
    key="hira_disease_search_text",
)

if st.button("HIRA API 검색", key="hira_disease_search_button"):
    if not search_text.strip():
        st.warning("질병명을 입력해 주세요.")
    else:
        results, error = search_hira_disease(search_text)

        if error:
            st.error(error)
        else:
            st.success(f"{len(results)}개 결과를 찾았습니다.")
            st.dataframe(results, use_container_width=True)


# ---------------------------------------------------------
# API 검색 화면
# ---------------------------------------------------------

st.divider()
st.header("🌐 HIRA 공공 질병정보 API")
st.write("건강보험심사평가원에서 질병명과 상병코드를 조회합니다.")

st.caption(
    "API에서 조회되는 질병명 전체가 VITRA의 증상 분석 대상인 것은 아닙니다. "
    "기존 분석 데이터가 있는 질환만 신체·치료 시각화에 연결됩니다."
)

with st.form("hira_api_search_form"):
    api_search_text = st.text_input(
        "질병명 검색",
        placeholder="예: 장염, 췌장염, 충수염",
    )
    api_search_submit = st.form_submit_button(
        "HIRA API 검색",
        use_container_width=True,
    )

if api_search_submit:
    if not api_search_text.strip():
        st.warning("검색할 질병명을 입력해 주세요.")
    else:
        try:
            with st.spinner("HIRA API에 연결하고 있습니다..."):
                api_results, api_error = search_hira_disease(
                    api_search_text.strip()
                )

            if api_error:
                st.error(api_error)

            elif not api_results:
                st.info(
                    "검색 결과가 없습니다. 다른 질병명을 입력해 보세요."
                )

            else:
                st.success(f"API 검색 결과: {len(api_results)}건")

                for item in api_results:
                    if not isinstance(item, dict):
                        continue

                    disease_name = item.get("질병명", "정보 없음")
                    disease_code = item.get("상병코드", "정보 없음")
                    english_name = item.get("영문명", "정보 없음")

                    with st.container(border=True):
                        st.markdown(f"**{disease_name}**")
                        st.write(f"상병코드: {disease_code}")
                        st.write(f"영문명: {english_name}")

                        if disease_name in DISEASE_DATA:
                            st.success(
                                "VITRA 분석 지원: 기존 질환 데이터와 연결됨"
                            )
                        else:
                            st.warning(
                                "질병명 조회 가능 · VITRA 분석 데이터 미등록"
                            )

        except KeyError:
            st.error(
                "Streamlit Secrets에서 HIRA_API_KEY를 확인해 주세요."
            )
        except requests.exceptions.RequestException:
            st.error(
                "API 연결에 실패했습니다. 인증키와 네트워크를 확인해 주세요."
            )
        except ET.ParseError:
            st.error("API 응답을 XML로 해석하지 못했습니다.")
        except ValueError as error:
            st.error(str(error))
        except Exception as error:
            st.error("검색 중 오류가 발생했습니다.")
            st.caption(f"오류 유형: {type(error).__name__}: {error}")

