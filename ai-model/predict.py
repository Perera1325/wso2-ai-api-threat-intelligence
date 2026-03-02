import sys
import pandas as pd
import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "ai-model", "training_data.csv")
model_path = os.path.join(BASE_DIR, "ai-model", "anomaly_detector.pkl")
scaler_path = os.path.join(BASE_DIR, "ai-model", "scaler.pkl")

user_id = sys.argv[1]

df = pd.read_csv(data_path)

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

user_data = df[df["user_id"] == user_id]

if user_data.empty:
    print("USER_NOT_FOUND")
    sys.exit()

X = user_data.drop(columns=["user_id"])
X_scaled = scaler.transform(X)

# Get anomaly prediction
prediction = model.predict(X_scaled)

# Get anomaly score (the lower, the more abnormal)
score = model.decision_function(X_scaled)[0]

# Convert to 0–100 risk score
risk_score = int((1 - score) * 50 + 50)

if risk_score < 0:
    risk_score = 0
if risk_score > 100:
    risk_score = 100

if risk_score >= 75:
    status = "HIGH_RISK"
elif risk_score >= 50:
    status = "MEDIUM_RISK"
else:
    status = "LOW_RISK"

confidence = round(abs(score), 2)

print(f"{risk_score}|{status}|{confidence}")