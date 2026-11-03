# =========================================================
# 치료/수술 과정 시각화
# =========================================================

def create_surgery_visualization(steps, selected_step):

    disease = result["disease"]
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
# 수술 과정 페이지 화면
# =========================================================

st.set_page_config(
    page_title="치료·수술 과정 | VITRA",
    page_icon="🔬",
    layout="wide"
)

if "surgery_steps" not in st.session_state:
    st.warning("먼저 질환 검색에서 질환을 분석해 주세요.")
    st.stop()

steps = st.session_state.surgery_steps
disease = st.session_state.surgery_disease

st.title("🔬 치료 · 수술 과정 시각화")

st.subheader(disease)

st.write(
    "선택한 질환의 치료 및 수술 과정을 단계별로 확인할 수 있습니다."
)

if "surgery_selected_step" not in st.session_state:
    st.session_state.surgery_selected_step = 1

# 단계 선택 버튼
button_columns = st.columns(len(steps))

for i, step in enumerate(steps):

    with button_columns[i]:

        if st.button(
            f"{step['icon']} {i + 1}단계",
            key=f"surgery_step_{i}",
            use_container_width=True
        ):
            st.session_state.surgery_selected_step = i + 1

# 그래프 표시
selected_step = st.session_state.surgery_selected_step

fig = create_surgery_visualization(
    steps,
    selected_step
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# 선택 단계 설명
current_step = steps[selected_step - 1]

st.subheader(
    f"{selected_step}단계. {current_step['title']}"
)

st.info(current_step["description"])

# 전체 과정
with st.expander("📋 전체 치료·수술 과정 보기"):

    for i, step in enumerate(steps):

        st.markdown(
            f"### {i + 1}. {step['icon']} {step['title']}"
        )

        st.write(step["description"])

        if i < len(steps) - 1:
            st.divider()
