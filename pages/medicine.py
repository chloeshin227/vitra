import streamlit as st
import requests

BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService08"
SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"

st.title("의약품 검색")

drug_name = st.text_input("의약품명 입력")

if st.button("검색"):

    params = {
        "serviceKey": st.secrets["MFDS_API_KEY"],
        "type": "json",
        "pageNo": 1,
        "numOfRows": 5,
    }

    response = requests.get(
        SEARCH_URL,
        params=params,
        timeout=30
    )

    st.write("상태코드:", response.status_code)

    try:
        data = response.json()
        st.json(data)
    except:
        st.text(response.text)
