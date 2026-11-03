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
