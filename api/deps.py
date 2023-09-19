from typing import Generator

import firebase_admin
from db.session import SessionLocal
from fastapi import Depends, HTTPException, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth, credentials

cred = credentials.Certificate("./core/lil_pro_account_key.json")
firebase_admin.initialize_app(cred)


def get_current_user(
    res: Response,
    cred: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> dict:
    """認証を行い、デコードされたトークンを返す。

    この関数はHTTP Bearer認証を使用して認証を行います。
    認証に成功した場合は、デコードされたJWTトークン（辞書型）を返します。
    認証に失敗した場合は、HTTP 401エラーを返します。

    Args:
        res (Response): FastAPIレスポンスオブジェクト。カスタムヘッダーを追加するために使用されます。
        cred (HTTPAuthorizationCredentials, optional): Bearer認証情報。デフォルトでは、HTTPBearer依存関数から取得されます。

    Raises:
        HTTPException: Bearer認証情報が提供されていない場合、HTTP 401エラーを発生させます。
        HTTPException: 提供された認証情報が無効な場合、HTTP 401エラーを発生させます。

    Returns:
        dict: デコードされたJWTトークン。通常はユーザー情報と各種クレームを含む辞書。
    """
    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={"WWW-Authenticate": 'Bearer realm="auth_required"'},
        )
    try:
        decoded_token = auth.verify_id_token(cred.credentials)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
            headers={"WWW-Authenticate": 'Bearer error="invalid_token"'},
        )
    res.headers["WWW-Authenticate"] = 'Bearer realm="auth_required"'

    uid = decoded_token.get("uid")
    if not uid:
        raise HTTPException(status_code=401, detail="Could not retrieve user ID.")

    return decoded_token


def get_db() -> Generator:
    """DB接続を行う

    Yields:
        Generator: DB接続
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
