import json
import base64
import requests

with open("실감미디어_프로젝트\img.png", "rb") as f:
    img = base64.b64encode(f.read())

 # 본인의 APIGW Invoke URL로 치환
URL = "https://3sk7z245pt.apigw.ntruss.com/custom/v1/19163/dda94686f278db7812bbc62464f4832480be1258b6f36681dbb60a9488a3a2a8/general"
    
 # 본인의 Secret Key로 치환
KEY = "aVdDcnhZZ0ROcW1XSkNhQXNxQmlZSU5CZ3VPRmJ4c1E="
    
headers = {
    "Content-Type": "application/json",
    "X-OCR-SECRET": KEY
}
    
data = {
    "version": "V1",
    "requestId": "sample_id", # 요청을 구분하기 위한 ID, 사용자가 정의
    "timestamp": 0, # 현재 시간값
    "images": [
        {
            "name": "sample_image",
            "format": "png",
            "data": img.decode('utf-8')
        }
    ]
}
data = json.dumps(data)
response = requests.post(URL, data=data, headers=headers)
res = json.loads(response.text)

result = " ".join(res)
print(result)