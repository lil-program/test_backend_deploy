from typing import Optional

from crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from models.closet import Closet
from schemas.closet import ClosetCreate, ClosetUpdate
from sqlalchemy.orm import Session


class CRUDCloset(CRUDBase[Closet, ClosetCreate, ClosetUpdate]):
    def create_with_uid(
        self,
        db: Session,
        *,
        uid: str,
        obj_in: ClosetCreate,
    ) -> Closet:
        """ユーザーIDを使用してクローゼットを作成する

        Args:
            db (Session): DBセッション
            uid (str): ユーザーID
            obj_in (ClosetCreate): クローゼット情報

        Returns:
            Closet: 作成されたクローゼット
        """
        closet_data = jsonable_encoder(obj_in)
        db_closet = Closet(user_id=uid, **closet_data)
        db.add(db_closet)
        db.commit()
        db.refresh(db_closet)
        return db_closet

    def get_by_id_and_user(
        self,
        db: Session,
        *,
        closet_id: str,
        user_id: str,
    ) -> Optional[Closet]:
        """ユーザーIDとクローゼットIDを使用してクローゼットを取得する

        Args:
            db (Session): DBセッション
            closet_id (str): クローゼットID
            user_id (str): ユーザーID

        Returns:
            Optional[Closet]: クローゼット
        """
        return (
            db.query(Closet)
            .filter(Closet.id == closet_id, Closet.user_id == user_id)
            .first()
        )
    
    def get_multi_by_user(
        self,
        db: Session,
        *,
        user_id: str,
    ) -> list[Closet]:
        """ユーザーIDを使用してクローゼットを取得する

        Args:
            db (Session): DBセッション
            user_id (str): ユーザーID

        Returns:
            list[Closet]: クローゼットのリスト
        """
        return db.query(Closet).filter(Closet.user_id == user_id).all()


closet = CRUDCloset(Closet)
