import models
from db.session import SessionLocal


def seed_clothes():
    """clothesを作成する関数"""
    print("=====================================")
    print("     clothesを作成します...")

    with SessionLocal() as db:
        result = (
            db.query(models.Closet.user_id, models.Closet.id)
            .group_by(models.Closet.user_id, models.Closet.id)
            .all()
        )
        grouped_by_user = {}

        for user_id, closet_id in result:
            if user_id not in grouped_by_user:
                grouped_by_user[user_id] = []
            grouped_by_user[user_id].append(closet_id)

        # 各user_idに対して、そのuser_idが所有する各closet_idごとに2つのclothesを作成
        for user_index, (user_id, closet_ids) in enumerate(
            grouped_by_user.items(), start=1
        ):
            for closet_index, closet_id in enumerate(closet_ids, start=1):
                for i in range(1, 3):  # 各closet_idに対して2つのclothesを作成
                    clothes_name = f"tester{user_index}_clothes{closet_index}_{i}"
                    db.add(
                        models.Clothes(
                            name=clothes_name,
                            shop_url="http://www.example.com/",
                            img_path="https://1.bp.blogspot.com/-seNH6_bImIs/XxU0amXx0nI/AAAAAAABaKo/16b2Byz0hIMKWg-336NpZm9Wd1ngaQSgACNcBGAsYHQ/s450/fashion_blouson_jumper_man.png",
                            description="test",
                            closet_id=closet_id,
                        )
                    )

        db.commit()

    print("     clothesの作成が完了しました！")
    print("=====================================")
