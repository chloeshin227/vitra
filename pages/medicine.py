import streamlit as st
import requests

# 공공데이터포털에서 발급받은 디코딩된 API 키 입력
API_KEY = "185a24e9e330b5a71ceb3495879128988532b7ecfd102cba636ae1c408a7450f"
BASE_URL = "https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList"

st.title("💊 의약품 검색 페이지")
st.write("공공데이터포털 API를 활용한 의약품 정보 검색")

# 사용자 입력
drug_name = st.text_input("검색할 의약품명을 입력하세요:")

if st.button("검색하기"):
    if drug_name.strip() == "":
        st.warning("의약품명을 입력해주세요.")
    else:
        # URL 직접 구성
        url = f"{BASE_URL}?serviceKey={API_KEY}&type=json&itemName={drug_name}"
        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()
                if "body" in data and "items" in data["body"]:
                    items = data["body"]["items"]
                    if len(items) > 0:
                        st.success(f"총 {len(items)}개의 결과가 검색되었습니다.")
                        for item in items:
                            st.subheader(item.get("itemName", "의약품명 없음"))
                            st.write(f"💊 효능: {item.get('efcyQesitm', '정보 없음')}")
                            st.write(f"⚠️ 주의사항: {item.get('atpnQesitm', '정보 없음')}")
                            st.write(f"🚫 상호작용: {item.get('intrcQesitm', '정보 없음')}")
                            st.write(f"👩‍⚕️ 복용법: {item.get('useMethodQesitm', '정보 없음')}")
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
