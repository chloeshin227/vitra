
import streamlit as st
import requests
import xml.etree.ElementTree as ET


# =========================================================
# HIRA 질병정보 API 설정
# =========================================================

HIRA_DISEASE_API_URL = (
    "https://apis.data.go.kr/"
    "B551182/diseaseInfoService1/getDissNameCodeList1"
)


def get_xml_value(element, names):
    """XML에서 지정한 태그의 값을 가져옵니다."""
    names = {name.lower() for name in names}

    for child in element.iter():
        tag = child.tag.split("}")[-1].lower()

        if tag in names and child.text:
            return child.text.strip()

    return ""


def search_hira_disease(search_text):
    """
    검색 결과와 오류 메시지를 반환합니다.
    성공: (검색 결과 리스트, None)
    실패: (빈 리스트, 오류 메시지)
    """

    api_key = st.secrets.get("HIRA_API_KEY", "")

    if not api_key:
        return [], (
            "HIRA_API_KEY가 없습니다. "
            "Streamlit Secrets 설정을 확인해 주세요."
        )

    params = {
        "ServiceKey": api_key,
        "pageNo": "1",
        "numOfRows": "20",
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
                "API 주소와 요청 매개변수를 확인해 주세요."
            )

        root = ET.fromstring(response.content)

        result_code = get_xml_value(
            root, ["resultCode", "RESULTCODE"]
        )
        result_message = get_xml_value(
            root, ["resultMsg", "RESULTMSG"]
        )

        if result_code and result_code not in ("00", "0000"):
            return [], (
                f"API 응답 오류: {result_code} - "
                f"{result_message or '요청 실패'}"
            )

        items = []
        seen = set()

        for element in root.iter():
            if element.tag.split("}")[-1].lower() != "item":
                continue

            disease_name = get_xml_value(
                element, ["sickNm", "SICK_NM"]
            )
            disease_code = get_xml_value(
                element, ["sickCd", "SICK_CD"]
            )
            english_name = get_xml_value(
                element, ["engNm", "ENG_NM", "engSickNm"]
            )

            if not disease_name and not disease_code:
                continue

            identity = (disease_name, disease_code)

            if identity in seen:
                continue

            seen.add(identity)

            items.append({
                "질병명": disease_name or "정보 없음",
                "상병코드": disease_code or "정보 없음",
                "영문명": english_name or "정보 없음",
            })

        if not items:
            return [], (
                "검색 결과가 없습니다. 다른 질병명을 입력해 보세요."
            )

        return items, None

    except requests.exceptions.Timeout:
        return [], "API 응답 시간이 초과되었습니다. 다시 시도해 주세요."

    except requests.exceptions.RequestException:
        return [], (
            "API 연결에 실패했습니다. "
            "네트워크와 API 설정을 확인해 주세요."
        )

    except ET.ParseError:
        return [], (
            "API 응답을 XML로 해석하지 못했습니다. "
            "API 응답 형식을 확인해 주세요."
        )

    except Exception as error:
        return [], (
            f"검색 중 오류가 발생했습니다 "
            f"({type(error).__name__})."
        )


# =========================================================
# 화면
# =========================================================

st.title("🔎 HIRA 질병정보 검색")

st.write(
    "건강보험심사평가원 API를 이용해 질병명과 상병코드를 조회합니다."
)

st.caption(
    "검색 결과는 질병명과 코드 확인을 위한 정보입니다. "
    "검색 결과만으로 증상, 장기 위치, 치료 및 수술 정보를 "
    "판단하지 않습니다."
)

with st.form("hira_disease_search_form"):
    search_text = st.text_input(
        "검색할 질병명",
        placeholder="예: 충수염, 지방간, 간염",
    )

    search_button = st.form_submit_button(
        "공공 질병정보 검색",
        use_container_width=True,
    )

if search_button:
    if not search_text.strip():
        st.warning("검색할 질병명을 입력해 주세요.")

    else:
        with st.spinner("질병정보를 검색하고 있습니다..."):
            results, error_message = search_hira_disease(search_text)

        if error_message:
            st.error(error_message)

        else:
            st.success(f"검색 결과: {len(results)}건")

            for index, disease in enumerate(results, start=1):
                with st.container(border=True):
                    st.markdown(
                        f"**{index}. {disease['질병명']}**"
                    )
                    st.write(f"상병코드: {disease['상병코드']}")
                    st.write(f"영문명: {disease['영문명']}")
