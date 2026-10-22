```python
import streamlit as st
import requests

# 식품의약품안전처 의약품 제품 허가정보 API
BASE_URL = (
    "https://apis.data.go.kr/"
    "1471000/DrugPrdtPrmsnInfoService08"
)

SEARCH_URL = f"{BASE_URL}/getDrugPrdtMcpnDtlInq08"

st.title("💊 의약품 주성분 상세정보 검색")
st.write("식품의약품안전처 의약품 제품 허가정보 API 활용")

st.info(
    "의약품의 주성분 관련 공개 정보를 조회합니다. "
    "검색 결과는 의약품의 복용이나 처방을 위한 권고가 아닙니다."
)


def search_medicine_ingredients(drug_name):
    # Streamlit Cloud의 Secrets에서 인증키 읽기
    api_key = st.secrets.get("MFDS_API_KEY")

    if not api_key:
        st.error(
            "API 인증키를 찾을 수 없습니다. "
            "Streamlit Cloud의 Settings → Secrets를 확인해 주세요."
        )
        return None

    params = {
        "serviceKey": api_key,
        "type": "json",
        "pageNo": 1,
        "numOfRows": 10,
        "item_name": drug_name,
    }

    try:
        response = requests.get(
            SEARCH_URL,
            params=params,
            timeout=20,
        )

        if response.status_code != 200:
            st.error(f"API 요청 실패: HTTP {response.status_code}")
            return None

        # API가 JSON 형식으로 응답하는지 확인
        try:
            data = response.json()
        except ValueError:
            st.error(
                "서버 응답이 JSON 형식이 아닙니다. "
                "인증키와 API 응답 형식을 확인해 주세요."
            )
            return None

        # 일반적인 공공데이터 API 응답 구조 확인
        response_data = data.get("response", data)
        header = response_data.get("header", {})
        body = response_data.get("body", {})

        result_code = str(header.get("resultCode", ""))
        if result_code and result_code not in ("00", "0"):
            st.error(
                "API 오류: "
                + str(header.get("resultMsg", "원인을 확인할 수 없습니다."))
            )
            return None

        items = body.get("items", [])

        # API에 따라 items가 딕셔너리로 반환될 수 있음
        if isinstance(items, dict):
            items = items.get("item", items)

        if isinstance(items, dict):
            items = [items]

        if not isinstance(items, list):
            return []

        return items

    except requests.exceptions.Timeout:
        st.error("API 응답 시간이 초과되었습니다. 다시 시도해 주세요.")
        return None

    except requests.exceptions.RequestException:
        st.error("API 서버에 연결하지 못했습니다. 잠시 후 다시 시도해 주세요.")
        return None


drug_name = st.text_input("검색할 의약품명을 입력하세요:")

if st.button("검색하기"):
    if not drug_name.strip():
        st.warning("의약품명을 입력해주세요.")
    else:
        with st.spinner("식약처 데이터를 검색하고 있습니다..."):
            items = search_medicine_ingredients(drug_name.strip())

        if items is not None:
            if items:
                st.success(f"검색 결과 {len(items)}건")

                for item in items:
                    with st.expander(
                        item.get("ITEM_NAME", "의약품명 정보 없음"),
                        expanded=True,
                    ):
                        st.write(
                            "**의약품명:**",
                            item.get("ITEM_NAME", "정보 없음"),
                        )
                        st.write(
                            "**주성분명:**",
                            item.get("MCPN_NM", "정보 없음"),
                        )
                        st.write(
                            "**함량:**",
                            item.get("MCPN_CPCT", "정보 없음"),
                        )
                        st.write(
                            "**단위:**",
                            item.get("MCPN_CPCT_UNIT", "정보 없음"),
                        )
                        st.write(
                            "**성분코드:**",
                            item.get("MCPN_CD", "정보 없음"),
                        )
            else:
                st.warning(
                    "검색 결과가 없습니다. "
                    "API의 검색 조건과 응답 구조를 확인해 주세요."
                )
```
