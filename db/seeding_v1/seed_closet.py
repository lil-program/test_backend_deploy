import os

import models
from db.session import SessionLocal
from dotenv import load_dotenv

load_dotenv(override=True)


def seed_closet():
    """closetを作成する"""
    print("=====================================")
    print("     closetを作成します...")

    with SessionLocal() as db:
        db.add_all(
            [
                models.Closet(
                    name="tester1_closet_1",
                    user_id=os.environ.get("TESTER1_UID"),
                ),
                models.Closet(
                    name="tester1_closet_2",
                    user_id=os.environ.get("TESTER1_UID"),
                ),
                models.Closet(
                    name="tester2_closet_1",
                    user_id=os.environ.get("TESTER2_UID"),
                ),
                models.Closet(
                    name="tester2_closet_2",
                    user_id=os.environ.get("TESTER2_UID"),
                ),
            ]
        )
        db.commit()

    print("     closetの作成が完了しました！")
    print("=====================================")
