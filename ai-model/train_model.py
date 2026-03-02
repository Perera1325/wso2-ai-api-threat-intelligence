import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load training data
df = pd.read_csv("ai-model/training_data.csv")

# Drop user_id (not used in training)
X = df.drop(columns=["user_id"])

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Isolation Forest
model = IsolationForest(
    n_estimators=150,
    contamination=0.15,
    random_state=42
)

model.fit(X_scaled)

# Save model and scaler
joblib.dump(model, "ai-model/anomaly_detector.pkl")
joblib.dump(scaler, "ai-model/scaler.pkl")

print("Model trained and saved successfully.")