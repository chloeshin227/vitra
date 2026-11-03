
import streamlit as st
import pandas as pd


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="치료 방법 비교 | VITRA",
    page_icon="⚖️",
    layout="wide"
)


# =========================================================
# 질환 목록: main.py의 25개 질환과 동일하게 관리
# =========================================================

DISEASE_LIST = [
    "장중첩증",
    "충수염",
    "장폐색",
    "장회전이상",
    "탈장",
    "담낭염",
    "복막염",
    "담석증",
    "췌장염",
    "장천공",
    "비후성 유문협착증",
    "히르슈스프룽병",
    "메켈게실",
    "괴사성 장염",
    "담도폐쇄증",
    "총담관낭종",
    "선천성 횡격막 탈장",
    "복벽갈림증",
    "배꼽류",
    "항문직장기형",
    "선천성 식도폐쇄증",
    "잠복고환",
    "요도하열",
    "고환 염전",
    "난소 염전"
]


# =========================================================
# 치료 방법 비교 데이터
# 상세 내용이 확인된 질환만 등록
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
                    "환자의 상태에 따라 적용 여부가 달라집니다."
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
                    "일부 환자에서 수술 없이 치료를 시도할 수 있습니다.",
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
                    "일부 소아 배꼽탈장은 자연적으로 닫힐 수 있습니다.",
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
    "소아외과 관련 질환의 치료 방법을 비교하고 "
    "치료 목적과 특징을 살펴볼 수 있습니다."
)

st.info(
    "본 페이지는 의료정보 교육용 자료입니다. "
    "실제 치료 방법과 적용 여부는 환자의 상태 및 "
    "전문 의료진의 판단에 따라 달라집니다."
)


# =========================================================
# 탭 구성
# =========================================================

tab1, tab2 = st.tabs([
    "질환별 치료 비교",
    "두 질환 비교"
])


# =========================================================
# 탭 1: 질환별 치료 비교
# =========================================================

with tab1:

    st.subheader("1. 질환 선택")

    disease = st.selectbox(
        "비교할 질환을 선택하세요.",
        DISEASE_LIST,
        key="single_disease"
    )

    st.markdown(f"### 🩺 {disease}")

    if disease not in TREATMENT_DATA:

        st.warning(
            "현재 이 질환의 상세 치료 비교 자료는 "
            "아직 등록되지 않았습니다."
        )

        st.write(
            "해당 질환의 치료 방법, 적용 조건 및 "
            "주의사항을 의학적 근거에 따라 검증한 후 "
            "비교 자료에 추가할 예정입니다."
        )

        st.caption(
            "질환 선택과 데이터베이스 등록은 완료되었으며, "
            "상세 치료 비교 정보는 준비 중입니다."
        )

    else:

        data = TREATMENT_DATA[disease]

        st.write(data["summary"])

        st.divider()

        st.subheader("2. 치료 방법 비교")

        methods = data["methods"]

        columns = st.columns(
            min(len(methods), 2)
        )

        for index, method in enumerate(methods):

            with columns[index % 2]:

                st.markdown(
                    f"### {method['category']}"
                )

                st.markdown(
                    f"#### {method['name']}"
                )

                st.markdown("**치료 목적**")
                st.write(method["purpose"])

                st.markdown("**치료 방법**")
                st.write(method["method"])

                st.markdown("**주요 특징**")

                for feature in method["features"]:
                    st.markdown(f"- {feature}")

                st.markdown("**고려할 점**")

                for limitation in method["limitations"]:
                    st.markdown(f"- {limitation}")

        st.divider()

        st.subheader("3. 핵심 비교표")

        comparison_rows = []

        for method in methods:

            comparison_rows.append({
                "치료 방법": method["name"],
                "치료 유형": method["category"],
                "치료 목적": method["purpose"],
                "주요 특징": " / ".join(method["features"]),
                "고려할 점": " / ".join(method["limitations"])
            })

        st.dataframe(
            pd.DataFrame(comparison_rows),
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("4. 치료 방법 상세 설명")

        selected_method = st.selectbox(
            "자세히 알아볼 치료 방법을 선택하세요.",
            [method["name"] for method in methods],
            key="detail_method"
        )

        selected_data = next(
            method for method in methods
            if method["name"] == selected_method
        )

        st.markdown(
            f"### {selected_data['name']}"
        )

        st.write(selected_data["method"])

        with st.expander("주요 특징"):
            for feature in selected_data["features"]:
                st.write(f"• {feature}")

        with st.expander("치료 시 고려할 점"):
            for limitation in selected_data["limitations"]:
                st.write(f"• {limitation}")


# =========================================================
# 탭 2: 두 질환 비교
# =========================================================

with tab2:

    st.subheader("두 질환 비교")

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

    if disease1 == disease2:

        st.warning("서로 다른 두 질환을 선택해 주세요.")

    else:

        st.markdown("### 비교 결과")

        comparison_data = []

        for disease_name in [disease1, disease2]:

            if disease_name in TREATMENT_DATA:

                disease_info = TREATMENT_DATA[disease_name]

                treatment_names = ", ".join(
                    method["name"]
                    for method in disease_info["methods"]
                )

                categories = ", ".join(
                    method["category"]
                    for method in disease_info["methods"]
                )

                comparison_data.append({
                    "비교 항목": disease_name,
                    "질환 설명": disease_info["summary"],
                    "등록된 치료 방법": treatment_names,
                    "치료 유형": categories,
                    "자료 상태": "상세 정보 등록"
                })

            else:

                comparison_data.append({
                    "비교 항목": disease_name,
                    "질환 설명": "상세 비교 자료 준비 중",
                    "등록된 치료 방법": "자료 준비 중",
                    "치료 유형": "자료 준비 중",
                    "자료 상태": "상세 정보 미등록"
                })

        st.dataframe(
            pd.DataFrame(comparison_data),
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "두 질환의 치료 방법을 비교하려면 "
            "각 질환의 상세 치료 데이터가 등록되어 있어야 합니다."
        )


# =========================================================
# 하단 안내
# =========================================================

st.divider()

st.caption(
    "VITRA | 의료정보 시각화 교육용 플랫폼 · "
    "본 자료는 진단이나 치료 결정을 대신하지 않습니다."
)
