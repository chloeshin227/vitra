import streamlit as st
import plotly.graph_objects as go


# =========================================================
# 페이지 기본 설정
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

    # 충수
    "충수염": {
        "keywords": ["충수염", "충수", "맹장염", "맹장"],
        "organ": "충수",
        "body_part": "오른쪽 아랫배"
    },

    # 장
    "장폐색": {
        "keywords": ["장폐색", "장 막힘", "소장폐색"],
        "organ": "장",
        "body_part": "복부"
    },

    "장중첩증": {
        "keywords": ["장중첩증", "장 중첩"],
        "organ": "장",
        "body_part": "복부"
    },

    "장회전이상": {
        "keywords": [
            "장회전이상",
            "장 회전 이상",
            "장 회전 이상증"
        ],
        "organ": "장",
        "body_part": "복부"
    },

    "장염": {
        "keywords": [
            "장염",
            "소장염",
            "대장염"
        ],
        "organ": "장",
        "body_part": "복부"
    },

    # 대장
    "선천성 거대결장증": {
        "keywords": [
            "선천성 거대결장증",
            "거대결장증",
            "히르슈스프룽병",
            "히르슈스프룽"
        ],
        "organ": "대장",
        "body_part": "아랫배"
    },

    "궤양성 대장염": {
        "keywords": [
            "궤양성 대장염",
            "궤양성 대장"
        ],
        "organ": "대장",
        "body_part": "아랫배"
    },

    # 탈장
    "탈장": {
        "keywords": [
            "탈장",
            "복벽 탈장"
        ],
        "organ": "복벽",
        "body_part": "복부"
    },

    "서혜부 탈장": {
        "keywords": [
            "서혜부 탈장",
            "사타구니 탈장",
            "서혜 탈장"
        ],
        "organ": "복벽",
        "body_part": "사타구니"
    },

    "배꼽 탈장": {
        "keywords": [
            "배꼽 탈장",
            "제대 탈장"
        ],
        "organ": "복벽",
        "body_part": "배꼽 주변"
    },

    # 담낭
    "담낭염": {
        "keywords": [
            "담낭염",
            "담낭"
        ],
        "organ": "담낭",
        "body_part": "오른쪽 윗배"
    },

    # 췌장
    "췌장염": {
        "keywords": [
            "췌장염",
            "췌장"
        ],
        "organ": "췌장",
        "body_part": "상복부"
    },

    # 위
    "위염": {
        "keywords": [
            "위염",
            "위 점막 염증"
        ],
        "organ": "위",
        "body_part": "상복부"
    },

    "위궤양": {
        "keywords": [
            "위궤양",
            "위 궤양"
        ],
        "organ": "위",
        "body_part": "상복부"
    },

    # 소장
    "크론병": {
        "keywords": [
            "크론병",
            "크론"
        ],
        "organ": "소장",
        "body_part": "복부"
    },

    # 신장
    "신장 질환": {
        "keywords": [
            "신장 이상",
            "신장 질환",
            "신장염"
        ],
        "organ": "신장",
        "body_part": "옆구리"
    },

    "수신증": {
        "keywords": [
            "수신증",
            "신우 확장"
        ],
        "organ": "신장",
        "body_part": "옆구리"
    },

    # 요로
    "요로 폐색": {
        "keywords": [
            "요로 폐색",
            "요관 폐색",
            "요로 막힘"
        ],
        "organ": "요로",
        "body_part": "옆구리"
    },

    # 식도
    "식도 폐쇄증": {
        "keywords": [
            "식도 폐쇄증",
            "식도폐쇄"
        ],
        "organ": "식도",
        "body_part": "가슴"
    },

    # 횡격막
    "선천성 횡격막 탈장": {
        "keywords": [
            "선천성 횡격막 탈장",
            "횡격막 탈장"
        ],
        "organ": "횡격막",
        "body_part": "가슴과 복부 사이"
    }
}


# =========================================================
# 의료 정보 분석
# =========================================================

def analyze_medical_info(text):
    """
    입력된 검사/진료 정보에서
    질환 관련 키워드를 찾아낸다.
    """

    text = text.strip()

    for disease, information in DISEASE_DATA.items():

        for keyword in information["keywords"]:

            if keyword in text:

                return {
                    "disease": disease,
                    "organ": information["organ"],
                    "body_part": information["body_part"]
                }

    return None


# =========================================================
# 장기별 위치
#
# 모든 좌표는 몸통 내부에 들어가도록 설정
# =========================================================

ORGAN_POSITION = {

    # 식도
    "식도": (0.00, 4.20),

    # 상복부
    "담낭": (-0.20, 3.45),
    "위": (0.18, 3.25),
    "췌장": (0.00, 3.05),

    # 신장
    "신장": (-0.27, 3.00),

    # 장
    "장": (0.00, 2.70),
    "소장": (0.00, 2.70),
    "대장": (0.00, 2.55),

    # 충수
    # 앞에서 본 사람 기준으로 오른쪽 아랫배는
    # 그림에서는 왼쪽에 표시
    "충수": (-0.25, 2.35),

    # 복벽
    "복벽": (0.00, 2.85),

    # 요로
    "요로": (0.00, 2.30),

    # 횡격막
    "횡격막": (0.00, 3.70)
}


# =========================================================
# 신체 부위 시각화
# =========================================================

def create_body_visualization(result):

    fig = go.Figure()

    # -----------------------------------------------------
    # 머리
    # -----------------------------------------------------

    fig.add_shape(
        type="circle",
        x0=-0.35,
        x1=0.35,
        y0=5.25,
        y1=5.95,
        line=dict(
            width=2,
            color="black"
        ),
        fillcolor="white"
    )

    # -----------------------------------------------------
    # 목
    # -----------------------------------------------------

    fig.add_shape(
        type="rect",
        x0=-0.13,
        x1=0.13,
        y0=4.75,
        y1=5.25,
        line=dict(width=0),
        fillcolor="lightgray"
    )

    # -----------------------------------------------------
    # 몸통
    # -----------------------------------------------------

    fig.add_shape(
        type="rect",
        x0=-0.45,
        x1=0.45,
        y0=1.9,
        y1=4.8,
        line=dict(
            width=2,
            color="black"
        ),
        fillcolor="lightgray"
    )

    # -----------------------------------------------------
    # 왼쪽 팔
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[-0.45, -1.05],
            y=[4.45, 2.85],
            mode="lines",
            line=dict(
                width=28,
                color="lightgray"
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
            x=[0.45, 1.05],
            y=[4.45, 2.85],
            mode="lines",
            line=dict(
                width=28,
                color="lightgray"
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
            x=[-0.20, -0.55],
            y=[1.9, 0.1],
            mode="lines",
            line=dict(
                width=32,
                color="lightgray"
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
            x=[0.20, 0.55],
            y=[1.9, 0.1],
            mode="lines",
            line=dict(
                width=32,
                color="lightgray"
            ),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # -----------------------------------------------------
    # 분석된 장기의 위치
    # -----------------------------------------------------

    organ = result["organ"]

    if organ in ORGAN_POSITION:

        x, y = ORGAN_POSITION[organ]

    else:

        x, y = 0, 3.0

    # -----------------------------------------------------
    # 장기 표시
    # -----------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[x],
            y=[y],
            mode="markers+text",

            marker=dict(
                size=24,
                symbol="circle",
                line=dict(
                    width=2,
                    color="black"
                )
            ),

            text=[organ],

            textposition="middle right",

            textfont=dict(
                size=14
            ),

            hovertemplate=(
                f"관련 장기: {organ}"
                "<extra></extra>"
            ),

            showlegend=False
        )
    )

    # -----------------------------------------------------
    # 그래프 설정
    # -----------------------------------------------------

    fig.update_layout(

        height=600,

        xaxis=dict(
            visible=False,
            range=[-1.4, 1.4],
            fixedrange=True
        ),

        yaxis=dict(
            visible=False,
            range=[-0.2, 6.2],
            fixedrange=True
        ),

        margin=dict(
            l=0,
            r=0,
            t=10,
            b=10
        ),

        plot_bgcolor="white",
        paper_bgcolor="white",

        dragmode=False
    )

    return fig


# =========================================================
# VITRA 메인 화면
# =========================================================

st.title("🩺 VITRA")

st.subheader(
    "의료 정보를 환자가 이해하기 쉬운 시각적 정보로"
)

st.write(
    "의료진이 검사 결과나 진료 내용을 입력하면 "
    "VITRA가 관련 질환과 신체 부위를 분석하여 "
    "시각적으로 보여줍니다."
)

st.divider()


# =========================================================
# 기능 1. 검사·진료 정보 입력
# =========================================================

st.header("1. 검사·진료 정보 입력")

medical_text = st.text_area(
    "검사 결과 또는 진료 내용을 입력하세요.",

    placeholder=(
        "예: 복부 초음파에서 충수 주변에 "
        "염증 소견이 관찰됨."
    ),

    height=150
)


# =========================================================
# 분석 버튼
# =========================================================

if st.button(
    "의료 정보 분석하기",
    type="primary"
):

    # -----------------------------------------------------
    # 입력값이 없는 경우
    # -----------------------------------------------------

    if not medical_text.strip():

        st.warning(
            "검사 결과나 진료 내용을 입력해주세요."
        )

    else:

        # -------------------------------------------------
        # 기능 2. 질환 정보 분석
        # -------------------------------------------------

        result = analyze_medical_info(
            medical_text
        )

        # -------------------------------------------------
        # 분석할 질환을 찾지 못한 경우
        # -------------------------------------------------

        if result is None:

            st.error(
                "현재 분석할 수 있는 질환 정보를 "
                "찾지 못했습니다."
            )

            st.info(
                "현재 VITRA는 등록된 질환의 "
                "주요 키워드를 기반으로 분석합니다."
            )

        # -------------------------------------------------
        # 질환을 찾은 경우
        # -------------------------------------------------

        else:

            st.success(
                "의료 정보 분석이 완료되었습니다."
            )

            col1, col2 = st.columns(2)

            # -------------------------------------------------
            # 분석 결과
            # -------------------------------------------------

            with col1:

                st.subheader("분석 결과")

                st.write(
                    f"**질환:** {result['disease']}"
                )

                st.write(
                    f"**관련 장기:** {result['organ']}"
                )

                st.write(
                    f"**신체 부위:** {result['body_part']}"
                )

                st.caption(
                    "※ 현재 결과는 입력된 텍스트의 "
                    "키워드를 기반으로 한 시각화 예시입니다."
                )

            # -------------------------------------------------
            # 기능 3. 신체 부위 시각화
            # -------------------------------------------------

            with col2:

                st.subheader(
                    "신체 부위 시각화"
                )

                figure = create_body_visualization(
                    result
                )

                st.plotly_chart(
                    figure,
                    use_container_width=True
                )


# =========================================================
# 지원 질환 목록
# =========================================================

with st.expander(
    "현재 분석 가능한 질환 보기"
):

    disease_names = list(
        DISEASE_DATA.keys()
    )

    for i in range(
        0,
        len(disease_names),
        2
    ):

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"• {disease_names[i]}"
            )

        if i + 1 < len(disease_names):

            with col2:

                st.write(
                    f"• {disease_names[i + 1]}"
                )
