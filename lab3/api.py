from flask import Flask, request, jsonify
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"answer":"pong"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = data.get("features")
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)

    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
