import crud
import schemas
from api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create/{closet_id}", response_model=schemas.Clothes)
async def create_clothes(
    *,
    db: Session = Depends(deps.get_db),
    closet_id: str,
    clothes_in: schemas.ClothesCreate,
    cred: dict = Depends(deps.get_current_user),
) -> schemas.Clothes:
    # closet_idとuidでclosetを検索し、存在しない場合はエラーを返す
    existing_closet = crud.closet.get_by_id_and_user(
        db, closet_id=closet_id, user_id=cred.get("uid")
    )
    if not existing_closet:
        raise HTTPException(status_code=404, detail="Closet not found.")

    clothes = crud.clothes.create_with_uid_closet_id(
        db=db, uid=cred.get("uid"), closet_id=closet_id, obj_in=clothes_in
    )

    return clothes


@router.get("/get_my_clothes/{closet_id}", response_model=list[schemas.Clothes])
async def read_clothes(
    *,
    db: Session = Depends(deps.get_db),
    closet_id: str,
    cred: dict = Depends(deps.get_current_user),
) -> list[schemas.Clothes]:
    # closet_idとuidでclosetを検索し、存在しない場合はエラーを返す
    existing_closet = crud.closet.get_by_id_and_user(
        db, closet_id=closet_id, user_id=cred.get("uid")
    )
    if not existing_closet:
        raise HTTPException(status_code=404, detail="Closet not found.")

    clothes = crud.clothes.get_by_closet_id(db, closet_id=closet_id)
    return clothes


@router.put("/update/{clothes_id}", response_model=schemas.Clothes)
async def update_clothes(
    *,
    clothes_id: str,
    db: Session = Depends(deps.get_db),
    clothes_in: schemas.ClothesUpdate,
    cred: dict = Depends(deps.get_current_user),
) -> schemas.Clothes:
    # 特定のclothesをuidとclothes_idで検索し、存在しない場合はエラーを返す
    existing_clothes = crud.clothes.get(db, id=clothes_id)
    if not existing_clothes:
        raise HTTPException(status_code=404, detail="Clothes not found.")

    # closet_idとuidでclosetを検索し、存在しない場合はエラーを返す
    existing_closet = crud.closet.get_by_id_and_user(
        db, closet_id=existing_clothes.closet_id, user_id=cred.get("uid")
    )
    if not existing_closet:
        raise HTTPException(status_code=404, detail="Closet not found.")

    # 更新処理
    clothes = crud.clothes.update(db, db_obj=existing_clothes, obj_in=clothes_in)

    return clothes


@router.delete("/delete", response_model=list[schemas.Clothes])
async def delete_clothes(
    *,
    clothes_ids: schemas.ClothesDelete,
    db: Session = Depends(deps.get_db),
    cred: dict = Depends(deps.get_current_user),
) -> list[schemas.Clothes]:
    removed_clothes = []

    for clothes_id in clothes_ids.clothes_ids:
        existing_clothes = crud.clothes.get(db, id=clothes_id)
        if not existing_clothes:
            raise HTTPException(status_code=404, detail="Clothes not found.")

        # closet_idとuidでclosetを検索し、存在しない場合はエラーを返す
        existing_closet = crud.closet.get_by_id_and_user(
            db, closet_id=existing_clothes.closet_id, user_id=cred.get("uid")
        )
        if not existing_closet:
            raise HTTPException(status_code=404, detail="Closet not found.")

        removed_clothes.append(existing_clothes)
        crud.clothes.remove(db, id=clothes_id)

    return removed_clothes
