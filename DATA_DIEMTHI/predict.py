import requests
import json

# Địa chỉ của API
api_url = 'http://127.0.0.1:5000/predict'

# Dữ liệu mẫu để gửi yêu cầu
data = {
    'percent10': 8.0,
    'percent20': 9.0,
    'percent20_1': 9.0
}

# Gửi yêu cầu POST đến API
response = requests.post(api_url, json=data)

# Kiểm tra trạng thái phản hồi
if response.status_code == 200:
    result = response.json()
    print(f"Predicted Score: {result['predicted_score']}")
else:
    print(f"Error: {response.status_code}")
