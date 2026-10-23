import streamlit as st
import requests

# ==================================================
# 페이지 설정
# ==================================================

st.set_page_config(
    page_title="의약품 정보",
    page_icon="💊",
    layout="wide"
)

# ==================================================
# 스타일
# ==================================================

st.markdown("""
<style>

.hero-box {
    padding: 1.5rem;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        #eef6ff 0%,
        #f8fbff 60%,
        #eefbf7 100%
    );
    border: 1px solid #dce9f5;
    margin-bottom: 1.5rem;
}

.drug-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e3ebf3;
}

.info-box {
    background: #eef8ff;
    padding: 15px;
    border-radius: 12px;
    border-left: 6px solid #2196F3;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# 상단 설명
# ==================================================

st.markdown("""
<div class="hero-box">
    <h1>💊 의약품 정보 검색</h1>
    <p>
        식품의약품안전처 e약은요 데이터를 기반으로
        환자가 이해하기 쉬운 의약품 정보를 제공합니다.
    </p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# API 설정
# ==================================================

API_KEY = st.secrets["MFDS_API_KEY"]

BASE_URL = (
    "https://apis.data.go.kr/1471000/"
    "DrbEasyDrugInfoService/getDrbEasyDrugList"
)

# ==================================================
# 텍스트 정리
# ==================================================

def safe_text(text):

    if text is None:
        return "정보 없음"

    text = str(text)

    # 취소선 방지
    text = text.replace("~", "\\~")

    # 줄바꿈 유지
    text = text.replace("\n", "\n\n")

    return text

# ==================================================
# 검색 함수
# ==================================================

def search_medicine(keyword):

    params = {
        "serviceKey": API_KEY,
        "itemName": keyword,
        "pageNo": 1,
        "numOfRows": 20,
        "type": "json"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30
    )

    data = response.json()

    body = data.get("body", {})

    items = body.get("items", [])

    if isinstance(items, dict):
        items = [items]

    return items

# ==================================================
# 검색창
# ==================================================

keyword = st.text_input(
    "의약품명을 검색하세요",
    placeholder="예: 타이레놀"
)

# ==================================================
# 검색
# ==================================================

if st.button(
    "🔍 검색하기",
    type="primary",
    use_container_width=True
):

    if not keyword.strip():

        st.warning(
            "의약품명을 입력해주세요."
        )

    else:

        with st.spinner(
            "의약품 정보를 불러오는 중..."
        ):

            items = search_medicine(
                keyword
            )

        if len(items) == 0:

            st.warning(
                "검색 결과가 없습니다."
            )

        else:

            st.success(
                f"{len(items)}건 검색되었습니다."
            )

            for item in items:

                medicine_name = item.get(
                    "itemName",
                    "의약품명 없음"
                )

                company = item.get(
                    "entpName",
                    "-"
                )

                with st.expander(
                    f"💊 {medicine_name}"
                ):

                    st.markdown(
                        f"""
                        <div class="drug-card">
                        <h3>{medicine_name}</h3>
                        <b>제조사:</b> {company}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown("### 📋 어떤 증상에 사용하나요?")

                    st.success(
                        safe_text(
                            item.get(
                                "efcyQesitm"
                            )
                        )
                    )

                    st.markdown("### 💊 어떻게 복용하나요?")

                    st.info(
                        safe_text(
                            item.get(
                                "useMethodQesitm"
                            )
                        )
                    )

                    st.markdown("### ⚠️ 복용 전 반드시 확인하세요")

                    st.warning(
                        safe_text(
                            item.get(
                                "atpnQesitm"
                            )
                        )
                    )

                    st.markdown("### 🚨 중요한 경고")

                    st.error(
                        safe_text(
                            item.get(
                                "atpnWarnQesitm"
                            )
                        )
                    )

                    st.markdown("### 🚫 함께 복용 시 주의")

                    st.markdown(
                        safe_text(
                            item.get(
                                "intrcQesitm"
                            )
                        )
                    )

                    st.markdown("### 🤒 발생 가능한 부작용")

                    st.markdown(
                        safe_text(
                            item.get(
                                "seQesitm"
                            )
                        )
                    )

                    st.markdown("### 📦 보관 방법")

                    st.info(
                        safe_text(
                            item.get(
                                "depositMethodQesitm"
                            )
                        )
                    )

                    st.divider()

                    with st.expander(
                        "👨‍⚕️ 의료진 참고 정보"
                    ):

                        st.write(
                            f"제조사: {company}"
                        )

                        st.write(
                            f"품목코드: {item.get('itemSeq','-')}"
                        )

                        st.write(
                            f"공개일: {item.get('openDe','-')}"
                        )

                        st.write(
                            f"수정일: {item.get('updateDe','-')}"
                        )

                        if item.get("bizrno"):
                            st.write(
                                f"사업자번호: {item.get('bizrno')}"
                            )

# ==================================================
# 안내
# ==================================================

st.divider()

st.caption(
    "※ 본 정보는 식품의약품안전처 e약은요(OpenAPI)를 기반으로 제공됩니다."
)
