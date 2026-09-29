import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="VITRA API Test",
    page_icon="🩺"
)

st.title("🩺 VITRA - OpenAI API 연결 테스트")

st.write("아래 버튼을 눌러 OpenAI API 연결을 확인합니다.")

if st.button("🔌 API 연결 테스트", type="primary"):

    try:
        client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

        response = client.responses.create(
            model="gpt-5.6-luna",
            input="VITRA API 연결 테스트입니다. 연결되었다면 짧게 '연결 성공'이라고 답해주세요."
        )

        st.success("✅ OpenAI API 연결 성공!")
        st.write("AI 응답:")
        st.info(response.output_text)

    except Exception as e:
        st.error("❌ API 연결에 실패했습니다.")
        st.write("오류 내용:")
        st.code(str(e))
