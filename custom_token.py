import requests
import json

from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv(override=True)

# FirebaseプロジェクトのAPIキー
API_KEY = os.environ.get("API_KEY")

# ユーザーのメールアドレスとパスワード
email = os.environ.get("TEST_MAIL")
password = os.environ.get("TEST_PASSWORD")

# IDトークンを取得するためのURL
url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

# ペイロードデータ
payload = json.dumps({
  "email": email,
  "password": password,
  "returnSecureToken": True
})

# HTTPリクエストを送信してIDトークンを取得
response = requests.post(url, data=payload, headers={"Content-Type": "application/json"})

# レスポンスからIDトークンを抽出
id_token = response.json().get("idToken")
print(id_token)