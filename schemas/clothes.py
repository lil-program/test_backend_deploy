from typing import List, Optional

from pydantic import BaseModel


class ClothesBase(BaseModel):
    name: Optional[str]


class ClothesCreate(ClothesBase):
    shop_url: str


class ClothesUpdate(ClothesBase):
    name: str


class ClothesDelete(BaseModel):
    clothes_ids: List[str]


class ClothesInDBBase(ClothesBase):
    id: str
    name: Optional[str]
    shop_url: str
    img_path: str
    description: Optional[str]
    closet_id: str

    model_config = {"from_attributes": True}


class Clothes(ClothesInDBBase):
    pass
