import streamlit as st
import requests

API_KEY = st.secrets["MFDS_API_KEY"]

BASE_URL = (
    "https://apis.data.go.kr/1471000/"
    "DrbEasyDrugInfoService/getDrbEasyDrugList"
)

st.title("e약은요 API 테스트")

keyword = st.text_input(
    "의약품명",
    value="타이레놀"
)

if st.button("조회"):

    params = {
        "serviceKey": API_KEY,
        "pageNo": 1,
        "numOfRows": 5,
        "itemName": keyword,
        "type": "json"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30
    )

    st.write("응답코드:", response.status_code)

    try:
        data = response.json()
        st.json(data)

    except Exception:
        st.text(response.text)
