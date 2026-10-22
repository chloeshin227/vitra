import streamlit as st
import requests
import pandas as pd

# ==================================================
# API 설정
# ==================================================

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"
SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"

st.set_page_config(
    page_title="의약품 검색",
    page_icon="💊",
    layout="wide"
)

st.title("💊 의약품 정보 검색")

st.write(
    "식품의약품안전처 의약품 제품 허가정보 API를 활용한 검색 서비스입니다."
)

# ==================================================
# API 조회 함수
# ==================================================

def search_medicine(keyword):

    params = {
        "serviceKey": st.secrets["MFDS_API_KEY"],
        "type": "json",
        "pageNo": 1,
        "numOfRows": 20,
        "item_name": keyword
    }

    try:

        response = requests.get(
            SEARCH_URL,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        body = data.get("body", {})

        return body.get("items", [])

    except Exception as e:
        st.error(f"API 호출 오류 : {e}")
        return []


# ==================================================
# 검색 UI
# ==================================================

keyword = st.text_input(
    "의약품명을 입력하세요",
    placeholder="예) 타이레놀"
)

if st.button("검색하기", type="primary"):

    if not keyword.strip():
        st.warning("의약품명을 입력해주세요.")

    else:

        with st.spinner("검색 중..."):

            items = search_medicine(keyword)

        if len(items) == 0:
            st.warning("검색 결과가 없습니다.")

        else:

            st.success(f"{len(items)}개의 의약품을 찾았습니다.")

            for i, item in enumerate(items, start=1):

                medicine_name = item.get("ITEM_NAME", "-")
                company = item.get("ENTP_NAME", "-")
                english_name = item.get("ITEM_ENG_NAME", "-")
                ingredient = item.get("ITEM_INGR_NAME", "-")
                ingredient_count = item.get("ITEM_INGR_CNT", "-")
                permit_date = item.get("ITEM_PERMIT_DATE", "-")
                drug_type = item.get("PRDUCT_TYPE", "-")
                specialist = item.get("SPCLTY_PBLC", "-")
                permit_no = item.get("PRDUCT_PRMISN_NO", "-")
                edi_code = item.get("EDI_CODE", "-")
                status = item.get("CANCEL_NAME", "-")

                with st.expander(
                    f"{i}. {medicine_name}",
                    expanded
