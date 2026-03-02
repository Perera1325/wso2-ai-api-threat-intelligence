import sys
import pandas as pd
import joblib
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct correct paths
data_path = os.path.join(BASE_DIR, "ai-model", "training_data.csv")
model_path = os.path.join(BASE_DIR, "ai-model", "anomaly_detector.pkl")
scaler_path = os.path.join(BASE_DIR, "ai-model", "scaler.pkl")

user_id = sys.argv[1]

df = pd.read_csv(data_path)

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

user_data = df[df["user_id"] == user_id]

if user_data.empty:
    print("User not found")
    sys.exit()

X = user_data.drop(columns=["user_id"])
X_scaled = scaler.transform(X)

prediction = model.predict(X_scaled)

if prediction[0] == -1:
    print("ANOMALOUS_BEHAVIOR_DETECTED")
else:
    print("NORMAL_BEHAVIOR")