
from pathlib import Path
import base64
from io import BytesIO

import streamlit as st
import plotly.graph_objects as go
from PIL import Image


st.set_page_config(
    page_title="신체 부위 시각화 | VITRA",
    page_icon="🧍",
    layout="wide"
)


def show_body_image():

    st.title("🧍 신체 부위 시각화")

    st.write(
        "성별과 장기를 선택하면 인체 이미지에서 "
        "해당 부위의 위치를 확인할 수 있습니다."
    )

    # 프로젝트 루트의 images 폴더
    image_dir = Path(__file__).resolve().parent.parent / "images"

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
        st.error(
            f"이미지 파일을 찾을 수 없습니다: {image_path}"
        )
        return

    # 장기별 위치
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
        "충수(맹장)": (41, 53),
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
