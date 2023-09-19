from pydantic import BaseModel
from typing import List

class ClosetBase(BaseModel):
    name: str


class ClosetCreate(ClosetBase):
    pass


class ClosetUpdate(ClosetBase):
    pass

class ClosetDelete(BaseModel):
    closet_ids: List[str]


class ClosetInDBBase(ClosetBase):
    id: str
    name: str
    user_id: str

    model_config = {"from_attributes": True}


class Closet(ClosetInDBBase):
    pass
