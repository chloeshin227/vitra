import streamlit as st
import requests

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"

SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"
DETAIL_URL = f"{BASE_URL}/getDrugPrdtPrmsnDtlInq08"

st.title("💊 의약품 검색")

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

    return data["body"]["items"]


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


keyword = st.text_input(
    "검색어",
    placeholder="타이레놀"
)

if st.button("검색"):

    items = search_medicine(keyword)

    for item in items:

        medicine_name = item.get("ITEM_NAME")

        with st.expander(medicine_name):

            st.write(
                f"제조사 : {item.get('ENTP_NAME')}"
            )

            st.write(
                f"성분 : {item.get('ITEM_INGR_NAME')}"
            )

            item_seq = item.get("ITEM_SEQ")

            if st.button(
                "상세정보 조회",
                key=item_seq
            ):

                detail = get_detail(item_seq)

                st.subheader("상세 API 응답")

                st.json(detail)
