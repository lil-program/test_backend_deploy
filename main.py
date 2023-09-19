from api.api_v1.api_router import api_router
from core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from termcolor import colored
from datetime import datetime

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

if settings.is_production():
    # 本番環境用の設定
    print(colored(f"{datetime.now()} - 本番環境設定を適用", 'red'))
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.PRODUCT_SEVER_DOMAIN],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
elif settings.is_development():
    # 開発環境用の設定
    print(colored(f"{datetime.now()} - 開発環境設定を適用", 'green'))
    app.add_middleware(
        CORSMiddleware,
        expose_headers=["*"],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
