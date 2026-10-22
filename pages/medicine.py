```python
import streamlit as st
import requests

# ==========================================
# 1. API 설정
# ==========================================

BASE_URL = (
    "https://apis.data.go.kr/"
    "1471000/DrugPrdtPrmsnInfoService08"
)

SEARCH_URL = f"{BASE_URL}/getDrugPrdtPrmsnInq08"

st.title("💊 의약품 정보 검색")
st.write("식품의약품안전처 의약품 제품 허가정보 API")

st.info(
    "의약품의 공개 정보를 검색하는 페이지입니다. "
    "검색 결과는 진단이나 복용 지침을 대신하지 않습니다."
)


# ==========================================
# 2. API 검색 함수
# ==========================================

def search_medicines(keyword):
    api_key = st.secrets.get("MFDS_API_KEY")

    if not api_key:
        st.error(
            "API 인증키가 없습니다. "
            "Streamlit Cloud의 Settings → Secrets를 확인해 주세요."
        )
        return None

    params = {
        "serviceKey": api_key,
        "type": "json",
        "pageNo": 1,
        "numOfRows": 10,
        "item_name": keyword,
    }

    try:
        response = requests.get(
            SEARCH_URL,
            params=params,
            timeout=60,
        )

        if response.status_code != 200:
            st.error(f"API 요청 실패: HTTP {response.status_code}")
            return None

        try:
            data = response.json()
        except ValueError:
            st.error("API 응답이 JSON 형식이 아닙니다.")
            return None

        # API 응답 구조 확인
        response_data = data.get("response", data)
        header = response_data.get("header", {})
        body = response_data.get("body", {})

        result_code = str(header.get("resultCode", ""))

        if result_code and result_code not in ("00", "0"):
            st.error(
                "API 오류: "
                + str(
                    header.get(
                        "resultMsg",
                        "응답 내용을 확인할 수 없습니다.",
                    )
                )
            )
            return None

        items = body.get("items", [])

        # items가 딕셔너리인 경우 처리
        if isinstance(items, dict):
            items = items.get("item", items)

        if isinstance(items, dict):
            items = [items]

        if not isinstance(items, list):
            return []

        return items

    except requests.exceptions.Timeout:
        st.error(
            "API 응답 시간이 초과되었습니다. "
            "잠시 후 다시 시도해 주세요."
        )
        return None

    except requests.exceptions.RequestException:
        st.error(
            "API 서버에 연결하지 못했습니다. "
            "주소와 네트워크를 확인해 주세요."
        )
        return None


# ==========================================
# 3. 검색 화면
# ==========================================

drug_name = st.text_input(
    "검색할 의약품명을 입력하세요",
    placeholder="예: 아스피린",
)

if st.button("검색하기", type="primary"):
    if not drug_name.strip():
        st.warning("의약품명을 입력해 주세요.")

    else:
        with st.spinner("의약품 정보를 검색하고 있습니다..."):
            items = search_medicines(drug_name.strip())

        if items is not None:
            if len(items) == 0:
                st.warning("검색 결과가 없습니다.")

            else:
                st.success(f"검색 결과 {len(items)}건")

                for index, item in enumerate(items, start=1):
                    # 실제 응답에서 확인한 필드명 사용
                    product_name = item.get(
                        "PRDUCT",
                        "의약품명 정보 없음",
                    )

                    ingredient_name = item.get(
                        "MTRAL_NM",
                        "정보 없음",
                    )

                    quantity = item.get(
                        "QNT",
                        "정보 없음",
                    )

                    unit = item.get(
                        "INGD_UNIT_CD",
                        "",
                    )

                    ingredient_code = item.get(
                        "MTRAL_CODE",
                        "정보 없음",
                    )

                    company = item.get(
                        "ENTRPS",
                        "정보 없음",
                    )

                    english_ingredient = item.get(
                        "MAIN_INGR_ENG",
                        "정보 없음",
                    )

                    approval_number = item.get(
                        "ENTRPS_PRMTSN_NO",
                        "정보 없음",
                    )

                    with st.expander(
                        f"{index}. {product_name}",
                        expanded=False,
                    ):
                        st.write(f"**의약품명:** {product_name}")
                        st.write(f"**주성분명:** {ingredient_name}")
                        st.write(
                            f"**함량:** {quantity} {unit}".strip()
                        )
                        st.write(f"**성분코드:** {ingredient_code}")
                        st.write(f"**제조업체:** {company}")
                        st.write(
                            f"**영문 주성분명:** {english_ingredient}"
                        )
                        st.write(
                            f"**허가 관련 번호:** {approval_number}"
                        )

                        with st.expander("원본 데이터 확인"):
                            st.json(item)


# ==========================================
# 4. 안내
# ==========================================

st.divider()

st.caption(
    "본 페이지는 식품의약품안전처 공개 API를 활용한 정보 검색용입니다. "
    "실제 의약품의 사용 여부와 복용 방법은 의료진 또는 약사에게 확인하세요."
)
```
