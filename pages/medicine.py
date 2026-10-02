import requests
import json

# 공공데이터포털에서 발급받은 디코딩된 API 키 입력
API_KEY = "185a24e9e330b5a71ceb3495879128988532b7ecfd102cba636ae1c408a7450f"
BASE_URL = "https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList"

# 테스트용 의약품명
drug_name = "타이레놀"

# URL 직접 구성
url = f"{BASE_URL}?serviceKey={API_KEY}&type=json&itemName={drug_name}"

response = requests.get(url)

print("응답 코드:", response.status_code)

if response.status_code == 200:
    try:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as e:
        print("JSON 파싱 오류:", e)
        print("응답 텍스트:", response.text)
else:
    print("API 요청 실패:", response.text)
