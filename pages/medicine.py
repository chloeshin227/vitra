import streamlit as st
import requests

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"

SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"
DETAIL_URL = f"{BASE_URL}/getDrugPrdtPrmsnDtlInq08"

st.title("💊 의약품 정보 검색")

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

    return data.get("body", {}).get("items", [])


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


# 검색 결과 저장
if "results" not in st.session_state:
    st.session_state.results = []

keyword = st.text_input(
    "검색할 의약품명",
    placeholder="예: 타이레놀"
)

if st.button("검색하기"):

    st.session_state.results = search_medicine(keyword)

results = st.session_state.results

if len(results) > 0:

    st.success(f"{len(results)}건 검색")

    for item in results:

        medicine_name = item.get("ITEM_NAME", "-")
        item_seq = item.get("ITEM_SEQ")

        with st.expander(f"💊 {medicine_name}"):

            st.write(
                f"제조사 : {item.get('ENTP_NAME','-')}"
            )

            st.write(
                f"주성분 : {item.get('ITEM_INGR_NAME','-')}"
            )

            st.write(
                f"허가일 : {item.get('ITEM_PERMIT_DATE','-')}"
            )

            if st.button(
                f"상세정보 조회",
                key=f"detail_{item_seq}"
            ):

                detail = get_detail(item_seq)

                st.subheader("상세 API 응답")

                st.json(detail)
