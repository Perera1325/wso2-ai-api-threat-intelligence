import json
import pandas as pd
from collections import Counter

def extract_features():
    with open("log-collector/api_logs.json") as f:
        logs = json.load(f)

    df = pd.DataFrame(logs)

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Aggregate per user
    features = []

    for user, group in df.groupby("user_id"):
        request_count = len(group)
        avg_response_time = group["response_time"].mean()
        unique_endpoints = group["api"].nunique()
        failed_ratio = len(group[group["status"] != 200]) / request_count

        features.append({
            "user_id": user,
            "request_count": request_count,
            "avg_response_time": avg_response_time,
            "unique_endpoints": unique_endpoints,
            "failed_ratio": failed_ratio
        })

    feature_df = pd.DataFrame(features)
    feature_df.to_csv("ai-model/training_data.csv", index=False)

    print("Feature dataset created successfully.")

if __name__ == "__main__":
    extract_features()