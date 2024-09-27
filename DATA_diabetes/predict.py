import json
import requests


def predict_diabetes(BMI, Age, Glucose):
    url = 'http://127.0.0.1:5000/diabetes/v1/predict'
    # Chuyển đổi các giá trị nhập thành số
    try:
        BMI = float(BMI)
        Age = float(Age)
        Glucose = float(Glucose)
    except ValueError:
        print("Error: Please enter valid numerical values for BMI, Age, and Glucose.")
        return {}

    data = {"BMI": BMI, "Age": Age, "Glucose": Glucose}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}

    try:
        response = requests.post(url, data=data_json, headers=headers)

        # Kiểm tra mã trạng thái phản hồi
        if response.status_code == 200:
            result = json.loads(response.text)
            return result
        else:
            print("Error:", response.status_code, response.text)
            return {}
    except requests.RequestException as e:
        print("Request failed:", str(e))
        return {}


if __name__ == "__main__":
    BMI = input('BMI? ')
    Age = input('Age? ')
    Glucose = input('Glucose? ')

    # Gửi yêu cầu dự đoán
    predictions = predict_diabetes(BMI, Age, Glucose)

    # In dữ liệu phản hồi để kiểm tra cấu trúc
    print("API response:", predictions)

    # Xử lý dự đoán và độ tin cậy
    if 'prediction' in predictions:
        print("Diabetic" if predictions["prediction"] == 1 else "Not Diabetic")
        print("Confidence: " + predictions.get("confidence", "N/A") + "%")
    else:
        print("Prediction not found in response.")
