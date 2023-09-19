from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name: str


class UserInDBBase(UserBase):
    id: str

    model_config = {"from_attributes": True}


class User(UserInDBBase):
    pass
