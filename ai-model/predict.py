import sys
import pandas as pd
import joblib

user_id = sys.argv[1]

df = pd.read_csv("ai-model/training_data.csv")

model = joblib.load("ai-model/anomaly_detector.pkl")
scaler = joblib.load("ai-model/scaler.pkl")

user_data = df[df["user_id"] == user_id]

if user_data.empty:
    print("User not found")
    sys.exit()

X = user_data.drop(columns=["user_id"])
X_scaled = scaler.transform(X)

prediction = model.predict(X_scaled)

if prediction[0] == -1:
    print("⚠️ Anomalous Behavior Detected")
else:
    print("✅ Normal Behavior")