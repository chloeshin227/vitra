import streamlit as st
from datetime import datetime


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="VITRA | 의약품 정보",
    page_icon="💊",
    layout="wide"
)


# =========================================================
# 테스트 데이터
# ※ 현재는 API 키가 없으므로 화면 테스트용으로만 사용
# ※ 추후 식약처 API 데이터로 교체
# =========================================================

TEST_MEDICINES = {
    "예시 의약품 A": {
        "product_name": "예시 의약품 A",
        "ingredient": "예시 성분 A",
        "form": "정제",
        "company": "예시 제약회사",
        "approval_date": "2024-03-15",
        "status": "허가",
        "rare": "아니오",
        "effect": (
            "이 영역에는 식품의약품안전처 공식 허가정보에서 "
            "제공되는 효능·효과 정보가 표시됩니다."
        ),
        "caution": (
            "이 영역에는 공식 허가사항에 포함된 "
            "사용상의 주의사항이 표시됩니다."
        ),
        "interaction": (
            "이 영역에는 공식 자료에서 확인되는 "
            "상호작용 관련 정보가 표시됩니다."
        ),
        "pediatric": (
            "이 영역에는 소아 환자와 관련하여 "
            "공식 자료에서 확인할 수 있는 정보가 표시됩니다."
        ),
        "special": [
            "현재는 테스트 데이터입니다.",
            "실제 API 연결 후 공식 허가정보를 기반으로 표시됩니다.",
            "AI는 제공된 공식 정보를 요약하는 역할을 합니다."
        ]
    },

    "예시 의약품 B": {
        "product_name": "예시 의약품 B",
        "ingredient": "예시 성분 B",
        "form": "시럽",
        "company": "예시 바이오",
        "approval_date": "2023-08-21",
        "status": "허가",
        "rare": "확인 필요",
        "effect": (
            "API 연결 후 해당 의약품의 공식 효능·효과 정보가 "
            "표시될 예정입니다."
        ),
        "caution": (
            "API 연결 후 해당 의약품의 공식 사용상의 "
            "주의사항이 표시될 예정입니다."
        ),
        "interaction": (
            "API 연결 후 공식 자료를 기반으로 "
            "관련 정보를 확인할 수 있습니다."
        ),
        "pediatric": (
            "API 연결 후 공식 자료에서 확인되는 "
            "소아 관련 정보를 표시합니다."
        ),
        "special": [
            "희귀의약품 여부는 공식 데이터 확인이 필요합니다.",
            "허가일자와 허가 상태를 함께 확인할 수 있습니다.",
            "실제 데이터 연결 시 이 영역이 자동으로 변경됩니다."
        ]
    }
}


# =========================================================
# API 연결부
# =========================================================
#
# 현재는 API 키가 없으므로 테스트 데이터를 반환합니다.
#
# 나중에 식약처 API를 연결할 때
# 이 함수 내부만 수정하면 됩니다.
#
# =========================================================

def fetch_medicine_from_api(search_text):
    """
    현재는 테스트 데이터 검색을 수행합니다.

    향후 식약처 API 연결 시:
        검색어
          ↓
        API 요청
          ↓
        JSON 응답
          ↓
        필요한 항목만 추출
          ↓
        아래와 같은 dictionary 반환

    형태로 변경할 예정입니다.
    """

    results = []

    search_text = search_text.strip().lower()

    if not search_text:
        return results

    for medicine_name, medicine_data in TEST_MEDICINES.items():

        searchable_text = (
            medicine_data["product_name"]
            + " "
            + medicine_data["ingredient"]
        ).lower()

        if search_text in searchable_text:
            results.append(medicine_data)

    return results


# =========================================================
# AI 요약 함수
# =========================================================
#
# 현재는 실제 AI API가 연결되지 않았기 때문에
# 공식 데이터가 들어온다는 전제하에 요약 UI만 구현합니다.
#
# 나중에 Gemini/OpenAI 등의 API를 연결할 수 있습니다.
# =========================================================

def create_ai_summary(medicine):
    """
    현재는 테스트용 요약을 반환합니다.

    실제 AI 연결 후에는
    medicine에 들어있는 공식 정보를 AI에게 전달하고
    그 내용을 요약하도록 변경할 예정입니다.
    """

    return f"""
### {medicine["product_name"]} 정보 요약

**기본 정보**
- 주성분: {medicine["ingredient"]}
- 제형: {medicine["form"]}
- 업체: {medicine["company"]}
- 허가일자: {medicine["approval_date"]}
- 허가 상태: {medicine["status"]}

**확인할 정보**
- 효능·효과
- 사용상의 주의사항
- 상호작용 관련 정보
- 소아 관련 정보

현재는 API 및 AI가 연결되지 않은 테스트 단계입니다.

실제 구현에서는 식약처 등 공식 자료에서 제공받은 정보를
바탕으로 핵심 내용을 요약하도록 구성합니다.

⚠️ 이 요약은 처방이나 투약 결정을 대신하지 않습니다.
"""


# =========================================================
# 제목
# =========================================================

st.title("💊 의약품 정보 탐색")

st.caption(
    "VITRA Medical Information Visualization"
)


# =========================================================
# 안내
# =========================================================

st.info(
    "의약품명 또는 주성분을 검색하여 관련 정보를 확인하고, "
    "일반적인 제품 정보에서 놓치기 쉬운 추가 정보를 "
    "한 화면에서 확인할 수 있도록 설계한 기능입니다."
)


# =========================================================
# 검색 영역
# =========================================================

st.subheader("🔎 의약품 검색")

search_col1, search_col2 = st.columns([5, 1])

with search_col1:
    search_text = st.text_input(
        "의약품명 또는 주성분",
        placeholder="예: 예시 의약품 A",
        label_visibility="collapsed"
    )

with search_col2:
    search_button = st.button(
        "검색",
        use_container_width=True
    )


# =========================================================
# 검색 실행
# =========================================================

if search_button:

    if not search_text.strip():

        st.warning(
            "검색할 의약품명 또는 주성분을 입력해주세요."
        )

    else:

        results = fetch_medicine_from_api(
            search_text
        )

        if not results:

            st.warning(
                f"'{search_text}'에 해당하는 테스트 데이터를 찾지 못했습니다."
            )

            st.caption(
                "현재는 API 키가 없어 테스트 데이터만 검색할 수 있습니다. "
                "식약처 API 연결 후 실제 의약품 검색으로 변경됩니다."
            )

        else:

            st.session_state["medicine_results"] = results


# =========================================================
# 검색 결과 표시
# =========================================================

if "medicine_results" in st.session_state:

    results = st.session_state["medicine_results"]

    st.divider()

    st.subheader(
        f"📋 검색 결과 ({len(results)}건)"
    )

    medicine_names = [
        medicine["product_name"]
        for medicine in results
    ]

    selected_name = st.selectbox(
        "확인할 의약품을 선택하세요",
        medicine_names
    )

    selected_medicine = next(
        medicine
        for medicine in results
        if medicine["product_name"] == selected_name
    )


    # =====================================================
    # 기본 정보
    # =====================================================

    st.divider()

    st.subheader("1. 기본 정보")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "의약품명",
            selected_medicine["product_name"]
        )

    with col2:
        st.metric(
            "주성분",
            selected_medicine["ingredient"]
        )

    with col3:
        st.metric(
            "제형",
            selected_medicine["form"]
        )


    col4, col5, col6 = st.columns(3)

    with col4:
        st.write("**제조·수입업체**")
        st.write(
            selected_medicine["company"]
        )

    with col5:
        st.write("**허가일자**")
        st.write(
            selected_medicine["approval_date"]
        )

    with col6:
        st.write("**허가 상태**")
        st.write(
            selected_medicine["status"]
        )


    # =====================================================
    # 특수 정보
    # =====================================================

    st.divider()

    st.subheader("2. 🔎 추가 확인 정보")

    st.caption(
        "일반적인 의약품 기본정보와 별도로 확인할 필요가 있는 "
        "정보를 모아 표시하는 영역입니다."
    )

    if selected_medicine["rare"] == "예":
        st.warning(
            "⚠️ 희귀의약품으로 표시된 의약품입니다."
        )

    elif selected_medicine["rare"] == "확인 필요":
        st.info(
            "희귀의약품 여부는 실제 공식 데이터를 통해 확인해야 합니다."
        )

    else:
        st.write(
            "희귀의약품 여부: "
            + selected_medicine["rare"]
        )


    for item in selected_medicine["special"]:
        st.write(
            "• " + item
        )


    # =====================================================
    # 상세 정보
    # =====================================================

    st.divider()

    st.subheader("3. 📖 상세 의약품 정보")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "효능·효과",
            "주의사항",
            "상호작용",
            "소아 관련 정보"
        ]
    )

    with tab1:

        st.markdown(
            selected_medicine["effect"]
        )

    with tab2:

        st.warning(
            selected_medicine["caution"]
        )

    with tab3:

        st.markdown(
            selected_medicine["interaction"]
        )

    with tab4:

        st.markdown(
            selected_medicine["pediatric"]
        )


    # =====================================================
    # AI 요약
    # =====================================================

    st.divider()

    st.subheader("4. 🤖 AI 정보 요약")

    st.caption(
        "공식 의약품 정보를 입력 자료로 받아 핵심 내용을 "
        "빠르게 파악할 수 있도록 요약하는 기능입니다."
    )

    if st.button(
        "🤖 정보 요약하기",
        use_container_width=True
    ):

        with st.spinner("정보를 정리하는 중..."):

            summary = create_ai_summary(
                selected_medicine
            )

        st.success(
            "정보 요약이 완료되었습니다."
        )

        st.markdown(
            summary
        )


    # =====================================================
    # 데이터 흐름 표시
    # =====================================================

    st.divider()

    st.subheader("5. ⚙️ 데이터 처리 구조")

    flow1, flow2, flow3, flow4 = st.columns(4)

    with flow1:
        st.markdown("### ①")
        st.write("의약품 검색")

    with flow2:
        st.markdown("### ②")
        st.write("공식 데이터")

    with flow3:
        st.markdown("### ③")
        st.write("정보 구조화")

    with flow4:
        st.markdown("### ④")
        st.write("AI 요약")


# =========================================================
# 현재 개발 단계 안내
# =========================================================

st.divider()

with st.expander("🛠 현재 개발 단계"):

    st.markdown(
        """
### 현재 구현된 부분

- 의약품명 / 주성분 검색 UI
- 검색 결과 선택
- 기본 의약품 정보 표시
- 추가 확인 정보 영역
- 상세 정보 탭
- AI 요약 UI
- 검색 결과가 없을 때의 오류 처리
- API 연결을 고려한 함수 구조

### 현재 연결되지 않은 부분

**식약처 실제 API**

현재는 API 인증키가 없기 때문에 테스트 데이터를 사용합니다.

향후:

```text
사용자 검색
      ↓
식약처 API
      ↓
실제 의약품 데이터
      ↓
VITRA에서 구조화
      ↓
AI 요약
