import requests

API_KEY = "185a24e9e330b5a71ceb3495879128988532b7ecfd102cba636ae1c408a7450f"
BASE_URL = "https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList"

drug_name = "타이레놀"
url = f"{BASE_URL}?serviceKey={API_KEY}&type=json&itemName={drug_name}"

print("요청 URL:", url)

response = requests.get(url)

print("응답 코드:", response.status_code)

# 응답 본문을 그대로 출력 (JSON 파싱 실패해도 확인 가능)
print("응답 텍스트:")
print(response.text)
