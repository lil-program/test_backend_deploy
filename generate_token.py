import requests
import json
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv(override=True)

# FirebaseプロジェクトのAPIキー
API_KEY = os.environ.get("API_KEY")

# ユーザー情報
user_info = {
    'TESTER1': {
        'email': os.environ.get("TESTER1_MAIL"),
        'password': os.environ.get("TESTER1_PASSWORD"),
    },
    'TESTER2': {
        'email': os.environ.get("TESTER2_MAIL"),
        'password': os.environ.get("TESTER2_PASSWORD"),
    }
}

# IDトークンを取得する関数
def get_id_token(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    payload = json.dumps({
      "email": email,
      "password": password,
      "returnSecureToken": True
    })
    response = requests.post(url, data=payload, headers={"Content-Type": "application/json"})
    return response.json().get("idToken")

print("=====================================")
print("          トークンの取得を開始")
print("=====================================")

for tester, info in user_info.items():
    id_token = get_id_token(info['email'], info['password'])
    print(f"-------- {tester} のIDトークン --------")
    print(id_token)
    print("-------------------------------------")

print("=====================================")
print("         トークンの取得が完了！")
print("=====================================")
