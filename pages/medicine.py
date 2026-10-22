import streamlit as st
import requests

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"
SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"

st.title("의약품 검색")

keyword = st.text_input("검색어")

if st.button("검색"):

    params = {
        "serviceKey": st.secrets["MFDS_API_KEY"],
        "type": "json",
        "pageNo": 1,
        "numOfRows": 5,
        "item_name": keyword
    }

    r = requests.get(SEARCH_URL, params=params)

    st.write("상태코드:", r.status_code)

    try:
        st.json(r.json())
    except:
        st.text(r.text)
