from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import requests

app = Flask(__name__)

# Tải scaler và mô hình từ đĩa
scaler = pickle.load(open('scaler.sav', 'rb'))
loaded_model = pickle.load(open('knn_model.sav', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    percent10 = float(request.form['percent10'])
    percent20 = float(request.form['percent20'])
    percent20_1 = float(request.form['percent20_1'])

    # Dữ liệu đầu vào
    sample_data = np.array([[percent10, percent20, percent20_1]])

    # Normalization dữ liệu đầu vào
    sample_data_scaled = scaler.transform(sample_data)

    # Dự đoán
    prediction = loaded_model.predict(sample_data_scaled)

    # Dự đoán đã nằm trên thang điểm gốc
    prediction_score = round(prediction[0], 2)

    return render_template('result.html', predicted_score=prediction_score)


if __name__ == '__main__':
    app.run(debug=True)
