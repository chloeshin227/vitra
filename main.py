import streamlit as st
import plotly.graph_objects as go


# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="VITRA",
    page_icon="🩺",
    layout="wide"
)


# -----------------------------
# 질환 정보 분석 함수
# -----------------------------
def analyze_medical_info(text):
    """
    입력된 진료/검사 정보에서
    주요 질환 및 관련 신체 부위를 찾는다.
    """

    disease_data = {
        "충수염": {
            "keywords": ["충수염", "충수", "맹장염", "맹장"],
            "organ": "충수",
            "body_part": "오른쪽 아랫배"
        },
        "장폐색": {
            "keywords": ["장폐색", "장 막힘", "소장폐색"],
            "organ": "장",
            "body_part": "복부"
        },
        "탈장": {
            "keywords": ["탈장", "서혜부 탈장", "배꼽 탈장"],
            "organ": "복벽",
            "body_part": "복부"
        },
        "담낭염": {
            "keywords": ["담낭염", "담낭"],
            "organ": "담낭",
            "body_part": "오른쪽 윗배"
        },
        "췌장염": {
            "keywords": ["췌장염", "췌장"],
            "organ": "췌장",
            "body_part": "상복부"
        }
    }

    for disease, information in disease_data.items():
        for keyword in information["keywords"]:
            if keyword in text:
                return {
                    "disease": disease,
                    "organ": information["organ"],
                    "body_part": information["body_part"]
                }

    return None


# -----------------------------
# 신체 부위 시각화 함수
# -----------------------------
def create_body_visualization(result):
    """
    분석 결과에 따라 간단한 신체 그림을 생성한다.
    """

    fig = go.Figure()

    # 인체 윤곽
    fig.add_trace(
        go.Scatter(
            x=[0, 0, 0, 0, 0],
            y=[5, 4, 3, 2, 1],
            mode="lines",
            line=dict(width=25),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # 머리
    fig.add_shape(
        type="circle",
        x0=-0.35,
        x1=0.35,
        y0=5,
        y1=5.7,
        line=dict(width=2)
    )

    # 왼쪽 팔
    fig.add_trace(
        go.Scatter(
            x=[-0.2, -1.0],
            y=[4.3, 2.8],
            mode="lines",
            line=dict(width=15),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # 오른쪽 팔
    fig.add_trace(
        go.Scatter(
            x=[0.2, 1.0],
            y=[4.3, 2.8],
            mode="lines",
            line=dict(width=15),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # 왼쪽 다리
    fig.add_trace(
        go.Scatter(
            x=[-0.15, -0.6],
            y=[2.0, 0],
            mode="lines",
            line=dict(width=18),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # 오른쪽 다리
    fig.add_trace(
        go.Scatter(
            x=[0.15, 0.6],
            y=[2.0, 0],
            mode="lines",
            line=dict(width=18),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # 질환 부위 표시
    if result["organ"] == "충수":
        x, y = 0.45, 2.5

    elif result["organ"] == "장":
        x, y = 0, 2.8

    elif result["organ"] == "담낭":
        x, y = 0.25, 3.3

    elif result["organ"] == "췌장":
        x, y = 0, 3.1

    elif result["organ"] == "복벽":
        x, y = 0, 2.8

    else:
        x, y = 0, 3

    fig.add_trace(
        go.Scatter(
            x=[x],
            y=[y],
            mode="markers+text",
            marker=dict(
                size=30,
                symbol="circle"
            ),
            text=[result["organ"]],
            textposition="middle right",
            hovertemplate=f"{result['organ']}<extra></extra>",
            showlegend=False
        )
    )

    fig.update_layout(
        height=600,
        xaxis=dict(
            visible=False,
            range=[-1.5, 1.5]
        ),
        yaxis=dict(
            visible=False,
            range=[-0.5, 6]
        ),
        margin=dict(l=0, r=0, t=20, b=20),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig


# -----------------------------
# VITRA 화면
# -----------------------------

st.title("🩺 VITRA")
st.subheader("의료 정보를 환자가 이해하기 쉬운 시각적 정보로")

st.write(
    "의료진이 검사 결과나 진료 내용을 입력하면 "
    "VITRA가 관련 질환과 신체 부위를 분석하여 시각적으로 보여줍니다."
)

st.divider()


# -----------------------------
# 기능 1. 검사/진료 정보 입력
# -----------------------------

st.header("1. 검사·진료 정보 입력")

medical_text = st.text_area(
    "검사 결과 또는 진료 내용을 입력하세요.",
    placeholder="예: 복부 초음파에서 충수 주변에 염증 소견이 관찰됨.",
    height=150
)


# -----------------------------
# 분석 버튼
# -----------------------------

if st.button("의료 정보 분석하기", type="primary"):

    if not medical_text.strip():
        st.warning("검사 결과나 진료 내용을 입력해주세요.")

    else:

        # -----------------------------
        # 기능 2. 질환 정보 분석
        # -----------------------------

        result = analyze_medical_info(medical_text)

        if result is None:

            st.error(
                "현재 분석할 수 있는 질환 정보를 찾지 못했습니다."
            )

            st.info(
                "현재는 충수염, 장폐색, 탈장, 담낭염, "
                "췌장염 관련 키워드를 분석할 수 있습니다."
            )

        else:

            st.success("의료 정보 분석이 완료되었습니다.")

            col1, col2 = st.columns(2)

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

            # -----------------------------
            # 기능 3. 신체 부위 시각화
            # -----------------------------

            with col2:

                st.subheader("신체 부위 시각화")

                figure = create_body_visualization(result)

                st.plotly_chart(
                    figure,
                    use_container_width=True
                )
