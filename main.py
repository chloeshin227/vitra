import streamlit as st
import plotly.graph_objects as go

# =========================================================
# 기본 설정
# =========================================================

st.set_page_config(
    page_title="VITRA",
    page_icon="🩺",
    layout="wide"
)

# =========================================================
# 질환 데이터
# =========================================================

DISEASE_DATA = {
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
    "충수": (-0.25, 2.35),
    "복벽": (0.00, 2.85),
    "요로": (0.00, 2.25),
}

# =========================================================
# 질환 분석
# =========================================================

def analyze_medical_info(text):

    text = text.strip()

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
# 치료/수술 과정 시각화
# =========================================================

def create_surgery_visualization(
    result,
    selected_step
):

    disease = result["disease"]

    steps = DISEASE_DATA[
        disease
    ]["surgery_steps"]

    fig = go.Figure()

    # 연결선
    for i in range(len(steps) - 1):

        fig.add_trace(
            go.Scatter(
                x=[i + 1, i + 2],
                y=[0, 0],
                mode="lines",
                line=dict(
                    width=7
                ),
                hoverinfo="skip",
                showlegend=False
            )
        )

    # 단계
    for i, step in enumerate(steps):

        step_number = i + 1

        is_selected = (
            step_number == selected_step
        )

        size = (
            65
            if is_selected
            else 45
        )

        fig.add_trace(
            go.Scatter(
                x=[step_number],
                y=[0],
                mode="markers+text",
                marker=dict(
                    size=size,
                    line=dict(
                        color="white",
                        width=4
                    )
                ),
                text=[
                    str(step_number)
                ],
                textposition="middle center",
                textfont=dict(
                    size=18,
                    color="white"
                ),
                hovertemplate=(
                    f"<b>{step['title']}</b><br>"
                    f"{step['description']}"
                    "<extra></extra>"
                ),
                showlegend=False
            )
        )

        fig.add_annotation(
            x=step_number,
            y=0.45,
            text=step["icon"],
            showarrow=False,
            font=dict(
                size=25
            )
        )

        fig.add_annotation(
            x=step_number,
            y=-0.42,
            text=(
                f"<b>{step_number}. "
                f"{step['title']}</b>"
            ),
            showarrow=False,
            font=dict(
                size=13
            )
        )

    current = steps[
        selected_step - 1
    ]

    fig.add_annotation(
        x=selected_step,
        y=-0.95,
        text=(
            f"<b>{current['title']}</b><br>"
            f"{current['description']}"
        ),
        showarrow=False,
        font=dict(
            size=13
        ),
        bgcolor="white",
        bordercolor="#1976D2",
        borderwidth=2,
        borderpad=10,
        xanchor="center"
    )

    fig.update_layout(
        height=430,
        xaxis=dict(
            visible=False,
            range=[
                0.5,
                len(steps) + 0.5
            ]
        ),
        yaxis=dict(
            visible=False,
            range=[
                -1.5,
                0.9
            ]
        ),
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        plot_bgcolor="white",
        paper_bgcolor="white"
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

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🩺</div>
        <div class="feature-title">질환 · 해부학 탐색</div>
        <div class="feature-text">
            질환명을 입력하면 관련 장기와 해부학적 위치를
            시각적으로 확인할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with feature2:
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

with feature3:
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

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# 의약품 정보 바로가기
# =========================================================

medicine_col1, medicine_col2 = st.columns([3, 1])

with medicine_col1:
    st.info(
        "💊 의약품 정보 탐색 기능이 추가되었습니다.\n\n"
        "의약품명 또는 성분명을 검색하여 의약품의 기본 정보와 "
        "주의사항, 상호작용 등의 정보를 확인할 수 있습니다."
    )

with medicine_col2:
    if st.button(
        "💊 의약품 정보\n탐색하기",
        use_container_width=True
    ):
        st.switch_page("pages/medicine.py")

st.divider()

# =========================================================
# 사이드바
# =========================================================

with st.sidebar:

    st.header("🩺 VITRA")

    st.caption(
        "Pediatric Surgery Medical Visualization"
    )

    st.write(
        "소아외과 관련 의료정보를 시각적으로 탐색하기 위한 "
        "교육용 프로토타입입니다."
    )

    st.divider()

    st.subheader("📚 정보 탐색")

    if st.button(
        "💊 의약품 정보",
        use_container_width=True
    ):
        st.switch_page("pages/medicine.py")

    st.divider()

    st.subheader("👤 환자 정보")

    gender = st.radio(
        "환자의 성별을 선택하세요.",
        ["여아", "남아"],
        horizontal=True,
        index=(
            0
            if st.session_state.gender == "여아"
            else 1
        )
    )

    st.session_state.gender = gender

    st.divider()

    if st.button(
        "🔄 새로운 환자 입력",
        use_container_width=True
    ):

        st.session_state.medical_text = ""
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
    value=st.session_state.medical_text,
    placeholder=(
        "예: 복부 초음파에서 "
        "충수돌기 주변에 염증 소견이 관찰됨."
    ),
    height=150
)


# =========================================================
# 분석 버튼
# =========================================================

if st.button(
    "🔍 의료 정보 분석하기",
    type="primary",
    use_container_width=True
):

    st.session_state.medical_text = medical_text

    result = analyze_medical_info(
        medical_text
    )

    if result is None:

        st.session_state.analysis_result = None

        st.error(
            "현재 등록된 질환 정보에서 "
            "관련 질환을 찾지 못했습니다."
        )

    else:

        st.session_state.analysis_result = result
        st.session_state.selected_step = 1


# =========================================================
# 결과
# =========================================================

result = st.session_state.analysis_result


if result is not None:

    disease = result["disease"]

    information = DISEASE_DATA[
        disease
    ]

    # -----------------------------------------------------
    # 질환 분석
    # -----------------------------------------------------

    st.divider()

    st.header("3. 질환 분석")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("분석 결과")

        st.write(
            f"**질환:** {disease}"
        )

        st.write(
            f"**관련 장기:** {result['organ']}"
        )

        st.write(
            f"**신체 부위:** {result['body_part']}"
        )

        st.write(
            f"**환자 성별:** "
            f"{st.session_state.gender}"
        )

    with col2:

        st.info(
            information[
                "easy_explanation"
            ]
        )

    # -----------------------------------------------------
    # 신체 시각화
    # -----------------------------------------------------

    st.divider()

    st.header("4. 신체 부위 시각화")

    st.write(
        "선택한 환자 성별을 반영하여 "
        "질환과 관련된 장기를 인체 내부의 위치와 함께 "
        "강조하여 표시합니다."
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
    # 치료 과정
    # -----------------------------------------------------

    st.divider()

    st.header("5. 치료·수술 과정 시각화")

    st.write(
        "치료 또는 수술 과정을 단계별로 "
        "확인할 수 있습니다."
    )

    steps = information[
        "surgery_steps"
    ]

    st.subheader("단계 선택")

    button_columns = st.columns(
        len(steps)
    )

    for i, step in enumerate(steps):

        with button_columns[i]:

            if st.button(
                f"{step['icon']} {i + 1}단계",
                key=f"step_{i}",
                use_container_width=True
            ):

                st.session_state.selected_step = (
                    i + 1
                )

    surgery_figure = create_surgery_visualization(
        result,
        st.session_state.selected_step
    )

    st.plotly_chart(
        surgery_figure,
        use_container_width=True
    )

    current_step = steps[
        st.session_state.selected_step - 1
    ]

    st.subheader(
        f"{current_step['icon']} "
        f"{st.session_state.selected_step}단계. "
        f"{current_step['title']}"
    )

    st.info(
        current_step["description"]
    )

    with st.expander(
        "📋 전체 치료·수술 과정 보기"
    ):

        for i, step in enumerate(steps):

            st.markdown(
                f"### {i + 1}. "
                f"{step['icon']} "
                f"{step['title']}"
            )

            st.write(
                step["description"]
            )

            if i < len(steps) - 1:
                st.divider()

    # -----------------------------------------------------
    # 치료 후 변화
    # -----------------------------------------------------

    st.divider()

    st.header("6. 치료 후 예상되는 변화")

    st.write(
        "치료 방법과 회복 과정은 "
        "환자의 상태에 따라 달라질 수 있습니다."
    )

    st.info(
        "치료 후에는 질환과 관련된 증상이 호전되는지 "
        "관찰하고, 수술을 받은 경우 수술 부위와 "
        "신체 기능의 회복 상태를 확인합니다."
    )


# =========================================================
# 지원 질환
# =========================================================

st.divider()

with st.expander(
    "📋 현재 분석 가능한 질환"
):

    for disease in DISEASE_DATA:

        st.write(
            f"• {disease}"
        )


# =========================================================
# 안내
# =========================================================

st.caption(
    "※ VITRA는 교육용 프로토타입이며 "
    "실제 의료 진단이나 치료 결정을 대신하지 않습니다."
)


# ==========================================
# VITRA Body Image 시각화
# ==========================================

from pathlib import Path
import base64
from io import BytesIO

import streamlit as st
import plotly.graph_objects as go
from PIL import Image


def show_body_image():
    st.subheader("🧍 신체 부위 시각화")
    st.write(
        "성별과 장기를 선택하면 인체 이미지에서 "
        "해당 부위의 위치를 확인할 수 있습니다."
    )

    # 프로젝트 폴더의 images 폴더
    image_dir = Path(__file__).parent / "images"

    # 성별 선택
    gender = st.radio(
        "신체 이미지 선택",
        ["남성", "여성"],
        horizontal=True,
        key="body_gender",
    )

    if gender == "남성":
        image_path = image_dir / "boybody.png"
    else:
        image_path = image_dir / "girlbody.png"

    if not image_path.exists():
        st.error(f"이미지 파일을 찾을 수 없습니다: {image_path}")
        return

    # 장기별 위치 (이미지 기준 대략적인 비율)
    organs = {
        "뇌": (50, 9),
        "갑상샘": (50, 19),
        "폐": (43, 29),
        "심장": (48, 32),
        "간": (39, 40),
        "위": (57, 41),
        "신장": (42, 43),
        "소장": (50, 53),
        "대장": (50, 51),
        "충수(맹장)": (59, 56),
        "방광": (50, 64),
    }

    selected_organ = st.selectbox(
        "확인할 장기",
        list(organs.keys()),
        key="selected_body_organ",
    )

    # 이미지 불러오기
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # 이미지를 Plotly 배경으로 사용
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    encoded_image = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    x, y = organs[selected_organ]

    fig = go.Figure()

    fig.add_layout_image(
        dict(
            source=f"data:image/png;base64,{encoded_image}",
            xref="x",
            yref="y",
            x=0,
            y=100,
            sizex=100,
            sizey=100,
            sizing="stretch",
            layer="below",
        )
    )

    # 선택한 장기의 위치 표시
    fig.add_trace(
        go.Scatter(
            x=[x],
            y=[100 - y],
            mode="markers+text",
            text=[selected_organ],
            textposition="top center",
            marker=dict(
                size=16,
                color="red",
                line=dict(color="white", width=2),
            ),
            hovertemplate=(
                f"{selected_organ}<extra></extra>"
            ),
        )
    )

    fig.update_layout(
        width=500,
        height=650,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(
            range=[0, 100],
            visible=False,
            fixedrange=True,
        ),
        yaxis=dict(
            range=[0, 100],
            visible=False,
            fixedrange=True,
            scaleanchor="x",
        ),
        showlegend=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False},
    )

    st.caption(
        "장기 위치 표시는 이미지 위에 표시하기 위한 대략적인 좌표입니다. "
        "실제 해부학적 위치와 일치하는지 검증한 뒤 사용해야 합니다."
    )


show_body_image()

# =========================================================
# VITRA 공공 질병명·상병코드 검색 API
# 기존 코드 맨 아래에 추가
# =========================================================

import requests
import xml.etree.ElementTree as ET


HIRA_DISEASE_API_URL = (
    "https://apis.data.go.kr/B551182/"
    "diseaseInfoService1/getDissNameCodeList"
)


def get_hira_api_key():
    """Streamlit Secrets에서 HIRA 인증키를 가져옵니다."""
    possible_keys = [
        "HIRA_API_KEY",
        "hira_api_key",
        "HIRA_SERVICE_KEY",
    ]

    for key_name in possible_keys:
        try:
            key_value = st.secrets.get(key_name)
            if key_value:
                return str(key_value)
        except Exception:
            pass

    return None


def get_xml_value(item, possible_names):
    """XML 태그의 대소문자 차이를 고려해 값을 찾습니다."""
    for element in item.iter():
        tag_name = element.tag.split("}")[-1].lower()

        if tag_name in [name.lower() for name in possible_names]:
            if element.text:
                return element.text.strip()

    return ""


@st.cache_data(ttl=600, show_spinner=False)
def search_hira_diseases(search_text, api_key):
    """건강보험심사평가원 API에서 질병명칭과 코드를 검색합니다."""

    params = {
        "ServiceKey": api_key,
        "pageNo": "1",
        "numOfRows": "20",
        "SICK_NM": search_text,
    }

    response = requests.get(
        HIRA_DISEASE_API_URL,
        params=params,
        timeout=15,
    )

    response.raise_for_status()

    root = ET.fromstring(response.content)

    # API가 반환한 오류 확인
    result_code = get_xml_value(
        root,
        ["resultCode", "RESULTCODE"],
    )
    result_message = get_xml_value(
        root,
        ["resultMsg", "RESULTMSG"],
    )

    if result_code and result_code not in ["00", "0000"]:
        raise ValueError(
            f"API 응답 오류: {result_code} - {result_message}"
        )

    items = []

    for item in root.iter():
        tag_name = item.tag.split("}")[-1].lower()

        if tag_name != "item":
            continue

        disease_code = get_xml_value(
            item,
            ["sickCd", "SICK_CD"],
        )
        disease_name = get_xml_value(
            item,
            ["sickNm", "SICK_NM"],
        )
        english_name = get_xml_value(
            item,
            ["engNm", "ENG_NM", "engSickNm"],
        )

        if disease_name or disease_code:
            items.append({
                "질병명": disease_name or "정보 없음",
                "상병코드": disease_code or "정보 없음",
                "영문명": english_name or "정보 없음",
            })

    # 중복 결과 제거
    unique_items = []
    seen = set()

    for item in items:
        identity = (
            item["상병코드"],
            item["질병명"],
        )

        if identity not in seen:
            seen.add(identity)
            unique_items.append(item)

    return unique_items


# =========================================================
# 공공 질병 검색 화면
# =========================================================

st.divider()
st.header("🔎 공공 질병명·상병코드 검색")

st.write(
    "건강보험심사평가원 질병정보서비스를 이용해 "
    "질병명과 상병코드를 검색합니다."
)

st.caption(
    "검색 결과는 공공 API에서 제공하는 정보입니다. "
    "이 결과만으로 질환의 해부학적 위치나 치료·수술 과정을 "
    "확정하지 않습니다."
)

with st.form("hira_disease_search_form"):
    hira_search_text = st.text_input(
        "검색할 질병명",
        placeholder="예: 충수염, 장폐색, 탈장",
    )

    hira_search_button = st.form_submit_button(
        "공공 질병정보 검색",
        use_container_width=True,
    )

if hira_search_button:
    if not hira_search_text.strip():
        st.warning("검색할 질병명을 입력해 주세요.")

    else:
        hira_api_key = get_hira_api_key()

        if not hira_api_key:
            st.error(
                "HIRA API 인증키를 찾을 수 없습니다. "
                "Streamlit Secrets에 HIRA_API_KEY를 등록해 주세요."
            )

        else:
            try:
                with st.spinner("공공 질병정보를 검색하고 있습니다..."):
                    hira_results = search_hira_diseases(
                        hira_search_text.strip(),
                        hira_api_key,
                    )

                if hira_results:
                    st.success(
                        f"{len(hira_results)}개의 결과를 찾았습니다."
                    )

                    for index, disease in enumerate(hira_results):
                        with st.container(border=True):
                            st.markdown(
                                f"**{index + 1}. "
                                f"{disease['질병명']}**"
                            )

                            st.write(
                                f"상병코드: {disease['상병코드']}"
                            )

                            st.write(
                                f"영문명: {disease['영문명']}"
                            )

                            # 기존 VITRA 시각화 데이터에 등록된 질환인지 확인
                            matched_disease = None

                            for registered_name, info in DISEASE_DATA.items():
                                if (
                                    disease["질병명"] == registered_name
                                    or disease["질병명"]
                                    in info["keywords"]
                                ):
                                    matched_disease = registered_name
                                    break

                            if matched_disease:
                                st.success(
                                    f"VITRA 등록 질환: {matched_disease}"
                                )
                                st.caption(
                                    "기존 VITRA의 질환 시각화 데이터에 "
                                    "연결할 수 있는 질환입니다."
                                )
                            else:
                                st.info(
                                    "질병명·코드 조회 가능 / "
                                    "VITRA 시각화 정보는 아직 미등록"
                                )

                else:
                    st.info(
                        "검색 결과가 없습니다. "
                        "질병명의 일부만 입력해 다시 검색해 보세요."
                    )

            except requests.exceptions.Timeout:
                st.error(
                    "API 응답 시간이 초과되었습니다. "
                    "잠시 후 다시 시도해 주세요."
                )

            except requests.exceptions.RequestException as error:
                st.error(
                    "API 연결에 실패했습니다. "
                    "인증키와 API 주소, 네트워크 상태를 확인해 주세요."
                )
                st.caption(str(error))

            except ET.ParseError:
                st.error(
                    "API 응답을 XML로 읽을 수 없습니다. "
                    "인증키나 API 응답 형식을 확인해 주세요."
                )

            except ValueError as error:
                st.error(str(error))

            except Exception as error:
                st.error("검색 중 예상하지 못한 오류가 발생했습니다.")
                st.caption(str(error))



# =========================================================
# VITRA 8차시: HIRA 질병정보 API 연결
# main.py 맨 아래에 추가
# =========================================================

import requests
import xml.etree.ElementTree as ET

import requests
import xml.etree.ElementTree as ET
import streamlit as st

HIRA_DISEASE_API_URL = (
    "https://apis.data.go.kr/"
    "B551182/diseaseInfoService1/getDissNameCodeList1"
)


def get_xml_value(element, names):
    names = {name.lower() for name in names}

    for child in element.iter():
        tag = child.tag.split("}")[-1].lower()

        if tag in names and child.text:
            return child.text.strip()

    return ""


def search_hira_disease(search_text):
    api_key = st.secrets.get("HIRA_API_KEY", "")

    if not api_key:
        return [], "Streamlit Secrets에서 HIRA_API_KEY를 확인해 주세요."

    params = {
        "ServiceKey": api_key,
        "pageNo": 1,
        "numOfRows": 20,
        "sickType": "1",
        "medTp": "1",
        "diseaseType": "SICK_NM",
        "searchText": search_text.strip(),
    }

    try:
        response = requests.get(
            HIRA_DISEASE_API_URL,
            params=params,
            timeout=15,
        )

        if response.status_code != 200:
            return [], (
                f"API 요청 실패 (HTTP {response.status_code}). "
                "요청 주소와 매개변수를 확인해 주세요."
            )

        root = ET.fromstring(response.content)

        result_code = get_xml_value(root, ["resultCode"])
        result_message = get_xml_value(root, ["resultMsg"])

        if result_code and result_code not in ("00", "0000"):
            return [], (
                f"API 응답 오류: {result_code} - "
                f"{result_message or '요청을 처리하지 못했습니다.'}"
            )

        items = []

        for item in root.iter():
            if item.tag.split("}")[-1].lower() != "item":
                continue

            disease_code = get_xml_value(
                item, ["sickCd", "SICK_CD"]
            )
            disease_name = get_xml_value(
                item, ["sickNm", "SICK_NM"]
            )
            english_name = get_xml_value(
                item, ["engNm", "ENG_NM", "engSickNm"]
            )

            if disease_name or disease_code:
                items.append({
                    "질병명": disease_name or "정보 없음",
                    "상병코드": disease_code or "정보 없음",
                    "영문명": english_name or "정보 없음",
                })

        if not items:
            return [], "검색 결과가 없습니다. 검색어를 확인해 주세요."

        return items, None

    except requests.RequestException:
        return [], "API 연결에 실패했습니다. 네트워크를 확인해 주세요."
    except ET.ParseError:
        return [], "API 응답을 XML로 읽지 못했습니다."


# Streamlit 화면
st.subheader("HIRA 질병정보 검색")

search_text = st.text_input(
    "질병명 입력",
    placeholder="예: 충수염",
    key="hira_disease_search_text",
)

if st.button("HIRA API 검색", key="hira_disease_search_button"):
    if not search_text.strip():
        st.warning("질병명을 입력해 주세요.")
    else:
        results, error = search_hira_disease(search_text)

        if error:
            st.error(error)
        else:
            st.success(f"{len(results)}개 결과를 찾았습니다.")
            st.dataframe(results, use_container_width=True)


# ---------------------------------------------------------
# API 검색 화면
# ---------------------------------------------------------

st.divider()
st.header("🌐 HIRA 공공 질병정보 API")
st.write("건강보험심사평가원에서 질병명과 상병코드를 조회합니다.")

st.caption(
    "API에서 조회되는 질병명 전체가 VITRA의 증상 분석 대상인 것은 아닙니다. "
    "기존 분석 데이터가 있는 질환만 신체·치료 시각화에 연결됩니다."
)

with st.form("hira_api_search_form"):
    api_search_text = st.text_input(
        "질병명 검색",
        placeholder="예: 장염, 췌장염, 충수염",
    )
    api_search_submit = st.form_submit_button(
        "HIRA API 검색",
        use_container_width=True,
    )

if api_search_submit:
    if not api_search_text.strip():
        st.warning("검색할 질병명을 입력해 주세요.")
    else:
        try:
            api_key = st.secrets["HIRA_API_KEY"]

            with st.spinner("HIRA API에 연결하고 있습니다..."):
                api_results = search_hira_disease(
                    api_search_text.strip(),
                    api_key,
                )

            if not api_results:
                st.info("검색 결과가 없습니다. 다른 질병명을 입력해 보세요.")
            else:
                st.success(f"API 검색 결과: {len(api_results)}건")

                for item in api_results:
                    with st.container(border=True):
                        st.markdown(f"**{item['질병명']}**")
                        st.write(f"상병코드: {item['상병코드']}")
                        st.write(f"영문명: {item['영문명']}")

                        # 실제 분석 데이터가 존재하는지 확인
                        if item["질병명"] in DISEASE_DATA:
                            st.success(
                                "VITRA 분석 지원: 기존 질환 데이터와 연결됨"
                            )
                        else:
                            st.warning(
                                "질병명 조회 가능 · VITRA 분석 데이터 미등록"
                            )

        except KeyError:
            st.error(
                "Streamlit Secrets에 HIRA_API_KEY를 등록해 주세요."
            )
        except requests.exceptions.RequestException as error:
            st.error("API 연결에 실패했습니다. 인증키와 네트워크를 확인해 주세요.")
            st.caption(str(error))
        except ET.ParseError:
            st.error(
                "API 응답을 XML로 해석하지 못했습니다. "
                "인증키와 응답 내용을 확인해 주세요."
            )
        except ValueError as error:
            st.error(str(error))
        except Exception as error:
            st.error("검색 중 오류가 발생했습니다.")
            st.caption(str(error))

