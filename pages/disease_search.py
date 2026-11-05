import streamlit as st
import requests
import xml.etree.ElementTree as ET
import csv
from io import StringIO


# =========================================================
# HIRA 질병정보 API 설정
# =========================================================

HIRA_DISEASE_API_URL = (
    "https://apis.data.go.kr/"
    "B551182/diseaseInfoService1/getDissNameCodeList1"
)

CACHE_TTL = 300
MAX_SEARCH_LENGTH = 50


# =========================================================
# XML 데이터 처리
# =========================================================

def get_xml_value(element, names):

    names = {name.lower() for name in names}

    for child in element.iter():

        tag = child.tag.split("}")[-1].lower()

        if tag in names and child.text:
            return child.text.strip()

    return ""


def normalize_search_text(search_text):

    if not isinstance(search_text, str):
        return ""

    return " ".join(search_text.split())


# =========================================================
# HIRA 질병정보 검색
# =========================================================
@st.cache_data(ttl=CACHE_TTL, show_spinner=False)
def fetch_hira_response(search_text, api_key):

    params = {
        "ServiceKey": api_key,
        "pageNo": "1",
        "numOfRows": "20",
        "sickType": "1",
        "medTp": "1",
        "diseaseType": "SICK_NM",
        "searchText": search_text,
    }

    response = requests.get(
        HIRA_DISEASE_API_URL,
        params=params,
        timeout=15,
    )

    response.raise_for_status()

    return response.content


def search_hira_disease(search_text):

    api_key = st.secrets.get("HIRA_API_KEY", "")

    if not api_key:
        return [], "HIRA_API_KEY가 없습니다. Streamlit Secrets 설정을 확인해 주세요."

    try:

        content = fetch_hira_response(search_text, api_key)
        root = ET.fromstring(content)

        result_code = get_xml_value(
            root,
            ["resultCode", "RESULTCODE"]
        )

        result_message = get_xml_value(
            root,
            ["resultMsg", "RESULTMSG"]
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

            identity = (
                disease_name.casefold(),
                disease_code.casefold()
            )

            if identity in seen:
                continue

            seen.add(identity)

            items.append({
                "질병명": disease_name or "정보 없음",
                "상병코드": disease_code or "정보 없음",
                "영문명": english_name or "정보 없음",
            })

        if not items:
            return [], "검색 결과가 없습니다. 다른 질병명을 입력해 보세요."

        return items, None

    except requests.exceptions.Timeout:
        return [], "API 응답 시간이 초과되었습니다. 다시 시도해 주세요."

    except requests.exceptions.RequestException:
        return [], "API 연결 또는 요청에 실패했습니다. 네트워크와 API 설정을 확인해 주세요."

    except ET.ParseError:
        return [], "API 응답을 XML로 해석하지 못했습니다."

    except Exception as error:
        return [], f"검색 중 오류가 발생했습니다 ({type(error).__name__})."

# =========================================================
# 화면
# =========================================================

st.title("🔎 HIRA 질병정보 검색")

st.write(
    "건강보험심사평가원 API를 이용해 "
    "질병명과 상병코드를 조회합니다."
)

st.caption(
    "검색 결과는 질병명과 코드 확인을 위한 정보입니다. "
    "검색 결과만으로 증상, 장기 위치, 치료 및 수술 정보를 "
    "판단하지 않습니다."
)


# =========================================================
# 검색 입력
# =========================================================

with st.form("hira_disease_search_form"):

    search_text = st.text_input(
        "검색할 질병명",
        placeholder="예: 충수염, 지방간, 간염",
        max_chars=MAX_SEARCH_LENGTH,
    )

    search_button = st.form_submit_button(
        "공공 질병정보 검색",
        use_container_width=True,
    )


# =========================================================
# 검색 실행
# =========================================================

if search_button:

    # 새로운 검색을 시작하면 이전 결과 초기화
    st.session_state.pop(
        "hira_search_results",
        None
    )

    st.session_state.pop(
        "hira_search_keyword",
        None
    )

    normalized_text = normalize_search_text(search_text)

    if not normalized_text:

        st.warning("검색할 질병명을 입력해 주세요.")

    elif len(normalized_text) > MAX_SEARCH_LENGTH:

        st.warning(
            f"검색어는 {MAX_SEARCH_LENGTH}자 이하로 입력해 주세요."
        )

    else:

        with st.spinner("질병정보를 검색하고 있습니다..."):

            results, error_message = search_hira_disease(
                normalized_text
            )

        if error_message:

            st.error(error_message)

        else:

            st.session_state["hira_search_results"] = results
            st.session_state["hira_search_keyword"] = normalized_text


# =========================================================
# 검색 결과 출력
# =========================================================

if "hira_search_results" in st.session_state:

    results = st.session_state["hira_search_results"]
    keyword = st.session_state.get(
        "hira_search_keyword",
        ""
    )

    st.divider()

    st.subheader("📋 검색 결과")

    st.caption(f"검색어: {keyword}")

    st.success(f"검색 결과: {len(results)}건")

    for index, disease in enumerate(results, start=1):

        with st.container(border=True):

            st.markdown(
                f"**{index}. {disease['질병명']}**"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.caption("상병코드")
                st.code(disease["상병코드"])

            with col2:
                st.caption("영문명")
                st.write(disease["영문명"])

        # =====================================================
    # 검색 결과 CSV 다운로드
    # =====================================================

    csv_buffer = StringIO()

    writer = csv.DictWriter(
        csv_buffer,
        fieldnames=["질병명", "상병코드", "영문명"]
    )

    writer.writeheader()
    writer.writerows(results)

    st.download_button(
        label="📥 검색 결과 CSV 다운로드",
        data="\ufeff" + csv_buffer.getvalue(),
        file_name=f"HIRA_질병정보_{keyword}.csv",
        mime="text/csv",
        use_container_width=True,
    )
    if st.button(
        "검색 결과 지우기",
        use_container_width=True
    ):

        st.session_state.pop(
            "hira_search_results",
            None
        )

        st.session_state.pop(
            "hira_search_keyword",
            None
        )

        st.rerun()
