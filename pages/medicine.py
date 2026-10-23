import streamlit as st
import requests

# ==================================================
# API 설정
# ==================================================

API_KEY = st.secrets["MFDS_API_KEY"]

BASE_URL = (
    "https://apis.data.go.kr/1471000/"
    "DrbEasyDrugInfoService"
)

SEARCH_URL = (
    f"{BASE_URL}/getDrbEasyDrugList"
)

# ==================================================
# 페이지 설정
# ==================================================

st.set_page_config(
    page_title="의약품 정보 검색",
    page_icon="💊",
    layout="wide"
)

st.title("💊 의약품 검색")

st.write(
    "의약품의 효능, 복용방법, 주의사항을 쉽게 확인할 수 있습니다."
)

# ==================================================
# 검색 함수
# ==================================================

def search_medicine(keyword):

    params = {
        "serviceKey": API_KEY,
        "pageNo": 1,
        "numOfRows": 20,
        "itemName": keyword,
        "type": "json"
    }

    response = requests.get(
        SEARCH_URL,
        params=params,
        timeout=30
    )

    data = response.json()

    body = data.get("body", {})

    items = body.get("items", [])

    if isinstance(items, dict):
        items = [items]

    return items

# ==================================================
# 검색창
# ==================================================

keyword = st.text_input(
    "검색할 의약품명을 입력하세요",
    placeholder="예: 타이레놀"
)

# ==================================================
# 검색
# ==================================================

if st.button("검색하기", type="primary"):

    if keyword.strip() == "":
        st.warning("의약품명을 입력하세요.")

    else:

        with st.spinner("검색 중..."):

            items = search_medicine(keyword)

        if len(items) == 0:

            st.warning("검색 결과가 없습니다.")

        else:

            st.success(
                f"{len(items)}건 검색되었습니다."
            )

            for item in items:

                medicine_name = item.get(
                    "itemName",
                    "의약품명 없음"
                )

                company = item.get(
                    "entpName",
                    "-"
                )

                with st.expander(
                    f"💊 {medicine_name}"
                ):

                    # ==================================================
                    # 환자용 설명
                    # ==================================================

                    st.markdown("## 😊 환자용 설명")

                    st.markdown(
                        "### 📋 효능 · 효과"
                    )

                    st.write(
                        item.get(
                            "efcyQesitm",
                            "정보 없음"
                        )
                    )

                    st.markdown(
                        "### 💊 복용 방법"
                    )

                    st.write(
                        item.get(
                            "useMethodQesitm",
                            "정보 없음"
                        )
                    )

                    st.markdown(
                        "### ⚠️ 복용 시 주의사항"
                    )

                    st.write(
                        item.get(
                            "atpnQesitm",
                            "정보 없음"
                        )
                    )

                    st.markdown(
                        "### 🚨 중요 경고"
                    )

                    st.warning(
                        item.get(
                            "atpnWarnQesitm",
                            "정보 없음"
                        )
                    )

                    st.markdown(
                        "### 🚫 약물 상호작용"
                    )

                    st.write(
                        item.get(
                            "intrcQesitm",
                            "정보 없음"
                        )
                    )

                    st.markdown(
                        "### 🤒 부작용"
                    )

                    st.write(
                        item.get(
                            "seQesitm",
                            "정보 없음"
                        )
                    )

                    st.markdown(
                        "### 📦 보관 방법"
                    )

                    st.write(
                        item.get(
                            "depositMethodQesitm",
                            "정보 없음"
                        )
                    )

                    st.divider()

                    # ==================================================
                    # 의료진 참고 정보
                    # ==================================================

                    with st.expander(
                        "👨‍⚕️ 의료진 참고 정보"
                    ):

                        st.write(
                            f"제조사: {company}"
                        )

                        st.write(
                            f"품목기준코드: {item.get('itemSeq', '-')}"
                        )

                        st.write(
                            f"공개일자: {item.get('openDe', '-')}"
                        )

                        st.write(
                            f"최종 수정일: {item.get('updateDe', '-')}"
                        )

                        if item.get("bizrno"):
                            st.write(
                                f"사업자번호: {item.get('bizrno')}"
                            )

# ==================================================
# 하단 안내
# ==================================================

st.divider()

st.caption(
    "본 정보는 식품의약품안전처 의약품개요정보(e약은요)를 기반으로 제공합니다."
)
