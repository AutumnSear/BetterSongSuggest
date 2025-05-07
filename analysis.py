import requests
import json

url = "https://scoresaber.com/api/leaderboards?ranked=true&page=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=True))  # Pretty print with full Unicode
else:
    print("Error:", response.status_code)
