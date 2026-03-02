import json
import random
import datetime

APIS = ["/v1/payments", "/v1/users", "/v1/orders", "/v1/products"]
USERS = [f"U{i}" for i in range(1, 21)]

def generate_log_entry(user_id, abnormal=False):
    return {
        "user_id": user_id,
        "api": random.choice(APIS),
        "method": random.choice(["GET", "POST"]),
        "response_time": random.randint(50, 800 if abnormal else 300),
        "status": random.choice([200, 200, 200, 401, 403]) if abnormal else 200,
        "timestamp": datetime.datetime.now().isoformat()
    }

def generate_logs():
    logs = []

    # Normal behavior
    for _ in range(500):
        logs.append(generate_log_entry(random.choice(USERS)))

    # Abnormal behavior (scraping / abuse simulation)
    for _ in range(100):
        logs.append(generate_log_entry("U1", abnormal=True))

    with open("log-collector/api_logs.json", "w") as f:
        json.dump(logs, f, indent=4)

    print("Synthetic logs generated successfully.")

if __name__ == "__main__":
    generate_logs()