
import streamlit as st


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="치료 방법 비교 | VITRA",
    page_icon="⚖️",
    layout="wide"
)


# =========================================================
# 치료 방법 비교 데이터
# 교육용 예시이며 실제 치료 결정 기준이 아님
# =========================================================

TREATMENT_DATA = {

    "장중첩증": {
        "summary": "장 일부가 인접한 장 안으로 말려 들어가는 질환입니다.",
        "methods": [
            {
                "name": "공기·조영제 정복술",
                "category": "비수술적 치료",
                "purpose": "장중첩 상태를 비수술적인 방법으로 해소하는 것",
                "method": "영상의학적 관찰 아래 공기 또는 조영제를 이용해 장중첩을 풀어 줍니다.",
                "features": [
                    "수술 없이 치료를 시도할 수 있습니다.",
                    "영상 장비를 이용하여 치료 과정을 확인합니다.",
                    "모든 환자에게 적용할 수 있는 것은 아닙니다."
                ],
                "limitations": [
                    "장 천공 등 합병증 위험을 고려해야 합니다.",
                    "정복에 실패하면 수술적 치료가 필요할 수 있습니다."
                ]
            },
            {
                "name": "수술적 정복",
                "category": "수술적 치료",
                "purpose": "장중첩을 직접 확인하고 해소하는 것",
                "method": "수술을 통해 중첩된 장을 확인하고 상태에 따라 정복합니다.",
                "features": [
                    "비수술적 정복이 실패한 경우 고려할 수 있습니다.",
                    "장 상태를 직접 확인할 수 있습니다.",
                    "장 손상이 있는 경우 추가적인 처치가 필요할 수 있습니다."
                ],
                "limitations": [
                    "마취와 수술에 따른 부담이 있습니다.",
                    "수술 후 회복과 관찰이 필요합니다."
                ]
            }
        ]
    },

    "충수염": {
        "summary": "충수에 염증이 발생하는 질환입니다.",
        "methods": [
            {
                "name": "항생제 치료",
                "category": "비수술적 치료",
                "purpose": "세균 감염과 염증을 조절하는 것",
                "method": "의료진의 판단에 따라 항생제를 투여하고 상태를 관찰합니다.",
                "features": [
                    "수술을 피할 수 있는 경우가 있습니다.",
                    "환자 상태를 지속적으로 관찰해야 합니다."
                ],
                "limitations": [
                    "모든 충수염에 적용할 수 있는 방법은 아닙니다.",
                    "재발하거나 치료에 실패할 가능성이 있습니다."
                ]
            },
            {
                "name": "충수절제술",
                "category": "수술적 치료",
                "purpose": "염증이 발생한 충수를 제거하는 것",
                "method": "복강경 또는 개복 수술을 통해 충수를 제거합니다.",
                "features": [
                    "염증이 발생한 충수를 직접 제거합니다.",
                    "복강경 수술을 시행할 수 있습니다."
                ],
                "limitations": [
                    "마취와 수술에 따른 부담이 있습니다.",
                    "수술 후 회복 과정이 필요합니다."
                ]
            }
        ]
    },

    "장폐색": {
        "summary": "장 내용물이 정상적으로 이동하지 못하는 상태입니다.",
        "methods": [
            {
                "name": "보존적 치료",
                "category": "비수술적 치료",
                "purpose": "장 기능과 전신 상태를 안정시키는 것",
                "method": "원인과 환자 상태에 따라 금식, 수액 공급, 감압 등의 치료를 시행합니다.",
                "features": [
                    "일부 장폐색에서 수술 없이 호전될 수 있습니다.",
                    "수분과 전해질 상태를 관리합니다."
                ],
                "limitations": [
                    "장 허혈이나 천공 등 위험 징후가 있으면 다른 처치가 필요합니다.",
                    "치료 중 상태를 면밀하게 관찰해야 합니다."
                ]
            },
            {
                "name": "수술적 치료",
                "category": "수술적 치료",
                "purpose": "폐색의 원인을 해결하는 것",
                "method": "폐색 원인과 장 상태에 따라 유착 박리, 장 절제 등의 수술을 고려합니다.",
                "features": [
                    "폐색의 원인을 직접 해결할 수 있습니다.",
                    "손상된 장을 확인하고 필요한 처치를 할 수 있습니다."
                ],
                "limitations": [
                    "수술 범위는 원인과 장 상태에 따라 달라집니다.",
                    "마취와 수술 후 회복이 필요합니다."
                ]
            }
        ]
    },

    "탈장": {
        "summary": "장기나 조직이 정상적인 위치에서 주변 조직의 약한 부위로 빠져나오는 질환입니다.",
        "methods": [
            {
                "name": "경과 관찰",
                "category": "비수술적 관리",
                "purpose": "탈장의 상태와 합병증 발생 여부를 확인하는 것",
                "method": "탈장의 종류와 환자의 연령 및 상태에 따라 의료진이 경과를 관찰합니다.",
                "features": [
                    "일부 소아 탈장은 자연적으로 닫힐 수 있습니다.",
                    "상태 변화와 합병증 여부를 관찰합니다."
                ],
                "limitations": [
                    "모든 탈장에 적용되는 방법은 아닙니다.",
                    "감돈이나 교액이 의심되면 신속한 평가가 필요합니다."
                ]
            },
            {
                "name": "탈장 교정술",
                "category": "수술적 치료",
                "purpose": "탈장 부위를 교정하는 것",
                "method": "탈장의 종류와 상태에 따라 수술적으로 탈장 부위를 교정합니다.",
                "features": [
                    "탈장 부위를 직접 교정합니다.",
                    "탈장의 종류에 따라 수술 방법이 달라집니다."
                ],
                "limitations": [
                    "마취와 수술에 따른 부담이 있습니다.",
                    "수술 후 회복과 관찰이 필요합니다."
                ]
            }
        ]
    }
}


# =========================================================
# 페이지 제목
# =========================================================

st.title("⚖️ 치료 방법 비교")

st.write(
    "질환별 비수술적 치료와 수술적 치료의 목적, "
    "방법 및 특징을 비교할 수 있습니다."
)

st.info(
    "이 페이지는 의료정보 교육을 위한 자료입니다. "
    "실제 치료 방법은 환자의 상태와 전문 의료진의 판단에 따라 달라집니다."
)


# =========================================================
# 질환 선택
# =========================================================

st.subheader("1. 비교할 질환 선택")

disease = st.selectbox(
    "질환을 선택하세요.",
    list(TREATMENT_DATA.keys())
)

data = TREATMENT_DATA[disease]

st.markdown(f"### 🩺 {disease}")

st.write(data["summary"])


# =========================================================
# 치료 방법 비교
# =========================================================

st.divider()

st.subheader("2. 치료 방법 비교")

method1, method2 = data["methods"]

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        f"### 🔵 {method1['category']}"
    )

    st.markdown(
        f"#### {method1['name']}"
    )

    st.markdown("**치료 목적**")

    st.write(method1["purpose"])

    st.markdown("**치료 방법**")

    st.write(method1["method"])

    st.markdown("**주요 특징**")

    for feature in method1["features"]:
        st.markdown(f"- {feature}")

    st.markdown("**고려할 점**")

    for limitation in method1["limitations"]:
        st.markdown(f"- {limitation}")


with col2:

    st.markdown(
        f"### 🟠 {method2['category']}"
    )

    st.markdown(
        f"#### {method2['name']}"
    )

    st.markdown("**치료 목적**")

    st.write(method2["purpose"])

    st.markdown("**치료 방법**")

    st.write(method2["method"])

    st.markdown("**주요 특징**")

    for feature in method2["features"]:
        st.markdown(f"- {feature}")

    st.markdown("**고려할 점**")

    for limitation in method2["limitations"]:
        st.markdown(f"- {limitation}")


# =========================================================
# 비교 요약
# =========================================================

st.divider()

st.subheader("3. 핵심 비교")

comparison = {
    "비교 항목": [
        "치료 목적",
        "치료 방식",
        "침습성",
        "주요 고려사항"
    ],
    method1["name"]: [
        method1["purpose"],
        method1["method"],
        "비수술적 접근",
        ", ".join(method1["limitations"])
    ],
    method2["name"]: [
        method2["purpose"],
        method2["method"],
        "수술적 접근",
        ", ".join(method2["limitations"])
    ]
}

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# 치료 방법 상세 설명
# =========================================================

st.divider()

st.subheader("4. 치료 방법 자세히 살펴보기")

selected_method = st.selectbox(
    "자세히 알아볼 치료 방법을 선택하세요.",
    [method1["name"], method2["name"]]
)

selected_data = next(
    method for method in data["methods"]
    if method["name"] == selected_method
)

st.markdown(f"### {selected_data['name']}")

st.write(selected_data["method"])

with st.expander("치료의 주요 특징"):
    for feature in selected_data["features"]:
        st.write(f"• {feature}")

with st.expander("치료 시 고려할 점"):
    for limitation in selected_data["limitations"]:
        st.write(f"• {limitation}")


# =========================================================
# 하단 안내
# =========================================================

st.divider()

st.caption(
    "VITRA | 의료정보 시각화 교육용 플랫폼 · "
    "본 자료는 진단이나 치료 결정을 대신하지 않습니다."
)

