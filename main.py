# ============================================================
# VITRA 메인 화면
# ============================================================

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
    font-size: 2.7rem;
    font-weight: 800;
    margin-bottom: 0.3rem;
    color: #18324a;
}

.vitra-subtitle {
    font-size: 1.25rem;
    font-weight: 600;
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
    min-height: 150px;
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

.section-title {
    font-size: 1.35rem;
    font-weight: 750;
    color: #243b53;
    margin-top: 1.5rem;
    margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Hero
# ------------------------------------------------------------

st.markdown("""
<div class="vitra-hero">
    <div class="vitra-title">VITRA</div>
    <div class="vitra-subtitle">
        소아외과 의료정보를 시각적으로 탐색하다
    </div>
    <div class="vitra-description">
        질환과 해부학적 구조를 연결하고,
        치료 과정을 단계별로 확인하며,
        의료정보를 보다 직관적으로 탐색할 수 있도록 설계한
        의료정보 시각화 프로토타입입니다.
    </div>
</div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# 주요 기능
# ------------------------------------------------------------

st.markdown(
    '<div class="section-title">VITRA에서 할 수 있는 것</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
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

with col2:
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

with col3:
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


# ------------------------------------------------------------
# 의약품 정보 페이지 바로가기
# ------------------------------------------------------------

st.markdown(
    '<div class="section-title">새롭게 추가된 기능</div>',
    unsafe_allow_html=True
)

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


# ------------------------------------------------------------
# 현재 분석 시작
# ------------------------------------------------------------

st.markdown(
    '<div class="section-title">질환 분석 시작하기</div>',
    unsafe_allow_html=True
)

st.caption(
    "아래에서 성별과 질환 정보를 입력하면 관련 해부학적 구조와 "
    "의료정보를 시각적으로 확인할 수 있습니다."
)
