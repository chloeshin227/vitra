import streamlit as st
import requests

# ==================================================
# API 설정
# ==================================================

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"

SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"
DETAIL_URL = f"{BASE_URL}/getDrugPrdtPrmsnDtlInq08"

# ==================================================
# 페이지 설정
# ==================================================

st.title("💊 의약품 정보 검색")

st.write(
    "식품의약품안전처 의약품 제품 허가정보 API를 활용한 검색 서비스"
)

# ==================================================
# 의약품 목록 검색
# ==================================================

def search_medicine(keyword):

    params = {
        "serviceKey": st.secrets["MFDS_API_KEY"],
        "type": "json",
        "pageNo": 1,
        "numOfRows": 20,
        "item_name": keyword
    }

    response = requests.get(
        SEARCH_URL,
        params=params,
        timeout=30
    )

    data = response.json()

    body = data.get("body", {})

    return body.get("items", [])


# ==================================================
# 상세정보 조회
# ==================================================

def get_detail(item_seq):

    params = {
        "serviceKey": st.secrets["MFDS_API_KEY"],
        "type": "json",
        "item_seq": item_seq
    }

    response = requests.get(
        DETAIL_URL,
        params=params,
        timeout=30
    )

    return response.json()


# ==================================================
# 검색창
# ==================================================

keyword = st.text_input(
    "검색할 의약품명을 입력하세요",
    placeholder="예: 타이레놀"
)

# ==================================================
# 검색 버튼
# ==================================================

if st.button("검색하기"):

    st.write("✅ 검색 실행")

    if not keyword.strip():

        st.warning("의약품명을 입력해주세요.")

    else:

        with st.spinner("검색 중..."):

            items = search_medicine(keyword)

        if len(items) == 0:

            st.warning("검색 결과가 없습니다.")

        else:

            st.success(f"{len(items)}건 검색")

            for item in items:

                item_seq = item.get("ITEM_SEQ")

                medicine_name = item.get(
                    "ITEM_NAME",
                    "-"
                )

                company = item.get(
                    "ENTP_NAME",
                    "-"
                )

                
