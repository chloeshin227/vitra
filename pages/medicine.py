import streamlit as st
import requests

# ==================================================
# API 설정
# ==================================================

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"

SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"

# ==================================================
# 페이지
# ==================================================

st.set_page_config(
    page_title="의약품 검색",
    page_icon="💊",
    layout="wide"
)

st.title("💊 의약품 정보 검색")

st.write(
    "식품의약품안전처 의약품 제품 허가정보 API를 활용한 검색 서비스"
)

# ==================================================
# API 호출
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

    items = body.get("items", [])

    if not isinstance(items, list):
        items = []

    return items


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

if st.button("검색하기", type="primary"):

    if keyword.strip() == "":
        st.warning("의약품명을 입력하세요.")

    else:

        with st.spinner("검색 중입니다..."):

            items = search_medicine(keyword)

        st.success(f"{len(items)}건 검색")

        if len(items) == 0:
            st.warning("검색 결과가 없습니다.")

        else:

            for item in items:

                medicine_name = item.get(
                    "ITEM_NAME",
                    "-"
                )

                company = item.get(
                    "ENTP_NAME",
                    "-"
                )

                ingredient = item.get(
                    "ITEM_INGR_NAME",
                    "-"
                )

                permit_date = item.get(
                    "ITEM_PERMIT_DATE",
                    "-"
                )

                category = item.get(
                    "PRDUCT_TYPE",
                    "-"
                )

                specialist = item.get(
                    "SPCLTY_PBLC",
                    "-"
                )

                ingredient_count = item.get(
                    "ITEM_INGR_CNT",
                    "-"
                )

                english_name = item.get(
                    "ITEM_ENG_NAME",
                    "-"
                )

                permit_no = item.get(
                    "PRDUCT_PRMISN_NO",
                    "-"
                )

                edi_code = item.get(
                    "EDI_CODE",
                    "-"
                )

                status = item.get(
                    "CANCEL_NAME",
                    "-"
                )

                image_url = item.get(
                    "BIG_PRDT_IMG_URL",
                    
