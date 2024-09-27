import pickle
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# --- Tên tệp của mô hình đã lưu ---
filename = 'diabetes.sav'

# --- Tải mô hình đã lưu ---
loaded_model = pickle.load(open(filename, 'rb'))


@app.route('/diabetes/v1/predict', methods=['POST'])
def predict():
    try:
        # --- Lấy các đặc trưng để dự đoán ---
        features = request.json
        if not features or not all(k in features for k in ["Glucose", "BMI", "Age"]):
            return jsonify({"error": "Invalid input"}), 400

        # --- Tạo danh sách các đặc trưng để dự đoán ---
        features_list = [features["Glucose"], features["BMI"], features["Age"]]

        # --- Dự đoán lớp ---
        prediction = loaded_model.predict([features_list])

        # --- Lấy xác suất dự đoán ---
        confidence = loaded_model.predict_proba([features_list])

        # --- Tạo phản hồi để trả về cho khách hàng ---
        response = {
            'prediction': int(prediction[0]),
            'confidence': str(round(np.amax(confidence[0]) * 100, 2))
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
