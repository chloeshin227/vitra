
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
        "장회전이상": {
        "summary": "장회전이상은 태아 발달 과정에서 장이 정상적인 위치와 방향으로 회전하지 못한 선천성 질환이다. 장간막이 좁아지면 중장 염전이 발생할 수 있어 응급 수술이 필요할 수 있다.",
        "methods": [
            {
                "name": "Ladd 수술",
                "category": "수술적 치료",
                "purpose": "비정상적인 장의 위치로 인해 발생하는 장폐색과 중장 염전의 위험을 줄인다.",
                "method": "염전이 발생한 경우 장을 풀어주고, 십이지장을 압박하는 Ladd 띠를 절개한다. 장간막 기저부를 넓혀 염전 위험을 줄인 뒤 소장과 대장을 비회전 상태에 가깝게 재배치한다.",
                "features": "장회전이상에 대한 대표적인 수술 방법이다. 개복 또는 복강경으로 시행할 수 있으며, 중장 염전이 동반된 경우 응급 수술이 필요하다.",
                "limitations": "수술 후에도 장 유착이나 장폐색 등의 합병증이 발생할 수 있다. 무증상으로 우연히 발견된 경우에는 수술의 이득과 위험을 개별적으로 평가해야 한다."
            },
            {
                "name": "선별적 경과 관찰",
                "category": "보존적 관리",
                "purpose": "무증상 환자 중 수술의 위험이 이득보다 클 수 있는 경우 불필요한 수술을 피한다.",
                "method": "증상과 해부학적 형태, 동반 질환 등을 종합적으로 평가하고 전문 의료진의 판단에 따라 정기적인 임상 추적 관찰을 시행한다.",
                "features": "일부 무증상 환자에서 고려할 수 있는 접근이다. 가족과 보호자에게 응급 증상에 대한 교육과 지속적인 추적 관찰이 중요하다.",
                "limitations": "중장 염전의 위험을 완전히 제거하지 못한다. 무증상 장회전이상에 대한 최적의 관리 방법은 아직 충분한 근거가 확립되지 않았다."
            }
        ],
        "sources": [
            "https://pubmed.ncbi.nlm.nih.gov/26205079/",
            "https://www.merckmanuals.com/professional/pediatrics/congenital-gastrointestinal-anomalies/malrotation-of-the-bowel"
        ]
    },

    "담낭염": {
        "summary": "담낭염은 담낭에 염증이 발생한 질환으로, 담석이 담낭관을 막아 발생하는 경우가 흔하다. 소아에서는 원인과 중증도에 따라 항균 치료와 수술적 치료를 결정한다.",
        "methods": [
            {
                "name": "항균 치료 및 보존적 치료",
                "category": "약물·보존적 치료",
                "purpose": "감염과 염증을 조절하고 환자의 전신 상태를 안정시킨다.",
                "method": "입원 상태에서 수액 공급, 통증 조절 및 필요한 경우 항균 치료를 시행한다. 영상 검사와 혈액 검사 등을 통해 염증 정도와 담도 폐쇄 여부를 평가한다.",
                "features": "환자의 상태를 안정시키는 초기 치료로 활용된다. 항균제의 선택은 감염의 중증도와 원인, 연령 및 지역별 항균제 내성 등을 고려한다.",
                "limitations": "담석이나 담낭관 폐쇄 등 근본적인 원인이 남아 있으면 재발하거나 악화될 수 있다. 항균 치료만으로 모든 환자의 원인을 해결할 수 있는 것은 아니다."
            },
            {
                "name": "복강경 담낭절제술",
                "category": "수술적 치료",
                "purpose": "염증이 발생한 담낭을 제거하여 원인을 해결하고 재발 가능성을 줄인다.",
                "method": "전신마취 후 복부에 작은 절개를 내고 복강경 기구를 이용하여 담낭을 분리한 뒤 제거한다.",
                "features": "증상이 있는 담석성 담낭 질환에서 주요 치료 방법으로 활용된다. 환자의 상태와 염증 정도에 따라 수술 시기를 결정한다.",
                "limitations": "담낭 주변의 심한 염증이나 유착은 수술을 어렵게 만들 수 있다. 담관 손상, 출혈, 감염 등의 수술 관련 합병증 가능성이 있다."
            }
        ],
        "sources": [
            "https://www.healthychildren.org/English/health-issues/conditions/abdominal/Pages/Gallbladder-Disease-in-Children.aspx",
            "https://choc.org/wp-content/uploads/2023/11/2023CholelithiasisCareGuidelineWithReferences.pdf",
            "https://www.who.int/publications/i/item/WHO-MHP-HPS-EML-2022.02"
        ]
    },

    "복막염": {
        "summary": "복막염은 복강 내부를 덮는 복막에 염증이 발생한 상태이다. 소아에서는 장 천공이나 충수염 등 복강 내 감염이 원인이 되는 이차성 복막염이 중요하며, 감염의 원인과 범위에 따라 치료 방법이 달라진다.",
        "methods": [
            {
                "name": "항균 치료 및 집중적인 보존적 관리",
                "category": "약물·보존적 치료",
                "purpose": "복강 내 세균 감염을 억제하고 감염이 전신으로 확산되는 것을 방지한다.",
                "method": "환자의 상태를 평가하고 수액 공급과 전신 상태 관리를 시행한다. 이차성 복막염에서는 감염 원인과 예상되는 세균을 고려하여 적절한 항균 치료를 시행한다.",
                "features": "감염의 원인과 중증도에 따라 항균제의 종류와 치료 범위가 결정된다. 패혈증 등 전신 감염 징후가 있는 경우 신속한 치료가 중요하다.",
                "limitations": "장 천공이나 농양 등 감염의 원인이 남아 있다면 항균 치료만으로 충분하지 않을 수 있다."
            },
            {
                "name": "감염원 조절을 위한 수술 및 배액",
                "category": "수술적·중재적 치료",
                "purpose": "복강 내 감염의 근본 원인을 제거하고 고름이나 오염된 내용물을 배출한다.",
                "method": "감염의 원인에 따라 천공된 장을 복구하거나 손상된 부위를 절제하고, 복강 내 농양이 있는 경우 적절한 방법으로 배액한다.",
                "features": "이차성 복막염에서 감염원을 제거하는 과정은 치료의 핵심이다. 환자의 상태와 감염 위치에 따라 수술 또는 최소침습적 배액 방법을 선택할 수 있다.",
                "limitations": "감염의 범위와 환자의 전신 상태에 따라 수술의 위험이 달라진다. 감염이 완전히 조절되지 않으면 추가적인 시술이나 치료가 필요할 수 있다."
            }
        ],
        "sources": [
            "https://doi.org/10.1089/sur.2016.261",
            "https://doi.org/10.1086/649554"
        ]
    },

    "담석증": {
        "summary": "담석증은 담낭이나 담관에 담석이 형성되는 질환이다. 소아에서는 용혈성 질환, 선천성 질환, 약물 및 영양 상태 등 다양한 요인이 관련될 수 있다. 증상이 있는지, 담관 폐쇄나 담낭염 등의 합병증이 있는지에 따라 치료 방법을 결정한다.",
        "methods": [
            {
                "name": "경과 관찰 및 보존적 관리",
                "category": "보존적 치료",
                "purpose": "증상이 없고 합병증이 발생하지 않은 환자에서 불필요한 수술을 피하면서 상태를 확인한다.",
                "method": "증상과 초음파 검사 결과 등을 정기적으로 확인한다. 담석 형성에 영향을 줄 수 있는 기저 질환이나 위험 요인이 있다면 함께 관리한다.",
                "features": "무증상 담석증에서는 경과 관찰을 고려할 수 있다. 다만 용혈성 질환 등 동반 질환이 있는 경우에는 수술 여부를 별도로 평가해야 한다.",
                "limitations": "담석이 저절로 사라진다고 보장할 수 없으며, 추후 담도 폐쇄나 담낭염 등의 합병증이 발생할 가능성이 있다."
            },
            {
                "name": "복강경 담낭절제술",
                "category": "수술적 치료",
                "purpose": "증상을 일으키는 담석의 근원인 담낭을 제거하여 통증과 담석 관련 합병증의 재발을 줄인다.",
                "method": "전신마취 후 복강경을 이용하여 담낭을 분리하고 제거한다. 담관 결석이 의심되는 경우에는 추가적인 담도 평가를 시행할 수 있다.",
                "features": "증상이 반복되거나 담낭염 등 합병증이 동반된 소아에서 주요 치료 방법이다.",
                "limitations": "담관 결석이 남아 있는 경우 별도의 내시경적 치료가 필요할 수 있다. 담관 손상이나 출혈 등의 수술 관련 합병증 가능성이 있다."
            },
            {
                "name": "내시경적 역행성 담췌관 조영술(ERCP)",
                "category": "내시경적 치료",
                "purpose": "담관을 막고 있는 담석을 제거하여 담즙의 흐름을 회복한다.",
                "method": "내시경을 십이지장까지 삽입한 뒤 담관 입구를 통해 담관에 접근하고, 필요한 경우 담관 결석을 제거한다.",
                "features": "담낭 자체가 아닌 담관에 결석이 존재하는 경우 고려할 수 있는 치료 방법이다.",
                "limitations": "모든 담석증 환자에게 시행하는 치료가 아니다. 소아에서는 시술 가능 기관과 전문 인력이 제한될 수 있으며, 췌장염 등 시술 관련 합병증 가능성이 있다."
            }
        ],
        "sources": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8323576/",
            "https://health.ucdavis.edu/media-resources/pediatrics/documents/pdfs/clinical-guidelines/Gallstone-Disease-Peds-PICU.pdf",
            "https://www.healthychildren.org/English/health-issues/conditions/abdominal/Pages/Gallbladder-Disease-in-Children.aspx"
        ]
    },

    "췌장염": {
        "summary": "췌장염은 췌장에 염증이 발생하는 질환이다. 소아 급성 췌장염은 원인과 중증도가 다양하며, 초기에는 수액 공급과 통증 조절, 조기 영양 공급을 중심으로 치료한다. 담도 폐쇄나 국소 합병증이 있는 경우에는 추가적인 내시경적 또는 수술적 치료가 필요할 수 있다.",
        "methods": [
            {
                "name": "수액·통증 조절 및 영양 관리",
                "category": "보존적 치료",
                "purpose": "체액 부족을 교정하고 통증을 완화하며 췌장염으로 인한 전신 상태 악화를 예방한다.",
                "method": "환자의 상태에 맞춰 수액을 공급하고 통증을 조절한다. 상태가 허용되면 가능한 한 이른 시기에 경구 또는 경장 영양을 시작한다.",
                "features": "소아 급성 췌장염의 기본적인 치료 방법이다. 특별한 금기가 없다면 조기 영양 공급이 권장되며, 모든 환자에게 장기간 금식이나 지방 제한 식이를 적용하는 것은 적절하지 않다.",
                "limitations": "췌장염의 원인 자체를 제거하는 치료는 아니다. 중증 췌장염이나 장기 기능 장애, 국소 합병증이 발생한 경우에는 추가 치료가 필요하다."
            },
            {
                "name": "내시경적 역행성 담췌관 조영술(ERCP)",
                "category": "내시경적 치료",
                "purpose": "담관 결석이나 담도 폐쇄가 췌장염의 원인인 경우 담즙과 췌장액의 배출을 방해하는 요인을 해결한다.",
                "method": "내시경으로 십이지장에 접근하여 담관을 확인하고, 필요한 경우 담관 결석 제거 등의 시술을 시행한다.",
                "features": "담석성 췌장염에서 담관 결석이나 담관염, 지속적인 담도 폐쇄가 확인되는 등 특정 상황에 고려한다.",
                "limitations": "급성 췌장염 환자 모두에게 시행하는 표준 치료는 아니다. 소아에서는 전문적인 내시경 시설과 숙련된 의료진이 필요하다."
            },
            {
                "name": "합병증에 대한 중재적·수술적 치료",
                "category": "중재적·수술적 치료",
                "purpose": "췌장염으로 발생한 감염성 괴사, 농양, 가성낭종 등의 합병증을 치료한다.",
                "method": "합병증의 위치와 상태에 따라 영상 유도 배액, 내시경적 배액 또는 필요한 경우 수술적 치료를 고려한다.",
                "features": "일반적인 급성 췌장염의 초기 치료가 아니라 합병증이 발생한 일부 환자에서 전문 의료진의 판단에 따라 시행한다.",
                "limitations": "침습적 치료가 필요하지 않은 환자에게 일률적으로 적용하지 않는다. 치료 방법과 시기는 합병증의 종류와 환자의 상태에 따라 달라진다."
            }
        ],
        "sources": [
            "https://doi.org/10.1136/flgastro-2024-102788",
            "https://www.naspghan.org/files/Management_of_Acute_Pancreatitis_in_the_Pediatric.33.pdf",
            "https://doi.org/10.1016/j.pan.2025.04.020"
        ]
    },

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
