import streamlit as st
import pandas as pd

from treatment_data import DISEASE_LIST, TREATMENT_DATA


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="두 질환 비교 | VITRA",
    page_icon="⚖️",
    layout="wide"
)


# =========================================================
# 치료 방법 상세 출력
# =========================================================

def display_method(method):

    st.markdown(f"#### {method['name']}")
    st.caption(method["category"])

    st.markdown("**치료 목적**")
    st.write(method["purpose"])

    st.markdown("**구체적인 치료 방법**")
    st.write(method["method"])

    st.markdown("**주요 특징**")
    for feature in method["features"]:
        st.markdown(f"- {feature}")

    st.markdown("**한계 및 고려할 점**")
    for limitation in method["limitations"]:
        st.markdown(f"- {limitation}")


def make_comparison_dataframe(disease_name, methods):

    rows = []

    for method in methods:
        rows.append({
            "질환": disease_name,
            "치료 방법": method["name"],
            "치료 유형": method["category"],
            "치료 목적": method["purpose"],
            "구체적인 방법": method["method"],
            "주요 특징": " / ".join(method["features"]),
            "한계 및 고려할 점": " / ".join(method["limitations"])
        })

    return pd.DataFrame(rows)


# =========================================================
# 데이터 검증
# =========================================================

missing_diseases = [
    disease for disease in DISEASE_LIST
    if disease not in TREATMENT_DATA
]

if missing_diseases:
    st.error(
        "치료 데이터가 등록되지 않은 질환이 있습니다: "
        + ", ".join(missing_diseases)
    )
    st.stop()


# =========================================================
# 페이지 제목
# =========================================================

st.title("⚖️ 두 질환 비교")

st.write(
    "두 질환의 치료 방법과 치료 목적을 비교하여 "
    "질환별 치료 접근 방식의 차이를 확인합니다."
)

st.info(
    "본 페이지는 의료정보 교육용 자료입니다. "
    "실제 치료 방법과 적용 여부는 환자의 상태, 질환의 중증도 및 "
    "전문 의료진의 판단에 따라 달라집니다."
)


# =========================================================
# 질환 선택
# =========================================================

st.divider()
st.subheader("1. 비교할 질환 선택")

col1, col2 = st.columns(2)

with col1:
    disease1 = st.selectbox(
        "첫 번째 질환",
        DISEASE_LIST,
        key="compare_disease1"
    )

with col2:
    disease2 = st.selectbox(
        "두 번째 질환",
        DISEASE_LIST,
        index=1,
        key="compare_disease2"
    )


# =========================================================
# 비교 결과
# =========================================================

if disease1 == disease2:
    st.warning("서로 다른 두 질환을 선택해 주세요.")

else:
    data1 = TREATMENT_DATA[disease1]
    data2 = TREATMENT_DATA[disease2]

    st.divider()
    st.subheader("2. 질환별 치료 정보")

    summary_columns = st.columns(2)

    for index, disease_name in enumerate([disease1, disease2]):
        data = TREATMENT_DATA[disease_name]

        with summary_columns[index]:
            st.markdown(f"### {disease_name}")
            st.write(data["summary"])
            st.markdown("**등록된 치료 방법**")

            for method in data["methods"]:
                st.markdown(
                    f"- {method['name']} ({method['category']})"
                )

    st.divider()
    st.subheader("3. 치료 방법 상세 비교")

    detail_columns = st.columns(2)

    for index, disease_name in enumerate([disease1, disease2]):
        methods = TREATMENT_DATA[disease_name]["methods"]

        with detail_columns[index]:
            st.markdown(f"### {disease_name}")

            for method_index, method in enumerate(methods):
                with st.expander(
                    method["name"],
                    expanded=(method_index == 0)
                ):
                    display_method(method)

    st.divider()
    st.subheader("4. 두 질환의 치료 방법 비교표")

    comparison_df = pd.concat(
        [
            make_comparison_dataframe(disease1, data1["methods"]),
            make_comparison_dataframe(disease2, data2["methods"])
        ],
        ignore_index=True
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
