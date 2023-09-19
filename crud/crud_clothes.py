from typing import Optional

from crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from models.clothes import Clothes
from schemas.clothes import ClothesCreate, ClothesUpdate
from sqlalchemy.orm import Session
from functions.get_img_path import get_img_path


class CRUDClothes(CRUDBase[Clothes, ClothesCreate, ClothesUpdate]):
    def create_with_uid_closet_id(
        self,
        db: Session,
        *,
        uid: str,
        closet_id: str,
        obj_in: ClothesCreate,
    ) -> Clothes:
        """ユーザIDとクローゼットIDを使用して服を作成する

        Args:
            db (Session): DBセッション
            uid (str): ユーザID
            closet_id (str): クローゼットID
            obj_in (ClothesCreate): 服の情報

        Returns:
            Clothes: 服
        """
        db_obj = Clothes(
            **obj_in.model_dump(),
            img_path=get_img_path(obj_in.shop_url),
            closet_id=closet_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_closet_id(
        self,
        db: Session,
        *,
        closet_id: str,
    ) -> Optional[Clothes]:
        """クローゼットIDを使用してクローゼットを取得する

        Args:
            db (Session): DBセッション
            closet_id (str): クローゼットID

        Returns:
            Optional[Closet]: クローゼット
        """
        return db.query(Clothes).filter(Clothes.closet_id == closet_id).all()


clothes = CRUDClothes(Clothes)
