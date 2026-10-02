import streamlit as st
import requests

API_KEY = "185a24e9e330b5a71ceb3495879128988532b7ecfd102cba636ae1c408a7450f"
BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService01/getDrugPrdtPrmsnInq08"

st.title("💊 의약품 허가정보 검색")
st.write("식품의약품안전처 의약품 제품 허가정보 API 활용")

drug_name = st.text_input("검색할 의약품명을 입력하세요:")

if st.button("검색하기"):
    if drug_name.strip() == "":
        st.warning("의약품명을 입력해주세요.")
    else:
        url = f"{BASE_URL}?serviceKey={API_KEY}&type=json&item_name={drug_name}"
        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()
                if "body" in data and "items" in data["body"]:
                    items = data["body"]["items"]
                    if len(items) > 0:
                        st.success(f"총 {len(items)}개의 결과가 검색되었습니다.")
                        for item in items:
                            st.subheader(item.get("ITEM_NAME", "의약품명 없음"))
                            st.write(f"허가번호: {item.get('PRMSN_NO', '정보 없음')}")
                            st.write(f"허가일자: {item.get('PRMSN_DT', '정보 없음')}")
                            st.write(f"제조원: {item.get('MNFC_INST_NM', '정보 없음')}")
                            st.write(f"성상: {item.get('DRUG_SHAPE', '정보 없음')}")
                            st.write("---")
                    else:
                        st.warning("검색 결과가 없습니다.")
                else:
                    st.error("API 응답에 데이터가 없습니다.")
            except Exception as e:
                st.error(f"JSON 파싱 오류: {e}")
                st.text(response.text)
        else:
            st.error(f"API 요청 실패: {response.status_code}")
            st.text(response.text)
