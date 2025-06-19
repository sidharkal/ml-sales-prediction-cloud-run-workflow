from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return jsonify({"message": "Sales Prediction API is Running"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'predicted_sales': prediction[0]})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use PORT env var if set, else 8080
    print(f"Starting Flask app on port {port}...")
    app.run(host='0.0.0.0', port=port)


