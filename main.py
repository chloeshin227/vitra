import streamlit as st
import plotly.graph_objects as go
from difflib import get_close_matches

# =========================================================
# 기본 설정
# =========================================================ㄹ

st.set_page_config(
    page_title="VITRA",
    page_icon="🩺",
    layout="wide"
)

# =========================================================
# 질환 데이터
# =========================================================

DISEASE_DATA = {
    "장중첩증": {
    "keywords": ["장중첩증", "장중첩"],
    "organ": "장",
    "body_part": "복부",
    "easy_explanation": "장 일부가 다른 장 부분 안으로 말려 들어가는 상태입니다.",
    "surgery_title": "장중첩증 치료 과정",
    "surgery_steps": [
        {
            "title": "검사",
            "description": "장중첩이 발생한 위치와 상태를 확인합니다.",
            "icon": "🔎"
        },
        {
            "title": "치료",
            "description": "환자 상태에 따라 적절한 치료를 시행합니다.",
            "icon": "🏥"
        }
    ],
    "organ_color": "#FF9800"
},
    "충수염": {
        "keywords": [
            "충수염",
            "충수돌기염",
            "충수 돌기염",
            "급성 충수염",
            "급성충수염",
            "맹장염",
            "충수"
        ],
        "organ": "충수",
        "body_part": "오른쪽 아랫배",
        "easy_explanation": (
            "충수염은 대장과 연결된 작은 관 모양의 충수에 "
            "염증이 생긴 상태입니다."
        ),
        "surgery_title": "복강경 충수절제술",
        "surgery_steps": [
            {
                "title": "마취",
                "description": "수술 중 통증을 느끼지 않도록 마취를 시행합니다.",
                "icon": "💤"
            },
            {
                "title": "복부 접근",
                "description": "복부에 작은 절개를 만들어 카메라와 수술 기구를 넣습니다.",
                "icon": "🔎"
            },
            {
                "title": "충수 확인",
                "description": "카메라를 이용해 염증이 생긴 충수의 위치와 상태를 확인합니다.",
                "icon": "🩺"
            },
            {
                "title": "충수 제거",
                "description": "염증이 있는 충수를 분리하여 제거합니다.",
                "icon": "✂️"
            },
            {
                "title": "마무리",
                "description": "수술 부위를 확인하고 작은 절개 부위를 봉합합니다.",
                "icon": "🩹"
            }
        ],
        "organ_color": "#FF5252"
    },

    "장폐색": {
        "keywords": [
            "장폐색",
            "장 막힘",
            "장막힘",
            "소장폐색"
        ],
        "organ": "장",
        "body_part": "복부",
        "easy_explanation": (
            "장폐색은 장의 내용물이 정상적으로 이동하기 어려워진 상태입니다."
        ),
        "surgery_title": "장폐색 치료 과정",
        "surgery_steps": [
            {
                "title": "상태 확인",
                "description": "검사를 통해 막혀 있는 장의 위치와 상태를 확인합니다.",
                "icon": "🔎"
            },
            {
                "title": "복부 접근",
                "description": "필요한 경우 수술을 위해 복부에 접근합니다.",
                "icon": "🩺"
            },
            {
                "title": "폐색 확인",
                "description": "막힌 부분과 그 원인을 확인합니다.",
                "icon": "🔍"
            },
            {
                "title": "문제 해결",
                "description": "막힘의 원인과 환자의 상태에 맞는 치료를 시행합니다.",
                "icon": "🛠️"
            },
            {
                "title": "회복 확인",
                "description": "장의 상태와 움직임을 확인하고 치료를 마무리합니다.",
                "icon": "🩹"
            }
        ],
        "organ_color": "#FF9800"
    },

    "장중첩증": {
        "keywords": [
            "장중첩증",
            "장 중첩",
            "장중첩"
        ],
        "organ": "장",
        "body_part": "복부",
        "easy_explanation": (
            "장중첩증은 장의 한 부분이 다른 부분의 안쪽으로 말려 들어가는 상태입니다."
        ),
        "surgery_title": "장중첩증 치료 과정",
        "surgery_steps": [
            {
                "title": "검사",
                "description": "장중첩이 발생한 위치와 상태를 확인합니다.",
                "icon": "🔎"
            },
            {
                "title": "정복 시도",
                "description": "환자의 상태에 따라 먼저 비수술적 치료를 시도할 수 있습니다.",
                "icon": "🩺"
            },
            {
                "title": "장 확인",
                "description": "필요한 경우 수술을 통해 장의 상태를 확인합니다.",
                "icon": "🔍"
            },
            {
                "title": "위치 복원",
                "description": "말려 들어간 장을 정상적인 위치로 되돌립니다.",
                "icon": "↩️"
            },
            {
                "title": "상태 확인",
                "description": "장 손상 여부를 확인하고 치료를 마무리합니다.",
                "icon": "🩹"
            }
        ],
        "organ_color": "#FF9800"
    },

    "장회전이상": {
        "keywords": [
            "장회전이상",
            "장 회전 이상",
            "장 회전 이상증"
        ],
        "organ": "장",
        "body_part": "복부",
        "easy_explanation": (
            "장회전이상은 성장 과정에서 장이 정상적인 위치와 방향으로 "
            "자리 잡지 못한 상태입니다."
        ),
        "surgery_title": "장회전이상 치료 과정",
        "surgery_steps": [
            {
                "title": "영상검사",
                "description": "장의 위치와 상태를 검사합니다.",
                "icon": "🔎"
            },
            {
                "title": "복부 확인",
                "description": "수술을 통해 장과 주변 구조의 상태를 확인합니다.",
                "icon": "🩺"
            },
            {
                "title": "꼬임 확인",
                "description": "장에 비정상적인 꼬임이 있는지 확인합니다.",
                "icon": "🔍"
            },
            {
                "title": "위치 정리",
                "description": "필요한 경우 꼬임을 풀고 장의 위치를 정리합니다.",
                "icon": "↩️"
            },
            {
                "title": "마무리",
                "description": "장에 손상이 있는지 확인하고 수술을 마무리합니다.",
                "icon": "🩹"
            }
        ],
        "organ_color": "#FF9800"
    },

    "탈장": {
        "keywords": [
            "탈장",
            "복벽 탈장"
        ],
        "organ": "복벽",
        "body_part": "복부",
        "easy_explanation": (
            "탈장은 복벽의 약한 부분을 통해 장기나 조직이 "
            "원래 위치에서 바깥쪽으로 밀려 나오는 상태입니다."
        ),
        "surgery_title": "탈장 수술 과정",
        "surgery_steps": [
            {
                "title": "탈장 확인",
                "description": "탈장이 발생한 위치와 상태를 확인합니다.",
                "icon": "🔎"
            },
            {
                "title": "접근",
                "description": "탈장이 있는 부위에 접근합니다.",
                "icon": "🩺"
            },
            {
                "title": "조직 복원",
                "description": "밀려 나온 조직을 원래 위치로 돌려놓습니다.",
                "icon": "↩️"
            },
            {
                "title": "복벽 보강",
                "description": "약해진 복벽을 봉합하여 안정시킵니다.",
                "icon": "🛠️"
            },
            {
                "title": "마무리",
                "description": "수술 부위를 확인하고 절개 부위를 봉합합니다.",
                "icon": "🩹"
            }
        ],
        "organ_color": "#9C27B0"
    },

    "담낭염": {
        "keywords": [
            "담낭염",
            "담낭"
        ],
        "organ": "담낭",
        "body_part": "오른쪽 윗배",
        "easy_explanation": (
            "담낭염은 간 아래쪽에 위치한 담낭에 염증이 생긴 상태입니다."
        ),
        "surgery_title": "담낭 수술 과정",
        "surgery_steps": [
            {
                "title": "검사",
                "description": "영상검사 등을 통해 담낭의 상태를 확인합니다.",
                "icon": "🔎"
            },
            {
                "title": "접근",
                "description": "복부에 수술 기구를 넣어 담낭에 접근합니다.",
                "icon": "🩺"
            },
            {
                "title": "담낭 확인",
                "description": "담낭과 주변 구조의 상태를 확인합니다.",
                "icon": "🔍"
            },
            {
                "title": "치료",
                "description": "환자의 상태에 따라 필요한 치료를 시행합니다.",
                "icon": "🛠️"
            },
            {
                "title": "마무리",
                "description": "수술 부위를 확인하고 마무리합니다.",
                "icon": "🩹"
            }
        ],
        "organ_color": "#FBC02D"
    }
}


# =========================================================
# 추가 질환 데이터
# DISEASE_DATA 선언 직후, ORGAN_POSITION 선언 전에 배치
# =========================================================

EXTRA_DISEASE_DATA = {
    "복막염": {
        "keywords": ["복막염", "복막의 염증", "급성 복막염"],
        "organ": "장",
        "body_part": "복부",
        "easy_explanation": (
            "복막염은 복강 안쪽을 덮는 복막에 염증이 생긴 상태입니다. "
            "원인에 따라 긴급한 평가와 치료가 필요할 수 있습니다."
        ),
        "surgery_title": "복막염 평가 및 치료 과정",
        "surgery_steps": [
            {"title": "응급 평가", "description": "증상과 활력징후를 확인합니다.", "icon": "🩺"},
            {"title": "검사", "description": "혈액검사와 영상검사 등으로 원인을 평가합니다.", "icon": "🔎"},
            {"title": "원인 확인", "description": "장 천공 등 원인이 있는지 의료진이 확인합니다.", "icon": "🔍"},
            {"title": "치료", "description": "원인과 환자 상태에 따라 약물치료나 수술 등을 결정합니다.", "icon": "🏥"},
            {"title": "경과 관찰", "description": "염증과 전신 상태의 변화를 관찰합니다.", "icon": "🩹"},
        ],
        "organ_color": "#FF7043",
    },

    "담석증": {
        "keywords": ["담석증", "담석", "담낭 결석", "담낭결석"],
        "organ": "담낭",
        "body_part": "오른쪽 윗배",
        "easy_explanation": (
            "담석증은 담낭이나 담도에 돌처럼 굳은 물질이 생기는 상태입니다. "
            "증상과 결석의 위치에 따라 관리 방법이 달라집니다."
        ),
        "surgery_title": "담석증 평가 및 치료 과정",
        "surgery_steps": [
            {"title": "증상 확인", "description": "복통과 동반 증상을 확인합니다.", "icon": "🩺"},
            {"title": "영상검사", "description": "초음파 등으로 결석의 위치를 확인합니다.", "icon": "🔎"},
            {"title": "상태 평가", "description": "담낭과 담도의 염증 여부 등을 평가합니다.", "icon": "🔍"},
            {"title": "치료 결정", "description": "환자의 상태에 따라 관찰이나 시술·수술 등을 고려합니다.", "icon": "🏥"},
            {"title": "경과 관찰", "description": "증상과 치료 후 상태를 확인합니다.", "icon": "🩹"},
        ],
        "organ_color": "#FBC02D",
    },

    "췌장염": {
        "keywords": ["췌장염", "급성 췌장염", "급성췌장염"],
        "organ": "췌장",
        "body_part": "상복부",
        "easy_explanation": (
            "췌장염은 소화효소와 호르몬을 만드는 췌장에 염증이 생긴 상태입니다. "
            "원인과 중증도에 따라 치료가 달라집니다."
        ),
        "surgery_title": "췌장염 평가 및 치료 과정",
        "surgery_steps": [
            {"title": "증상 확인", "description": "복통과 구토 등 동반 증상을 확인합니다.", "icon": "🩺"},
            {"title": "검사", "description": "혈액검사와 필요시 영상검사를 시행합니다.", "icon": "🔎"},
            {"title": "원인 평가", "description": "담석이나 약물 등 가능한 원인을 평가합니다.", "icon": "🔍"},
            {"title": "치료", "description": "수액과 통증 조절 등 상태에 맞는 치료를 시행합니다.", "icon": "🏥"},
            {"title": "경과 관찰", "description": "증상과 합병증 발생 여부를 확인합니다.", "icon": "🩹"},
        ],
        "organ_color": "#7E57C2",
    },

    "장천공": {
        "keywords": ["장천공", "장 천공", "소장 천공", "대장 천공"],
        "organ": "장",
        "body_part": "복부",
        "easy_explanation": (
            "장천공은 장벽에 구멍이 생긴 상태입니다. 복강 내 감염을 일으킬 수 있어 "
            "신속한 의료 평가가 필요합니다."
        ),
        "surgery_title": "장천공 평가 및 치료 과정",
        "surgery_steps": [
            {"title": "응급 평가", "description": "환자의 전신 상태와 복부 증상을 확인합니다.", "icon": "🩺"},
            {"title": "검사", "description": "필요한 혈액검사와 영상검사를 시행합니다.", "icon": "🔎"},
            {"title": "천공 확인", "description": "천공 위치와 주변 조직의 상태를 평가합니다.", "icon": "🔍"},
            {"title": "치료 결정", "description": "환자 상태에 따라 응급 처치와 수술 여부를 결정합니다.", "icon": "🏥"},
            {"title": "회복 관찰", "description": "감염과 장 기능의 회복 상태를 관찰합니다.", "icon": "🩹"},
        ],
        "organ_color": "#FF5252",
    },
}

# 기존 질환 데이터에 추가
DISEASE_DATA.update(EXTRA_DISEASE_DATA)

# =========================================================
# 추가 소아외과 질환 데이터 15종
# 기존 DISEASE_DATA에 추가
# =========================================================

ADDITIONAL_DISEASE_DATA = {

    # -----------------------------------------------------
    # 위·장 질환
    # -----------------------------------------------------

    "비후성 유문협착증": {
        "keywords": ["유문협착", "비후성 유문협착", "영아 구토"],
        "organ": "위",
        "body_part": "상복부",
        "easy_explanation": "위와 십이지장을 연결하는 유문 근육이 두꺼워져 음식물이 위에서 장으로 이동하기 어려워지는 영아기 질환입니다.",
        "surgery_title": "유문근절개술",
        "organ_color": "#E67E22",
        "surgery_steps": [
            {"icon": "🩺", "title": "진단 및 평가", "description": "복부 초음파 등을 통해 유문 근육의 비후 여부를 확인하고 탈수와 전해질 이상을 평가합니다."},
            {"icon": "💧", "title": "수분 및 전해질 교정", "description": "수술 전 수액 치료 등을 통해 탈수와 전해질 이상을 교정합니다."},
            {"icon": "🔬", "title": "유문근절개술", "description": "두꺼워진 유문 근육을 절개하여 위 내용물이 십이지장으로 이동할 수 있도록 합니다."},
            {"icon": "🩹", "title": "수술 후 회복", "description": "수유를 단계적으로 재개하고 구토와 수분 상태 등을 관찰합니다."}
        ]
    },

    "히르슈스프룽병": {
        "keywords": ["히르슈스프룽", "선천성 거대결장", "장신경절 세포 결핍"],
        "organ": "대장",
        "body_part": "하복부",
        "easy_explanation": "장의 일부에 신경절 세포가 선천적으로 없어 해당 부위가 정상적으로 이완되지 못하고 장 내용물의 이동이 어려워지는 질환입니다.",
        "surgery_title": "풀스루 수술",
        "organ_color": "#27AE60",
        "surgery_steps": [
            {"icon": "🩺", "title": "진단", "description": "직장 흡인 생검 등으로 장의 신경절 세포 유무를 확인합니다."},
            {"icon": "🔍", "title": "병변 범위 확인", "description": "영상검사와 조직검사 등을 통해 신경절 세포가 없는 장의 범위를 평가합니다."},
            {"icon": "🔬", "title": "풀스루 수술", "description": "신경절 세포가 없는 장을 제거하거나 우회하고 정상적인 신경절 세포가 있는 장을 항문 쪽에 연결합니다."},
            {"icon": "🩹", "title": "수술 후 관리", "description": "배변 기능, 장염 발생 여부와 영양 상태 등을 관찰합니다."}
        ]
    },

    "메켈게실": {
        "keywords": ["메켈게실", "메켈", "소장 게실"],
        "organ": "소장",
        "body_part": "하복부",
        "easy_explanation": "태아 발달 과정에서 남은 구조물로 인해 소장에 생기는 선천성 게실입니다. 출혈이나 염증 등의 합병증이 발생할 수 있습니다.",
        "surgery_title": "메켈게실 절제술",
        "organ_color": "#16A085",
        "surgery_steps": [
            {"icon": "🩺", "title": "증상 및 검사 평가", "description": "출혈, 복통, 장폐색 등의 증상을 확인하고 필요한 검사를 시행합니다."},
            {"icon": "🔍", "title": "병변 확인", "description": "영상검사와 임상 소견 등을 통해 메켈게실 및 합병증 여부를 평가합니다."},
            {"icon": "🔬", "title": "수술적 치료", "description": "증상과 장 상태에 따라 게실 절제 또는 인접 소장 절제를 고려합니다."},
            {"icon": "🩹", "title": "회복 및 관찰", "description": "장 기능과 수술 부위 회복 상태를 관찰합니다."}
        ]
    },

    "괴사성 장염": {
        "keywords": ["괴사성 장염", "신생아 장염", "NEC"],
        "organ": "소장 및 대장",
        "body_part": "복부",
        "easy_explanation": "주로 미숙아에게 발생하며 장에 염증과 손상이 생기고 심한 경우 장 조직이 괴사할 수 있는 질환입니다.",
        "surgery_title": "괴사성 장염 치료 및 수술",
        "organ_color": "#C0392B",
        "surgery_steps": [
            {"icon": "🩺", "title": "상태 평가", "description": "복부 팽만, 수유 불내성 등의 증상과 영상검사 결과를 평가합니다."},
            {"icon": "💧", "title": "초기 집중 치료", "description": "장 휴식, 수액 공급, 항생제 투여와 전신 상태 관찰 등을 시행합니다."},
            {"icon": "🔬", "title": "수술적 치료 고려", "description": "장 천공이나 진행된 장 괴사 등 수술이 필요한 상황에서는 손상된 장에 대한 수술을 고려합니다."},
            {"icon": "🩹", "title": "회복 및 영양 관리", "description": "장 기능과 영양 상태를 확인하고 필요한 경우 장기적인 영양 관리를 시행합니다."}
        ]
    },

    # -----------------------------------------------------
    # 간·담도 질환
    # -----------------------------------------------------

    "담도폐쇄증": {
        "keywords": ["담도폐쇄증", "담관폐쇄", "신생아 황달"],
        "organ": "간 및 담도",
        "body_part": "우상복부",
        "easy_explanation": "신생아 시기에 담도가 막히거나 정상적으로 형성되지 않아 담즙이 장으로 배출되지 못하는 질환입니다.",
        "surgery_title": "카사이 수술",
        "organ_color": "#F1C40F",
        "surgery_steps": [
            {"icon": "🩺", "title": "황달 및 간 기능 평가", "description": "황달의 지속 여부와 간 기능, 담즙 정체 관련 검사 결과를 평가합니다."},
            {"icon": "🔍", "title": "진단 검사", "description": "혈액검사와 영상검사 등을 시행하고 필요한 경우 간 조직검사 및 수술적 평가를 진행합니다."},
            {"icon": "🔬", "title": "카사이 수술", "description": "간문부의 담도 잔여 조직을 제거하고 장을 연결하여 담즙이 배출될 수 있도록 합니다."},
            {"icon": "🩹", "title": "수술 후 관리", "description": "황달 변화, 간 기능, 담관염과 영양 상태 등을 지속적으로 관찰합니다."}
        ]
    },

    "총담관낭종": {
        "keywords": ["총담관낭종", "담관낭종", "담도 낭종"],
        "organ": "담도",
        "body_part": "우상복부",
        "easy_explanation": "간에서 십이지장으로 담즙을 운반하는 담관이 비정상적으로 확장되는 선천성 질환입니다.",
        "surgery_title": "담관낭종 절제 및 재건술",
        "organ_color": "#F39C12",
        "surgery_steps": [
            {"icon": "🩺", "title": "진단 및 평가", "description": "복통, 황달 등의 증상과 초음파 및 MRI 등의 영상검사로 담관 상태를 평가합니다."},
            {"icon": "🔍", "title": "담도 구조 확인", "description": "낭종의 위치와 범위, 췌담관 합류 구조 등을 확인합니다."},
            {"icon": "🔬", "title": "낭종 절제 및 재건", "description": "담관낭종을 절제하고 장을 이용해 담즙 배출 경로를 재건하는 수술을 시행할 수 있습니다."},
            {"icon": "🩹", "title": "회복 및 추적 관찰", "description": "담즙 배출 상태와 간 기능, 수술 후 합병증 여부를 확인합니다."}
        ]
    },

    # -----------------------------------------------------
    # 선천성 기형
    # -----------------------------------------------------

    "선천성 횡격막 탈장": {
        "keywords": ["횡격막 탈장", "선천성 횡격막 탈장", "CDH"],
        "organ": "횡격막 및 폐",
        "body_part": "흉부와 복부 경계",
        "easy_explanation": "횡격막에 결손이 있어 복부 장기가 흉강으로 이동하고 폐 발달에 영향을 줄 수 있는 선천성 질환입니다.",
        "surgery_title": "횡격막 결손 교정술",
        "organ_color": "#8E44AD",
        "surgery_steps": [
            {"icon": "🩺", "title": "출생 전후 평가", "description": "폐 발달 상태와 호흡 기능, 복부 장기의 위치를 평가합니다."},
            {"icon": "🫁", "title": "호흡 및 순환 안정화", "description": "수술 전 호흡과 순환 상태를 안정시키는 집중 치료를 시행합니다."},
            {"icon": "🔬", "title": "횡격막 결손 교정", "description": "환자의 상태가 안정되면 탈출한 장기를 복강으로 되돌리고 횡격막 결손을 교정합니다."},
            {"icon": "🩹", "title": "수술 후 집중 관리", "description": "호흡 기능, 폐 발달과 순환 상태 등을 지속적으로 관찰합니다."}
        ]
    },

    "복벽갈림증": {
        "keywords": ["복벽갈림증", "위벽파열", "위벽갈림증", "Gastroschisis"],
        "organ": "복벽 및 장",
        "body_part": "배꼽 주변",
        "easy_explanation": "선천적으로 복벽에 결손이 생겨 장이 복강 밖으로 노출되는 질환입니다.",
        "surgery_title": "복벽 결손 교정술",
        "organ_color": "#D35400",
        "surgery_steps": [
            {"icon": "🩺", "title": "출생 직후 평가", "description": "노출된 장의 상태와 체온, 수분 손실 및 전신 상태를 평가합니다."},
            {"icon": "🛡️", "title": "장 보호 및 안정화", "description": "노출된 장을 보호하고 체온과 수분 균형을 유지합니다."},
            {"icon": "🔬", "title": "복벽 결손 교정", "description": "장 상태와 복강 용적에 따라 단계적 또는 일차적 복벽 교정을 시행합니다."},
            {"icon": "🩹", "title": "장 기능 회복 관리", "description": "장 기능과 영양 공급 상태를 관찰하며 회복을 돕습니다."}
        ]
    },

    "배꼽류": {
        "keywords": ["배꼽류", "제대류", "제대탈장", "Omphalocele"],
        "organ": "복벽 및 복부 장기",
        "body_part": "배꼽",
        "easy_explanation": "복부 장기의 일부가 배꼽 부위의 복벽 결손을 통해 밖으로 나와 있으며 이를 덮는 막이 존재하는 선천성 기형입니다.",
        "surgery_title": "배꼽류 교정술",
        "organ_color": "#E67E22",
        "surgery_steps": [
            {"icon": "🩺", "title": "출생 직후 평가", "description": "탈출한 장기의 범위와 막의 상태, 동반 기형 여부를 확인합니다."},
            {"icon": "🛡️", "title": "탈출 장기 보호", "description": "노출된 부위를 보호하고 체온과 수분 상태를 관리합니다."},
            {"icon": "🔬", "title": "복벽 교정", "description": "결손의 크기와 복강 용적에 따라 일차적 또는 단계적 복벽 교정을 시행합니다."},
            {"icon": "🩹", "title": "수술 후 관리", "description": "호흡 기능과 장 기능, 영양 상태 등을 관찰합니다."}
        ]
    },

    "항문직장기형": {
        "keywords": ["항문직장기형", "항문 폐쇄", "선천성 항문기형"],
        "organ": "직장 및 항문",
        "body_part": "골반 및 회음부",
        "easy_explanation": "항문과 직장이 정상적으로 형성되지 않거나 주변 구조와 비정상적으로 연결되는 선천성 기형입니다.",
        "surgery_title": "항문직장기형 교정술",
        "organ_color": "#3498DB",
        "surgery_steps": [
            {"icon": "🩺", "title": "기형 평가", "description": "항문의 형태와 직장의 위치, 비뇨생식기와의 연결 여부를 평가합니다."},
            {"icon": "🔍", "title": "동반 기형 확인", "description": "비뇨기계와 척추 등 동반 기형 여부를 확인합니다."},
            {"icon": "🔬", "title": "교정 수술", "description": "기형의 유형에 따라 항문직장 구조를 재건하는 수술을 시행합니다."},
            {"icon": "🩹", "title": "배변 기능 관찰", "description": "수술 후 항문 구조와 배변 기능을 장기적으로 관찰합니다."}
        ]
    },

    "선천성 식도폐쇄증": {
        "keywords": ["식도폐쇄증", "기관식도루", "선천성 식도폐쇄"],
        "organ": "식도 및 기관",
        "body_part": "흉부",
        "easy_explanation": "식도가 정상적으로 연결되지 않고 막혀 있거나 기관과 비정상적인 통로가 연결되어 있는 선천성 질환입니다.",
        "surgery_title": "식도 연결 및 기관식도루 교정술",
        "organ_color": "#9B59B6",
        "surgery_steps": [
            {"icon": "🩺", "title": "출생 직후 평가", "description": "침 분비와 호흡 상태 등을 확인하고 식도 구조를 평가합니다."},
            {"icon": "🫁", "title": "호흡 및 영양 관리", "description": "흡인을 예방하고 수술 전 호흡과 전신 상태를 안정화합니다."},
            {"icon": "🔬", "title": "식도 재건 수술", "description": "해부학적 유형과 환자 상태에 따라 기관식도루를 교정하고 식도를 연결합니다."},
            {"icon": "🩹", "title": "수술 후 관찰", "description": "문합부 상태와 호흡, 수유 및 삼킴 기능을 확인합니다."}
        ]
    },

    # -----------------------------------------------------
    # 비뇨·생식기 질환
    # -----------------------------------------------------

    "잠복고환": {
        "keywords": ["잠복고환", "미하강 고환", "고환 하강 이상"],
        "organ": "고환",
        "body_part": "서혜부 및 음낭",
        "easy_explanation": "고환이 정상적인 하강 경로를 따라 음낭 안으로 내려오지 못한 상태입니다.",
        "surgery_title": "고환고정술",
        "organ_color": "#2980B9",
        "surgery_steps": [
            {"icon": "🩺", "title": "고환 위치 확인", "description": "신체검사 등을 통해 고환의 위치와 촉지 여부를 확인합니다."},
            {"icon": "🔍", "title": "치료 시기 평가", "description": "연령과 고환의 위치, 동반 질환 등을 평가합니다."},
            {"icon": "🔬", "title": "고환고정술", "description": "고환을 음낭 안으로 이동시키고 고정하는 수술을 시행할 수 있습니다."},
            {"icon": "🩹", "title": "수술 후 관찰", "description": "고환의 위치와 크기, 혈류 및 회복 상태를 관찰합니다."}
        ]
    },

    "요도하열": {
        "keywords": ["요도하열", "요도 입구 위치 이상", "Hypospadias"],
        "organ": "요도 및 음경",
        "body_part": "하복부 및 회음부",
        "easy_explanation": "요도 입구가 음경 끝이 아닌 아래쪽에 위치하는 선천성 기형입니다.",
        "surgery_title": "요도 재건술",
        "organ_color": "#2874A6",
        "surgery_steps": [
            {"icon": "🩺", "title": "기형 평가", "description": "요도 입구의 위치와 음경의 형태, 동반 기형 여부를 확인합니다."},
            {"icon": "🔍", "title": "수술 계획", "description": "기형의 유형과 정도에 따라 재건 방법을 계획합니다."},
            {"icon": "🔬", "title": "요도 재건", "description": "요도 입구를 적절한 위치로 재건하고 필요한 경우 음경 만곡을 교정합니다."},
            {"icon": "🩹", "title": "회복 및 관찰", "description": "배뇨 상태와 수술 부위 회복, 합병증 여부를 관찰합니다."}
        ]
    },

    "고환 염전": {
        "keywords": ["고환염전", "고환 꼬임", "정삭 염전"],
        "organ": "고환 및 정삭",
        "body_part": "음낭",
        "easy_explanation": "고환을 지지하는 정삭이 꼬이면서 고환으로 가는 혈류가 차단될 수 있는 응급 질환입니다.",
        "surgery_title": "고환 염전 응급 수술",
        "organ_color": "#C0392B",
        "surgery_steps": [
            {"icon": "🚨", "title": "응급 평가", "description": "갑작스러운 음낭 통증과 부종 등을 확인하고 신속하게 평가합니다."},
            {"icon": "🩺", "title": "혈류 및 상태 확인", "description": "필요한 경우 초음파 등을 통해 고환 혈류를 평가하지만 검사로 수술이 지연되어서는 안 됩니다."},
            {"icon": "🔬", "title": "응급 수술", "description": "수술로 꼬인 정삭을 풀고 고환의 생존 가능성을 평가한 뒤 고환고정술 등을 시행합니다."},
            {"icon": "🩹", "title": "수술 후 관찰", "description": "고환의 혈류와 회복 상태를 관찰합니다."}
        ]
    },

    "난소 염전": {
        "keywords": ["난소염전", "난소 꼬임", "부속기 염전"],
        "organ": "난소 및 난관",
        "body_part": "골반 및 하복부",
        "easy_explanation": "난소 또는 난관이 꼬이면서 혈류가 감소하거나 차단될 수 있는 응급 질환입니다.",
        "surgery_title": "난소 염전 복원술",
        "organ_color": "#D3548B",
        "surgery_steps": [
            {"icon": "🚨", "title": "응급 평가", "description": "갑작스러운 하복부 통증과 구역 등의 증상을 평가합니다."},
            {"icon": "🔍", "title": "영상검사 및 진단", "description": "초음파 등을 통해 난소 크기와 혈류, 주변 구조를 평가합니다."},
            {"icon": "🔬", "title": "수술적 염전 복원", "description": "수술로 꼬인 난소와 난관을 풀고 가능한 한 난소를 보존하는 방향으로 치료합니다."},
            {"icon": "🩹", "title": "회복 및 추적 관찰", "description": "난소의 회복 상태와 재발 가능성 등을 관찰합니다."}
        ]
    }
}


# =========================================================
# 기존 질환 데이터에 15종 추가
# =========================================================

DISEASE_DATA.update(ADDITIONAL_DISEASE_DATA)


# =========================================================
# 장기 위치
# =========================================================

ORGAN_POSITION = {
    "위": (0.15, 3.30),
    "담낭": (-0.20, 3.55),
    "췌장": (0.00, 3.05),
    "신장": (-0.25, 2.05),
    "장": (0.00, 2.75),
    "대장": (0.00, 2.55),
    "소장": (0.00, 2.75),
    "충수": (0.25, 2.55),
    "복벽": (0.00, 2.85),
    "요로": (0.00, 2.25),
}

# =========================================================
# 질환 분석
# =========================================================

def analyze_medical_info(text):

    text = text.strip()
    text = text.replace(" ", "")

    if not text:
        return None

    keywords = []

    for disease, info in DISEASE_DATA.items():

        for keyword in info["keywords"]:

            keywords.append(
                (
                    len(keyword),
                    keyword,
                    disease,
                    info
                )
            )

    # 긴 키워드부터 검색
    keywords.sort(
        key=lambda x: x[0],
        reverse=True
    )

    for _, keyword, disease, info in keywords:

        if keyword in text:

            return {
                "disease": disease,
                "organ": info["organ"],
                "body_part": info["body_part"]
            }

    return None


# =========================================================
# 인체 시각화
# =========================================================

def create_body_visualization(result, gender):

    fig = go.Figure()

    organ = result["organ"]

    x, y = ORGAN_POSITION.get(
        organ,
        (0, 3)
    )

    organ_color = DISEASE_DATA[
        result["disease"]
    ]["organ_color"]

    # -----------------------------------------------------
    # 머리
    # -----------------------------------------------------

    fig.add_shape(
        type="circle",
        x0=-0.35,
        x1=0.35,
        y0=5.05,
        y1=5.75,
        fillcolor="#FFE0BD",
        line=dict(
            color="#333333",
            width=2
        )
    )

    # -----------------------------------------------------
    # 성별에 따른 몸통
    # -----------------------------------------------------

    if gender == "여아":

        # 조금 더 둥근 형태의 몸통
        body_path = (
            "M -0.42 4.8 "
            "L 0.42 4.8 "
            "L 0.52 4.15 "
            "L 0.38 3.15 "
            "L 0.45 1.9 "
            "L -0.45 1.9 "
            "L -0.38 3.15 "
            "L -0.52 4.15 "
            "Z"
        )

        body_color = "#E57373"

    else:

        # 조금 더 직선적인 몸통
        body_path = (
            "M -0.48 4.8 "
            "L 0.48 4.8 "
            "L 0.48 1.9 "
            "L -0.48 1.9 "
            "Z"
        )

        body_color = "#64B5F6"

    fig.add_shape(
        type="path",
        path=body_path,
        fillcolor=body_color,
        line=dict(width=0)
    )

    # -----------------------------------------------------
    # 팔
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[-0.42, -1.05],
            y=[4.45, 2.8],
            mode="lines",
            line=dict(
                width=30,
                color="#FFCCBC"
            ),
            hoverinfo="skip",
            showlegend=False
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0.42, 1.05],
            y=[4.45, 2.8],
            mode="lines",
            line=dict(
                width=30,
                color="#FFCCBC"
            ),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # -----------------------------------------------------
    # 다리
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[-0.20, -0.65],
            y=[1.9, 0.1],
            mode="lines",
            line=dict(
                width=34,
                color="#FFCCBC"
            ),
            hoverinfo="skip",
            showlegend=False
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0.20, 0.65],
            y=[1.9, 0.1],
            mode="lines",
            line=dict(
                width=34,
                color="#FFCCBC"
            ),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # =====================================================
    # 장기 표현
    # =====================================================

    if organ == "충수":

        # 대장
        fig.add_trace(
            go.Scatter(
                x=[
                    -0.28,
                    -0.40,
                    -0.40,
                    0.40,
                    0.40,
                    0.28
                ],
                y=[
                    2.25,
                    2.45,
                    2.95,
                    2.95,
                    2.45,
                    2.25
                ],
                mode="lines",
                line=dict(
                    width=20,
                    color="#8BC34A"
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

        # 소장
        fig.add_trace(
            go.Scatter(
                x=[
                    -0.25,
                    0.25,
                    -0.25,
                    0.25
                ],
                y=[
                    2.55,
                    2.65,
                    2.75,
                    2.85
                ],
                mode="lines",
                line=dict(
                    width=13,
                    color="#FFCC80"
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

        # 충수
        fig.add_trace(
            go.Scatter(
                x=[
                    -0.28,
                    -0.48
                ],
                y=[
                    2.35,
                    2.20
                ],
                mode="lines",
                line=dict(
                    width=15,
                    color=organ_color
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

        # 염증 부위
        fig.add_trace(
            go.Scatter(
                x=[-0.48],
                y=[2.20],
                mode="markers",
                marker=dict(
                    size=28,
                    color="#FF1744",
                    line=dict(
                        color="white",
                        width=4
                    )
                ),
                hovertemplate="<b>염증이 발생한 충수</b><extra></extra>",
                showlegend=False
            )
        )

    elif organ in ["장", "소장", "대장"]:

        fig.add_trace(
            go.Scatter(
                x=[
                    -0.30,
                    -0.40,
                    -0.40,
                    0.40,
                    0.40,
                    0.30
                ],
                y=[
                    2.30,
                    2.45,
                    3.00,
                    3.00,
                    2.45,
                    2.30
                ],
                mode="lines",
                line=dict(
                    width=22,
                    color=organ_color
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[
                    -0.25,
                    0.25,
                    -0.20,
                    0.25
                ],
                y=[
                    2.45,
                    2.55,
                    2.75,
                    2.90
                ],
                mode="lines",
                line=dict(
                    width=13,
                    color="#FFCC80"
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

    elif organ == "위":

        fig.add_trace(
            go.Scatter(
                x=[
                    0.05,
                    0.25,
                    0.38,
                    0.15,
                    -0.05
                ],
                y=[
                    3.50,
                    3.45,
                    3.25,
                    3.05,
                    3.15
                ],
                mode="lines",
                line=dict(
                    width=35,
                    color=organ_color
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

    elif organ == "담낭":

        fig.add_trace(
            go.Scatter(
                x=[-0.25],
                y=[3.55],
                mode="markers",
                marker=dict(
                    size=28,
                    color=organ_color,
                    line=dict(
                        color="white",
                        width=3
                    )
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

    elif organ == "신장":

        fig.add_shape(
            type="circle",
            x0=x - 0.16,
            x1=x + 0.16,
            y0=y - 0.27,
            y1=y + 0.27,
            fillcolor=organ_color,
            line=dict(
                color="white",
                width=3
            )
        )

    elif organ == "췌장":

        fig.add_trace(
            go.Scatter(
                x=[-0.35, 0.35],
                y=[3.05, 3.05],
                mode="lines",
                line=dict(
                    width=22,
                    color=organ_color
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

    elif organ == "복벽":

        fig.add_shape(
            type="rect",
            x0=-0.35,
            x1=0.35,
            y0=2.25,
            y1=3.4,
            fillcolor="rgba(156,39,176,0.35)",
            line=dict(
                color=organ_color,
                width=5
            )
        )

    # =====================================================
    # 질환 부위 강조
    # =====================================================

    fig.add_shape(
        type="circle",
        x0=x - 0.32,
        x1=x + 0.32,
        y0=y - 0.32,
        y1=y + 0.32,
        fillcolor="rgba(255,255,255,0)",
        line=dict(
            color="#FF1744",
            width=5
        )
    )

    # =====================================================
    # 장기 이름
    # =====================================================

    fig.add_annotation(
        x=x,
        y=y,
        ax=x + 0.75,
        ay=y + 0.55,
        text=(
            f"<b>{organ}</b><br>"
            f"{result['body_part']}"
        ),
        showarrow=True,
        arrowhead=2,
        arrowsize=1.2,
        arrowwidth=3,
        font=dict(
            size=14,
            color="#333333"
        ),
        bgcolor="white",
        bordercolor="#FF1744",
        borderwidth=2,
        borderpad=8
    )

    # =====================================================
    # 레이아웃
    # =====================================================

    fig.update_layout(
        height=650,
        xaxis=dict(
            visible=False,
            range=[-1.5, 1.5],
            fixedrange=True
        ),
        yaxis=dict(
            visible=False,
            range=[-0.2, 6.0],
            fixedrange=True
        ),
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=20
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        dragmode=False
    )

    return fig

# =========================================================
# Session State
# =========================================================

if "medical_text" not in st.session_state:
    st.session_state.medical_text = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "selected_step" not in st.session_state:
    st.session_state.selected_step = 1

if "gender" not in st.session_state:
    st.session_state.gender = "여아"


# =========================================================
# 메인 화면 디자인
# =========================================================

st.markdown("""
<style>
.vitra-hero {
    padding: 2rem 2.2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #eef6ff 0%, #f8fbff 55%, #eefbf7 100%);
    border: 1px solid #dce9f5;
    margin-bottom: 1.5rem;
}

.vitra-title {
    font-size: 2.8rem;
    font-weight: 800;
    color: #18324a;
    margin-bottom: 0.25rem;
}

.vitra-subtitle {
    font-size: 1.25rem;
    font-weight: 650;
    color: #35627d;
    margin-bottom: 0.8rem;
}

.vitra-description {
    font-size: 1rem;
    line-height: 1.7;
    color: #526777;
}

.feature-card {
    padding: 1.25rem;
    border-radius: 16px;
    border: 1px solid #e1e8ee;
    background-color: white;
    min-height: 155px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.feature-icon {
    font-size: 1.8rem;
    margin-bottom: 0.4rem;
}

.feature-title {
    font-size: 1.08rem;
    font-weight: 700;
    color: #243b53;
    margin-bottom: 0.4rem;
}

.feature-text {
    font-size: 0.9rem;
    line-height: 1.55;
    color: #667784;
}
/* 주요 기능 카드 크기 통일 */
.feature-card {
    height: 240px !important;
    min-height: 240px !important;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    padding: 24px;
    overflow: hidden;
}

.feature-icon {
    font-size: 36px;
    margin-bottom: 16px;
    flex-shrink: 0;
}

.feature-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 12px;
    flex-shrink: 0;
}

.feature-text {
    font-size: 16px;
    line-height: 1.7;
    flex-grow: 1;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 메인 Hero
# =========================================================

st.markdown("""
<div class="vitra-hero">
    <div class="vitra-title">🩺 VITRA</div>
    <div class="vitra-subtitle">
        소아외과 의료정보를 시각적으로 탐색하다
    </div>
    <div class="vitra-description">
        질환과 해부학적 구조를 연결하고, 치료·수술 과정을 단계별로 확인하며
        의료정보를 보다 직관적으로 탐색할 수 있도록 설계한
        의료정보 시각화 프로토타입입니다.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 주요 기능 카드
# =========================================================

st.markdown("### VITRA에서 할 수 있는 것")

# 첫 번째 행
feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🩺</div>
        <div class="feature-title">질환 검색</div>
        <div class="feature-text">
            질환명을 입력하여 관련 질환 정보를 검색하고
            주요 증상과 특징을 확인할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🩺 질환 검색하기", key="disease_search_button",
                 use_container_width=True):
        st.switch_page("pages/disease_search.py")

with feature2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚖️</div>
        <div class="feature-title">치료 방법 비교</div>
        <div class="feature-text">
            질환별 치료 방법의 특징과 차이를
            비교하여 살펴볼 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⚖️ 치료 방법 비교하기",
                 key="treatment_comparison_button",
                 use_container_width=True):
        st.switch_page("pages/treatment_comparison.py")

with feature3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🫀</div>
        <div class="feature-title">신체 부위 시각화</div>
        <div class="feature-text">
            인체의 주요 장기와 해부학적 위치를
            시각적으로 확인할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🫀 신체 부위 탐색하기",
                 key="body_visualization_button",
                 use_container_width=True):
        st.switch_page("pages/body_visualization.py")

st.markdown("<br>", unsafe_allow_html=True)

# 두 번째 행
feature4, feature5 = st.columns(2)

with feature4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔬</div>
        <div class="feature-title">치료 · 수술 과정</div>
        <div class="feature-text">
            질환별 치료 및 수술 과정을 단계별로 확인하여
            복잡한 의료정보를 구조적으로 살펴볼 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔬 치료·수술 과정 살펴보기",
                 key="surgery_visualization_button",
                 use_container_width=True):
        st.switch_page("pages/surgery_visualization.py")

with feature5:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💊</div>
        <div class="feature-title">의약품 정보 탐색</div>
        <div class="feature-text">
            의약품명이나 성분명을 검색하여
            공식 의약품 정보를 확인할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💊 의약품 정보 탐색하기",
                 key="medicine_button",
                 use_container_width=True):
        st.switch_page("pages/medicine.py")

st.divider()

# =========================================================
# 사이드바
# =========================================================

with st.sidebar:

    st.header("🩺 VITRA")

    st.caption(
        "소아외과 의료정보 시각화"
    )

    st.write(
        "소아외과 관련 의료정보를 시각적으로 탐색하기 위한 "
        "교육용 프로토타입입니다."
    )

    st.divider()

    st.subheader("📚 기능 탐색")

    if st.button(
        "🧍 신체 부위 시각화",
        use_container_width=True
    ):
        st.switch_page("pages/body_visualization.py")

    if st.button(
        "🔎 질환 검색",
        use_container_width=True
    ):
        st.switch_page("pages/disease_search.py")

    if st.button(
        "💊 의약품 검색",
        use_container_width=True
    ):
        st.switch_page("pages/medicine.py")

    st.divider()

    if st.button(
        "🔄 새로운 환자 입력",
        use_container_width=True
    ):
        st.session_state.medical_text = ""
        st.session_state.medical_text_input = ""
        st.session_state.analysis_result = None
        st.session_state.selected_step = 1
        st.session_state.gender = "여아"

        st.rerun()

# =========================================================
# 환자 정보 표시
# =========================================================

st.header("1. 환자 정보")

gender_col1, gender_col2 = st.columns(
    [1, 3]
)

with gender_col1:

    gender_choice = st.radio(
        "성별",
        ["👧 여아", "👦 남아"],
        horizontal=True,
        index=(
            0
            if st.session_state.gender == "여아"
            else 1
        )
    )

    if "여아" in gender_choice:
        st.session_state.gender = "여아"
    else:
        st.session_state.gender = "남아"

with gender_col2:

    if st.session_state.gender == "여아":

        st.info(
            "👧 여아의 인체 시각화가 선택되었습니다."

        )

    else:

        st.info(
            "👦 남아의 인체 시각화가 선택되었습니다."
        )


# =========================================================
# 의료 정보 입력
# =========================================================

st.header("2. 검사·진료 정보 입력")

medical_text = st.text_area(
    "검사 결과 또는 진료 내용을 입력하세요.",
    placeholder="예: 복부 초음파에서 충수돌기 주변에 염증 소견이 관찰됨.",
    height=150,
    key="medical_text_input"
)



# =========================================================
# 분석 버튼 및 질환 분석
# =========================================================

if st.button(
    "🔍 의료 정보 분석하기",
    type="primary",
    use_container_width=True
):
    st.session_state.medical_text = medical_text

    if not medical_text.strip():
        st.warning("검사 결과 또는 진료 내용을 먼저 입력해 주세요.")

        st.session_state.analysis_result = None

    else:
        result = analyze_medical_info(medical_text)

        st.session_state.analysis_result = result
        st.session_state.selected_step = 1

        if result is None:
            st.warning(
                "현재 등록된 질환 정보에서 "
                "관련 질환을 찾지 못했습니다."
            )

            search_text = "".join(medical_text.split())
            disease_names = list(DISEASE_DATA.keys())

            suggestions = get_close_matches(
                search_text,
                disease_names,
                n=3,
                cutoff=0.3
            )

            if suggestions:
                st.info("혹시 다음 질환을 찾으셨나요?")

                for disease_name in suggestions:
                    st.write(f"• {disease_name}")

        else:
            st.success(
                f"{result['disease']} 관련 정보를 찾았습니다."
            )


# =========================================================
# 분석 결과 표시
# =========================================================

result = st.session_state.analysis_result

if result is not None:

    disease = result["disease"]

    information = DISEASE_DATA[disease]

    st.divider()

    # -----------------------------------------------------
    # 질환 분석 결과
    # -----------------------------------------------------

    st.header("3. 질환 분석")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("분석 결과")

        st.write(f"**질환:** {disease}")
        st.write(f"**관련 장기:** {result['organ']}")
        st.write(f"**신체 부위:** {result['body_part']}")
        st.write(
            f"**환자 성별:** {st.session_state.gender}"
        )

    with col2:

        st.info(information["easy_explanation"])

    # -----------------------------------------------------
    # 신체 시각화
    # -----------------------------------------------------

    st.divider()

    st.header("4. 신체 부위 시각화")

    st.write(
        "질환과 관련된 장기를 인체의 위치와 함께 "
        "시각적으로 확인할 수 있습니다."
    )

    body_figure = create_body_visualization(
        result,
        st.session_state.gender
    )

    st.plotly_chart(
        body_figure,
        use_container_width=True
    )

    st.caption(
        "🔴 빨간 테두리는 질환과 관련된 부위를 나타냅니다."
    )

    # -----------------------------------------------------
    # 치료·수술 과정 페이지 이동
    # -----------------------------------------------------

    st.divider()

    st.header("5. 치료·수술 과정")

    st.write(
        "선택한 질환의 치료 및 수술 과정을 "
        "별도 페이지에서 단계별로 확인할 수 있습니다."
    )

    if st.button(
        "🔬 치료·수술 과정 자세히 보기",
        key="open_surgery_page",
        use_container_width=True
    ):

        st.session_state.surgery_disease = disease

        st.session_state.surgery_steps = (
            information["surgery_steps"]
        )

        st.session_state.selected_step = 1

        st.switch_page(
            "pages/surgery_visualization.py"
        )


# =========================================================
# 지원 질환
# =========================================================

st.divider()

with st.expander("📋 현재 분석 가능한 질환"):

    for disease_name in DISEASE_DATA:

        st.write(f"• {disease_name}")
