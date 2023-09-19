from typing import Optional

from crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from models.user import User
from schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create_with_uid_and_display_name(
        self,
        db: Session,
        *,
        uid: str,
        obj_in: UserCreate,
        display_name: Optional[str] = None
    ) -> User:
        """FirebaseのユーザーIDとディスプレイネームを使用してユーザーを作成する

        Args:
        db (Session): DBセッション
            uid (str): FirebaseのユーザーID
            obj_in (UserCreate): ユーザー情報
            display_name (Optional[str], optional): ディスプレイネーム. Defaults to None.

        Returns:
            User: 作成されたユーザー
        """
        existing_user = self.get(db, id=uid)
        if existing_user:
            return existing_user  # 既存のユーザーがいればそれを返す

        user_data = jsonable_encoder(obj_in)
        if display_name:
            user_data["name"] = display_name  # ディスプレイネームを使用

        db_user = User(id=uid, **user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user = CRUDUser(User)
