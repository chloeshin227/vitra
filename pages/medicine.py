import streamlit as st
import requests

# 공공데이터포털에서 발급받은 디코딩된 API 키 입력
API_KEY = "185a24e9e330b5a71ceb3495879128988532b7ecfd102cba636ae1c408a7450f"
BASE_URL = "https://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService01/getDrugPrdtPrmsnDtlInq08"

st.title("💊 의약품 주성분 상세정보 검색")
st.write("식품의약품안전처 의약품 제품 허가정보 API 활용")

# 사용자 입력
drug_name = st.text_input("검색할 의약품명을 입력하세요:")

if st.button("검색하기"):
    if drug_name.strip() == "":
        st.warning("의약품명을 입력해주세요.")
    else:
        # API 요청 URL 구성
        url = f"{BASE_URL}?serviceKey={API_KEY}&type=json&item_name={drug_name}"
        response = requests.get(url)

        st.write("응답 코드:", response.status_code)

        if response.status_code == 200:
            try:
                data = response.json()
                if "body" in data and "items" in data["body"]:
                    items = data["body"]["items"]
                    if len(items) > 0:
                        st.success(f"총 {len(items)}개의 주성분 정보가 검색되었습니다.")
                        for item in items:
                            st.subheader(item.get("ITEM_NAME", "의약품명 없음"))
                            st.write(f"주성분명: {item.get('MCPN_NM', '정보 없음')}")
                            st.write(f"함량: {item.get('MCPN_CPCT', '정보 없음')}")
                            st.write(f"단위: {item.get('MCPN_CPCT_UNIT', '정보 없음')}")
                            st.write(f"성분코드: {item.get('MCPN_CD', '정보 없음')}")
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
