import os

import models
from db.session import SessionLocal
from dotenv import load_dotenv

load_dotenv(override=True)


def seed_user():
    """ユーザーを作成する"""
    print("=====================================")
    print("     userを作成します...")

    with SessionLocal() as db:
        db.add_all(
            [
                models.User(
                    id=os.environ.get("TESTER1_UID"),
                    name="test_user_1",
                ),
                models.User(
                    id=os.environ.get("TESTER2_UID"),
                    name="test_user_2",
                ),
            ]
        )
        db.commit()

    print("     userの作成が完了しました！")
    print("=====================================")
