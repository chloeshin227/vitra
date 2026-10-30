
# 치료 과정
# -----------------------------------------------------

st.divider()
st.header("5. 치료·수술 과정 시각화")
st.write(
    "치료 또는 수술 과정을 단계별로 "
    "확인할 수 있습니다."
)

steps = information["surgery_steps"]

st.subheader("단계 선택")

button_columns = st.columns(len(steps))

for i, step in enumerate(steps):
    with button_columns[i]:
        if st.button(
            f"{step['icon']} {i + 1}단계",
            key=f"step_{i}",
            use_container_width=True
        ):
            st.session_state.selected_step = i + 1

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

st.info(current_step["description"])

with st.expander("📋 전체 치료·수술 과정 보기"):
    for i, step in enumerate(steps):
        st.markdown(
            f"### {i + 1}. "
            f"{step['icon']} "
            f"{step['title']}"
        )

        st.write(step["description"])

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

with st.expander("📋 현재 분석 가능한 질환"):
    for disease in DISEASE_DATA:
        st.write(f"• {disease}")


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
