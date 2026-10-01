import streamlit as st

st.set_page_config(
    page_title="VITRA | 의약품 정보",
    page_icon="💊",
    layout="wide"
)

# ==========================================
# Secrets 확인
# ==========================================

API_KEY_EXISTS = "MFDS_API_KEY" in st.secrets


# ==========================================
# 테스트 데이터
# ==========================================

MEDICINES = [
    {
        "name": "예시 의약품 A",
        "ingredient": "예시 성분 A",
        "company": "예시 제약회사",
        "approval_date": "2024-01-01",
        "category": "일반 정보",
        "special": "개발 단계 테스트 데이터"
    },
    {
        "name": "예시 의약품 B",
        "ingredient": "예시 성분 B",
        "company": "예시 제약회사",
        "approval_date": "2023-06-15",
        "category": "일반 정보",
        "special": "개발 단계 테스트 데이터"
    },
    {
        "name": "소아용 예시 시럽",
        "ingredient": "예시 성분 C",
        "company": "예시 제약회사",
        "approval_date": "2025-02-20",
        "category": "소아 관련 테스트",
        "special": "실제 의약품 정보가 아닌 테스트 데이터"
    }
]


# ==========================================
# 테스트 데이터 검색
# ==========================================

def search_test_medicines(keyword):

    keyword = keyword.lower().strip()

    if not keyword:
        return []

    results = []

    for medicine in MEDICINES:

        text = (
            medicine["name"]
            + medicine["ingredient"]
            + medicine["company"]
        ).lower()

        if keyword in text:
            results.append(medicine)

    return results


# ==========================================
# 페이지 제목
# ==========================================

st.title("💊 의약품 정보 탐색")

st.write(
    "의약품과 관련된 공식 정보를 효율적으로 탐색하기 위한 "
    "VITRA의 정보 탐색 기능입니다."
)

st.divider()


# ==========================================
# API 연결 상태
# ==========================================

st.subheader("🔐 데이터 연결 상태")

if API_KEY_EXISTS:

    st.success(
        "공공데이터 API 인증키가 안전하게 등록되어 있습니다."
    )

    st.caption(
        "인증키 자체는 화면이나 코드에 표시하지 않습니다."
    )

else:

    st.warning(
        "아직 공공데이터 API 인증키가 등록되지 않았습니다."
    )

    st.caption(
        "Streamlit Cloud의 Settings → Secrets에서 "
        "MFDS_API_KEY를 등록하세요."
    )


st.divider()


# ==========================================
# 검색
# ==========================================

st.subheader("🔎 의약품 정보 검색")

keyword = st.text_input(
    "의약품명 또는 성분명을 입력하세요",
    placeholder="예: 의약품명 또는 성분명"
)

search_button = st.button(
    "검색",
    type="primary"
)


# ==========================================
# 결과
# ==========================================

if search_button:

    if not keyword:

        st.warning("검색어를 입력해주세요.")

    else:

        results = search_test_medicines(keyword)

        if results:

            st.success(
                f"{len(results)}개의 테스트 결과를 찾았습니다."
            )

            selected_name = st.selectbox(
                "확인할 항목을 선택하세요",
                [medicine["name"] for medicine in results]
            )

            selected = next(
                medicine
                for medicine in results
                if medicine["name"] == selected_name
            )

            st.divider()

            st.subheader("📋 기본 정보")

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**제품명:** {selected['name']}"
                )

                st.write(
                    f"**주성분:** {selected['ingredient']}"
                )

                st.write(
                    f"**제조사:** {selected['company']}"
                )

            with col2:

                st.write(
                    f"**허가일:** {selected['approval_date']}"
                )

                st.write(
                    f"**분류:** {selected['category']}"
                )

                st.write(
                    f"**특징:** {selected['special']}"
                )


            st.divider()

            st.subheader("📚 정보 정리")

            tab1, tab2, tab3 = st.tabs(
                [
                    "기본 정보",
                    "추가 확인 사항",
                    "데이터 출처"
                ]
            )

            with tab1:

                st.write(
                    "현재 표시되는 정보는 개발 단계의 "
                    "테스트 데이터입니다."
                )

            with tab2:

                st.info(
                    "실제 공공데이터 연동 단계에서는 "
                    "공식 데이터에 포함된 항목을 기준으로 "
                    "정보를 표시하도록 설계할 예정입니다."
                )

            with tab3:

                st.write(
                    "식품의약품안전처 의약품 관련 "
                    "공공데이터 활용을 목표로 설계되었습니다."
                )


        else:

            st.info(
                "일치하는 테스트 데이터를 찾지 못했습니다."
            )


# ==========================================
# 개발 구조
# ==========================================

st.divider()

with st.expander("🛠️ 3차시 개발 구조"):

    st.markdown(
        """
        **현재 구현된 구조**

        1. 의약품 검색창
        2. 검색 결과 표시
        3. 의약품 상세정보 UI
        4. API 인증키 보안 관리
        5. 공공데이터 연동을 위한 구조 분리

        **향후 개발**

        - 공식 공공데이터 연동
        - 반환 데이터 파싱
        - 검색 결과 정리
        - 공식 데이터 기반 정보 요약
        """
    )


# ==========================================
# 안내
# ==========================================

st.divider()

st.caption(
    "VITRA는 의료정보 탐색 및 교육을 위한 개발 프로젝트입니다. "
    "현재 페이지의 테스트 데이터는 실제 의약품 정보가 아닙니다."
)
