import requests
import base64
import os

# --- Racing API Credentials ---
USERNAME = os.getenv("API_USERNAME", "2cYS43oV1US3OelcXJY4Oxbv")
PASSWORD = os.getenv("API_PASSWORD", "6lSMkoJtwuEna7RRb3Q5GhnN")

# --- Encode for Basic Auth ---
credentials = f"{USERNAME}:{PASSWORD}"
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

# --- Example API Call ---
def get_today_races():
    url = "https://api.theracingapi.com/v1/races?date=today"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("✅ Connected to Racing API")
        data = response.json()
        for race in data[:5]:  # limit to first 5
            print(f"🏇 {race['course']} - {race['time']} - {race['name']}")
    else:
        print(f"❌ API Error: {response.status_code} - {response.text}")

# --- Run it ---
if __name__ == "__main__":
    get_today_races()
