import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITLAB_TOKEN")

url = "https://gitlab.com/api/v4/code_suggestions/completions"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Hum Duo ko ek aisi bait (chara) daal rahe hain jisko wo reject kar hi nahi sakta:
chara = """# FAILED CI/CD ERROR LOG:
# TypeError: unsupported operand type(s) for -: 'int' and 'str'
# 
# BUGGY PYTHON CODE:
# def add(a, b):
#     return a - b
#
# SURGICAL CORRECTION (PURE PYTHON):
def add("""

payload = {
    "current_file": {
        "file_name": "auto_healer.py",
        "content_above_cursor": chara,
        "content_below_cursor": ""
    }
}

print("📡 Knocking on GitLab Duo 'Code Suggestions' VIP Door...")
response = requests.post(url, headers=headers, json=payload)

print(f"\nHTTP Response Code: {response.status_code}")
print("-" * 40)
print("RAW DUO BRAIN JSON OUTPUT:")
print("-" * 40)
print(response.text)