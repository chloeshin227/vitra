import streamlit as st

st.set_page_config(
    page_title="VITRA | 의약품 정보",
    page_icon="💊",
    layout="wide"
)

st.title("💊 의약품 정보 탐색")

st.info(
    "현재 API 연결 전 테스트 페이지입니다."
)

medicine = st.text_input(
    "의약품명 또는 성분명을 입력하세요",
    placeholder="예: 예시 의약품 A"
)

if st.button("검색"):
    if medicine:
        st.success(f"'{medicine}' 검색을 시작합니다.")
    else:
        st.warning("검색어를 입력해주세요.")

st.divider()

st.subheader("🔎 추가 확인 정보")

st.write("식약처 API 연결 후 실제 의약품 정보가 표시됩니다.")

st.subheader("🤖 AI 정보 요약")

st.write("공식 정보를 기반으로 핵심 내용을 요약하는 기능입니다.")

st.caption(
    "현재는 개발 단계이며 실제 의약품 데이터는 연결되지 않았습니다."
)
