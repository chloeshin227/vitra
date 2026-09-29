import streamlit as st
import plotly.graph_objects as go


# =========================================================
# 페이지 설정
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
                "description": "막힌 부분과 그 원인을 직접 확인합니다.",
                "icon": "🔍"
            },
            {
                "title": "문제 해결",
                "description": "막힘의 원인과 환자의 상태에 맞는 치료를 시행합니다.",
                "icon": "🛠️"
            },
            {
                "title": "회복 확인",
                "description": "장의 상태와 움직임을 확인하고 수술을 마무리합니다.",
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
            "장중첩증은 장의 한 부분이 다른 부분의 안쪽으로 "
            "말려 들어가는 상태입니다."
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
# 장기 위치
# =========================================================

ORGAN_POSITION = {

    "식도": (0.00, 4.10),

    "위": (0.15, 3.30),

    "담낭": (-0.20, 3.55),

    "췌장": (0.00, 3.05),

    "신장": (-0.25, 3.05),

    "장": (0.00, 2.75),

    "대장": (0.00, 2.55),

    "소장": (0.00, 2.75),

    "충수": (-0.25, 2.35),

    "복벽": (0.00, 2.85),

    "요로": (0.00, 2.25),

    "횡격막": (0.00, 3.70)
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
# 3번 기능
# 신체 부위 상세 시각화
# =========================================================

def create_detailed_body_visualization(result):

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
    # 몸통
    # -----------------------------------------------------

    fig.add_shape(
        type="path",

        path=(
            "M -0.45 4.8 "
            "L 0.45 4.8 "
            "L 0.45 1.9 "
            "L -0.45 1.9 Z"
        ),

        fillcolor="#1976D2",

        line=dict(
            width=0
        )
    )


    # -----------------------------------------------------
    # 왼쪽 팔
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[-0.38, -1.05],
            y=[4.45, 2.8],

            mode="lines",

            line=dict(
                width=30,
                color="#64B5F6"
            ),

            hoverinfo="skip",
            showlegend=False
        )
    )


    # -----------------------------------------------------
    # 오른쪽 팔
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[0.38, 1.05],
            y=[4.45, 2.8],

            mode="lines",

            line=dict(
                width=30,
                color="#FF5252"
            ),

            hoverinfo="skip",
            showlegend=False
        )
    )


    # -----------------------------------------------------
    # 왼쪽 다리
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[-0.20, -0.65],
            y=[1.9, 0.1],

            mode="lines",

            line=dict(
                width=34,
                color="#FF9E9E"
            ),

            hoverinfo="skip",
            showlegend=False
        )
    )


    # -----------------------------------------------------
    # 오른쪽 다리
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[0.20, 0.65],
            y=[1.9, 0.1],

            mode="lines",

            line=dict(
                width=34,
                color="#26A69A"
            ),

            hoverinfo="skip",
            showlegend=False
        )
    )


    # =====================================================
    # 장기별 기본 형태
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
                x=[-0.28, -0.48],
                y=[2.35, 2.20],

                mode="lines",

                line=dict(
                    width=15,
                    color=organ_color
                ),

                hoverinfo="skip",
                showlegend=False
            )
        )


        # 염증 강조
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

                hovertemplate=(
                    "<b>염증이 발생한 충수</b>"
                    "<extra></extra>"
                ),

                showlegend=False
            )
        )


    elif organ in ["장", "소장", "대장"]:

        # 대장
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


        # 소장
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

        # 신장
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


    elif organ == "식도":

        fig.add_trace(
            go.Scatter(
                x=[0, 0],
                y=[4.55, 3.65],

                mode="lines",

                line=dict(
                    width=15,
                    color=organ_color
                ),

                hoverinfo="skip",
                showlegend=False
            )
        )


    elif organ == "횡격막":

        fig.add_trace(
            go.Scatter(
                x=[-0.35, 0, 0.35],
                y=[3.7, 3.55, 3.7],

                mode="lines",

                line=dict(
                    width=15,
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


    elif organ == "요로":

        fig.add_trace(
            go.Scatter(
                x=[-0.15, 0, 0.15],
                y=[3.1, 2.6, 2.1],

                mode="lines",

                line=dict(
                    width=10,
                    color=organ_color
                ),

                hoverinfo="skip",
                showlegend=False
            )
        )


    # =====================================================
    # 문제 부위 강조 원
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
    # 확대 표시용 화살표
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
# 5번 기능
# 수술 과정 상세 시각화
# =========================================================

def create_detailed_surgery_visualization(
    result,
    selected_step
):

    disease = result["disease"]

    steps = DISEASE_DATA[
        disease
    ]["surgery_steps"]


    fig = go.Figure()


    # -----------------------------------------------------
    # 단계 사이 연결선
    # -----------------------------------------------------

    for i in range(
        len(steps) - 1
    ):

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


    # -----------------------------------------------------
    # 각 단계
    # -----------------------------------------------------

    for i, step in enumerate(steps):

        step_number = i + 1

        is_selected = (
            step_number == selected_step
        )


        if is_selected:

            size = 65

        else:

            size = 45


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


        # 아이콘
        fig.add_annotation(

            x=step_number,

            y=0.45,

            text=step["icon"],

            showarrow=False,

            font=dict(
                size=25
            )
        )


        # 단계 이름
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


    # -----------------------------------------------------
    # 현재 단계 설명
    # -----------------------------------------------------

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


# =========================================================
# 제목
# =========================================================

st.title("🩺 VITRA")

st.subheader(
    "의료 정보를 환자가 이해하기 쉬운 시각적 정보로"
)

st.write(
    "의료진이 검사 결과나 진료 내용을 입력하면 "
    "VITRA가 관련 질환과 신체 부위를 분석하고 "
    "치료 과정을 시각적으로 보여줍니다."
)


st.divider()


# =========================================================
# 사이드바
# =========================================================

with st.sidebar:

    st.header("VITRA")

    st.write(
        "환자와 보호자의 의료 정보 이해를 "
        "돕기 위한 시각화 프로그램"
    )

    st.divider()

    if st.button(
        "🔄 새로운 환자 입력",
        use_container_width=True
    ):

        st.session_state.medical_text = ""

        st.session_state.analysis_result = None

        st.session_state.selected_step = 1

        st.rerun()


# =========================================================
# 1. 검사 / 진료 정보 입력
# =========================================================

st.header("1. 검사·진료 정보 입력")


medical_text = st.text_area(

    "검사 결과 또는 진료 내용을 입력하세요.",

    value=st.session_state.medical_text,

    placeholder=(
        "예: 복부 초음파에서 충수돌기 주변에 "
        "염증 소견이 관찰됨."
    ),

    height=150
)


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
            "현재 분석할 수 있는 질환 정보를 찾지 못했습니다."
        )

    else:

        st.session_state.analysis_result = result

        st.session_state.selected_step = 1


# =========================================================
# 분석 결과
# =========================================================

result = st.session_state.analysis_result


if result is not None:

    disease = result["disease"]

    information = DISEASE_DATA[
        disease
    ]


    # =====================================================
    # 2. 질환 분석
    # =====================================================

    st.divider()

    st.header("2. 질환 분석")

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


    with col2:

        st.info(
            information["easy_explanation"]
        )


    # =====================================================
    # 3. 상세 신체 부위 시각화
    # =====================================================

    st.divider()

    st.header(
        "3. 신체 부위 시각화"
    )

    st.write(
        "질환과 관련된 장기를 인체 내부의 위치와 함께 "
        "강조하여 표시합니다."
    )


    body_figure = create_detailed_body_visualization(
        result
    )


    st.plotly_chart(
        body_figure,
        use_container_width=True
    )


    st.caption(
        "🔴 빨간 테두리: 질환과 관련된 부위"
    )


    # =====================================================
    # 5. 수술 과정 시각화
    # =====================================================

    st.divider()

    st.header(
        "4. 치료·수술 과정 시각화"
    )

    st.write(
        "치료 또는 수술 과정을 단계별로 확인할 수 있습니다."
    )


    steps = information[
        "surgery_steps"
    ]


    # -----------------------------------------------------
    # 단계 선택 버튼
    # -----------------------------------------------------

    st.subheader(
        "단계 선택"
    )


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

                st.session_state.selected_step = i + 1


    # -----------------------------------------------------
    # 수술 과정 그래픽
    # -----------------------------------------------------

    surgery_figure = create_detailed_surgery_visualization(

        result,

        st.session_state.selected_step
    )


    st.plotly_chart(
        surgery_figure,
        use_container_width=True
    )


    # -----------------------------------------------------
    # 현재 단계 카드
    # -----------------------------------------------------

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


    # =====================================================
    # 단계별 전체 설명
    # =====================================================

    with st.expander(
        "📋 전체 치료·수술 과정 보기"
    ):

        for i, step in enumerate(steps):

            st.markdown(
                f"### {i + 1}. "
                f"{step['icon']} {step['title']}"
            )

            st.write(
                step["description"]
            )

            if i < len(steps) - 1:

                st.divider()


    # =====================================================
    # 치료 후 변화
    # =====================================================

    st.divider()

    st.header(
        "5. 치료 후 예상되는 변화"
    )

    st.write(
        "치료 방법과 회복 과정은 환자의 상태에 따라 "
        "달라질 수 있습니다."
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
    "※ VITRA는 교육용 프로토타입이며 실제 의료 진단이나 "
    "치료 결정을 대신하지 않습니다."
)
