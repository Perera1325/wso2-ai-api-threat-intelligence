import pandas as pd
import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "ai-model", "training_data.csv")
model_path = os.path.join(BASE_DIR, "ai-model", "anomaly_detector.pkl")
scaler_path = os.path.join(BASE_DIR, "ai-model", "scaler.pkl")

df = pd.read_csv(data_path)

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

results = []

for _, row in df.iterrows():
    user_id = row["user_id"]
    X = row.drop("user_id").values.reshape(1, -1)
    X_scaled = scaler.transform(X)

    score = model.decision_function(X_scaled)[0]
    risk_score = int((1 - score) * 50 + 50)

    risk_score = max(0, min(100, risk_score))

    if risk_score >= 75:
        status = "HIGH_RISK"
    elif risk_score >= 50:
        status = "MEDIUM_RISK"
    else:
        status = "LOW_RISK"

    results.append({
        "user": user_id,
        "risk_score": risk_score,
        "status": status
    })

result_df = pd.DataFrame(results)
result_df = result_df.sort_values(by="risk_score", ascending=False)

print(result_df.to_json(orient="records"))