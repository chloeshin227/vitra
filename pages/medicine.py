import streamlit as st

st.set_page_config(
    page_title="VITRA | 의약품 정보",
    page_icon="💊",
    layout="wide"
)


# =========================================================
# 테스트용 의약품 데이터
# =========================================================
# 현재는 식약처 API 키가 없기 때문에 테스트 데이터를 사용합니다.
# 나중에 이 부분을 실제 API 데이터로 교체합니다.
# =========================================================

MEDICINES = [
    {
        "name": "예시 의약품 A",
        "ingredient": "예시 성분 A",
        "form": "정제",
        "company": "예시 제약회사",
        "approval_date": "2024-03-15",
        "status": "허가",
        "rare": "아니오",
        "effect": "예시 의약품 A의 효능·효과 정보가 표시되는 영역입니다.",
        "caution": "사용상의 주의사항이 표시되는 영역입니다.",
        "interaction": "다른 의약품과 함께 사용할 때 확인해야 할 정보가 표시됩니다.",
        "pediatric": "소아 환자와 관련된 공식 정보가 표시되는 영역입니다.",
        "special": [
            "현재는 테스트 데이터입니다.",
            "실제 식약처 API 연결 후 공식 허가정보로 교체됩니다."
        ]
    },
    {
        "name": "예시 의약품 B",
        "ingredient": "예시 성분 B",
        "form": "시럽",
        "company": "예시 바이오",
        "approval_date": "2023-08-21",
        "status": "허가",
        "rare": "확인 필요",
        "effect": "예시 의약품 B의 효능·효과 정보가 표시되는 영역입니다.",
        "caution": "사용상의 주의사항이 표시되는 영역입니다.",
        "interaction": "상호작용 관련 공식 정보가 표시되는 영역입니다.",
        "pediatric": "소아 관련 공식 정보가 표시되는 영역입니다.",
        "special": [
            "희귀의약품 여부를 공식 자료에서 확인해야 합니다.",
            "실제 API 연결 후 자동으로 업데이트됩니다."
        ]
    },
    {
        "name": "소아용 예시 시럽",
        "ingredient": "예시 성분 C",
        "form": "시럽제",
        "company": "VITRA 테스트 제약",
        "approval_date": "2025-01-10",
        "status": "허가",
        "rare": "아니오",
        "effect": "소아 환자를 대상으로 하는 의약품 정보의 테스트 예시입니다.",
        "caution": "연령과 관련된 공식 주의사항이 표시될 영역입니다.",
        "interaction": "병용 의약품과 관련된 정보가 표시될 영역입니다.",
        "pediatric": "소아 관련 허가정보를 별도로 확인할 수 있도록 구성했습니다.",
        "special": [
            "소아 관련 정보를 별도로 확인할 수 있습니다.",
            "실제 데이터에서는 식약처 공식 정보를 표시합니다."
        ]
    }
]


# =========================================================
# 검색 함수
# =========================================================

def search_medicines(keyword):
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for medicine in MEDICINES:

        name = medicine["name"].lower()
        ingredient = medicine["ingredient"].lower()

        if keyword in name or keyword in ingredient:
            results.append(medicine)

    return results


# =========================================================
# 제목
# =========================================================

st.title("💊 의약품 정보 탐색")

st.caption("VITRA Medical Information Visualization")


# =========================================================
# 안내
# =========================================================

st.info(
    "의약품명 또는 주성분을 검색하여 기본 정보와 "
    "추가적으로 확인할 수 있는 정보를 한 화면에서 "
    "확인할 수 있도록 구성한 프로토타입입니다."
)


# =========================================================
# 검색
# =========================================================

st.subheader("🔎 의약품 검색")

keyword = st.text_input(
    "의약품명 또는 주성분을 입력하세요",
    placeholder="예: 예시 의약품 A"
)

search_clicked = st.button(
    "🔍 검색",
    use_container_width=True
)


# =========================================================
# 검색 실행
# =========================================================

if search_clicked:

    results = search_medicines(keyword)

    if not keyword.strip():

        st.warning(
            "의약품명 또는 주성분을 입력해주세요."
        )

        st.session_state["medicine_results"] = []

    elif not results:

        st.warning(
            "검색 결과가 없습니다."
        )

        st.session_state["medicine_results"] = []

    else:

        st.session_state["medicine_results"] = results


# =========================================================
# 검색 결과
# =========================================================

if "medicine_results" in st.session_state:

    results = st.session_state["medicine_results"]

    if results:

        st.divider()

        st.subheader(
            "📋 검색 결과"
        )

        st.write(
            "검색된 의약품:",
            len(results),
            "건"
        )

        medicine_names = []

        for medicine in results:
            medicine_names.append(
                medicine["name"]
            )

        selected_name = st.selectbox(
            "확인할 의약품을 선택하세요",
            medicine_names
        )

        selected = None

        for medicine in results:

            if medicine["name"] == selected_name:
                selected = medicine
                break


        # =================================================
        # 기본 정보
        # =================================================

        st.divider()

        st.subheader("1. 기본 정보")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "의약품명",
                selected["name"]
            )

        with col2:

            st.metric(
                "주성분",
                selected["ingredient"]
            )

        with col3:

            st.metric(
                "제형",
                selected["form"]
            )


        col4, col5, col6 = st.columns(3)

        with col4:

            st.write("**제조·수입업체**")

            st.write(
                selected["company"]
            )

        with col5:

            st.write("**허가일자**")

            st.write(
                selected["approval_date"]
            )

        with col6:

            st.write("**허가 상태**")

            st.write(
                selected["status"]
            )


        # =================================================
        # 추가 확인 정보
        # =================================================

        st.divider()

        st.subheader(
            "2. 🔎 추가 확인 정보"
        )

        st.caption(
            "일반적인 제품 정보 외에 검색 과정에서 "
            "추가적으로 확인할 수 있도록 구성한 영역입니다."
        )

        if selected["rare"] == "예":

            st.warning(
                "⚠️ 희귀의약품으로 표시되어 있습니다."
            )

        elif selected["rare"] == "확인 필요":

            st.info(
                "희귀의약품 여부를 공식 자료에서 확인해야 합니다."
            )

        else:

            st.write(
                "희귀의약품 여부:",
                selected["rare"]
            )


        for item in selected["special"]:

            st.write(
                "•",
                item
            )


        # =================================================
        # 상세 정보
        # =================================================

        st.divider()

        st.subheader(
            "3. 📖 상세 정보"
        )

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "효능·효과",
                "주의사항",
                "상호작용",
                "소아 관련 정보"
            ]
        )


        with tab1:

            st.write(
                selected["effect"]
            )


        with tab2:

            st.warning(
                selected["caution"]
            )


        with tab3:

            st.write(
                selected["interaction"]
            )


        with tab4:

            st.write(
                selected["pediatric"]
            )


        # =================================================
        # AI 요약
        # =================================================

        st.divider()

        st.subheader(
            "4. 🤖 AI 정보 요약"
        )

        st.caption(
            "현재는 테스트 단계입니다. "
            "향후 공식 의약품 데이터를 AI가 요약하도록 연결합니다."
        )

        if st.button(
            "🤖 정보 요약하기",
            use_container_width=True
        ):

            st.success(
                "정보 요약이 완료되었습니다."
            )

            st.markdown(
                f"""
### {selected["name"]}

**기본 정보**

- 주성분: {selected["ingredient"]}
- 제형: {selected["form"]}
- 제조·수입업체: {selected["company"]}
- 허가일자: {selected["approval_date"]}

**확인할 사항**

- 효능·효과
- 사용상의 주의사항
- 상호작용
- 소아 관련 정보
- 희귀의약품 여부

현재 표시되는 내용은 테스트 데이터입니다.

실제 구현에서는 식약처 API에서 받은 공식 정보를
AI가 요약하도록 연결할 예정입니다.
"""
            )


        # =================================================
        # 데이터 처리 구조
        # =================================================

        st.divider()

        st.subheader(
            "5. ⚙️ VITRA 데이터 처리 구조"
        )

        flow1, flow2, flow3, flow4 = st.columns(4)

        with flow1:

            st.markdown("### ①")

            st.write(
                "의약품 검색"
            )

        with flow2:

            st.markdown("### ②")

            st.write(
                "공식 데이터 조회"
            )

        with flow3:

            st.markdown("### ③")

            st.write(
                "정보 구조화"
            )

        with flow4:

            st.markdown("### ④")

            st.write(
                "AI 요약"


            )


# =========================================================
# 현재 개발 상태
# =========================================================

st.divider()

with st.expander("🛠 현재 개발 상태"):

    st.write(
        "현재는 식약처 API 연결 전 단계입니다."
    )

    st.write(
        "따라서 테스트용 의약품 데이터를 사용하고 있습니다."
    )

    st.write(
        "API 인증키를 발급받으면 실제 공식 데이터로 교체할 예정입니다."
    )


# =========================================================
# 주의사항
# =========================================================

st.divider()

st.caption(
    "⚠️ 본 페이지는 의약품 정보 탐색 및 교육 목적의 프로토타입입니다. "
    "처방이나 투약 결정을 대신하지 않습니다."
)
