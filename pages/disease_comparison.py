import streamlit as st
import pandas as pd


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="두 질환 비교 | VITRA",
    page_icon="⚖️",
    layout="wide"
)


# =========================================================
# 기존 페이지의 데이터 및 함수 가져오기
# =========================================================

# 기존 treatment_comparison.py에서 다음 항목을
# 그대로 복사해서 이 위치에 붙여넣으세요.
#
# 1. DISEASE_LIST
# 2. TREATMENT_DATA
# 3. display_method() 함수


# =========================================================
# 페이지 제목
# =========================================================

st.title("⚖️ 두 질환 비교")

st.write(
    "두 질환의 치료 방법과 치료 목적을 비교하여 "
    "질환별 치료 접근 방식의 차이를 확인합니다."
)

st.caption(
    "치료 방법은 질환의 상태와 환자의 특성에 따라 달라질 수 있으며, "
    "본 자료는 의료정보 이해를 위한 교육용 정보입니다."
)


# =========================================================
# 비교 가능한 질환 목록
# =========================================================

AVAILABLE_DISEASES = [
    disease
    for disease in DISEASE_LIST
    if disease in TREATMENT_DATA
]


# =========================================================
# 질환 선택
# =========================================================

st.divider()

st.subheader("1. 비교할 질환 선택")

if len(AVAILABLE_DISEASES) < 2:

    st.warning(
        "비교 가능한 치료 정보가 등록된 질환이 2개 이상 필요합니다."
    )

else:

    col1, col2 = st.columns(2)

    with col1:

        disease1 = st.selectbox(
            "첫 번째 질환",
            AVAILABLE_DISEASES,
            key="compare_disease1"
        )

    with col2:

        disease2 = st.selectbox(
            "두 번째 질환",
            AVAILABLE_DISEASES,
            index=1,
            key="compare_disease2"
        )


    # =====================================================
    # 질환 비교 실행
    # =====================================================

    if disease1 == disease2:

        st.warning(
            "서로 다른 두 질환을 선택해 주세요."
        )

    else:

        data1 = TREATMENT_DATA[disease1]
        data2 = TREATMENT_DATA[disease2]

        st.divider()

        # =================================================
        # 기본 정보 비교
        # =================================================

        st.subheader("2. 질환별 치료 정보")

        comparison_columns = st.columns(2)

        for index, disease_name in enumerate(
            [disease1, disease2]
        ):

            data = TREATMENT_DATA[disease_name]

            with comparison_columns[index]:

                st.markdown(f"### {disease_name}")

                st.write(data["summary"])

                st.markdown("**등록된 치료 방법**")

                for method in data["methods"]:

                    st.markdown(
                        f"- {method['name']} "
                        f"({method['category']})"
                    )


        # =================================================
        # 치료 방법 상세 비교
        # =================================================

        st.divider()

        st.subheader("3. 치료 방법 상세 정보")

        detail_columns = st.columns(2)

        for index, disease_name in enumerate(
            [disease1, disease2]
        ):

            data = TREATMENT_DATA[disease_name]

            with detail_columns[index]:

                st.markdown(f"### {disease_name}")

                for method in data["methods"]:

                    with st.expander(
                        method["name"],
                        expanded=True
                    ):

                        display_method(method)


        # =================================================
        # 치료 방법 비교표
        # =================================================

        st.divider()

        st.subheader("4. 두 질환의 치료 방법 비교표")

        comparison_rows = []

        for disease_name in [disease1, disease2]:

            data = TREATMENT_DATA[disease_name]

            for method in data["methods"]:

                comparison_rows.append({
                    "질환": disease_name,
                    "치료 방법": method["name"],
                    "치료 유형": method["category"],
                    "치료 목적": method["purpose"]
                })

        comparison_df = pd.DataFrame(
            comparison_rows
        )

        st.dataframe(
            comparison_df,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# 하단 안내
# =========================================================

st.divider()

st.caption(
    "VITRA | 의료정보 시각화 교육용 플랫폼 · "
    "본 자료는 진단이나 치료 결정을 대신하지 않습니다."
)
