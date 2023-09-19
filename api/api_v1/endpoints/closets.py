from typing import List

import crud
import schemas
from api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create", response_model=schemas.Closet)
async def create_closet(
    *,
    db: Session = Depends(deps.get_db),
    closet_in: schemas.ClosetCreate,
    cred: dict = Depends(deps.get_current_user),
) -> schemas.Closet:
    closet = crud.closet.create_with_uid(db=db, uid=cred.get("uid"), obj_in=closet_in)

    return closet


@router.get("/get_my_closets", response_model=list[schemas.Closet])
async def read_closets(
    *, db: Session = Depends(deps.get_db), cred: dict = Depends(deps.get_current_user)
) -> list[schemas.Closet]:
    closets = crud.closet.get_multi_by_user(db, user_id=cred.get("uid"))
    return closets


@router.put("/update/{closet_id}", response_model=schemas.Closet)
async def update_closet(
    *,
    closet_id: str,
    db: Session = Depends(deps.get_db),
    closet_in: schemas.ClosetUpdate,
    cred: dict = Depends(deps.get_current_user),
) -> schemas.Closet:
    # ここで特定のclosetをuidとcloset_idで検索し、存在しない場合はエラーを返す
    existing_closet = crud.closet.get_by_id_and_user(
        db, closet_id=closet_id, user_id=cred.get("uid")
    )
    if not existing_closet:
        raise HTTPException(status_code=404, detail="Closet not found.")

    # 更新処理
    closet = crud.closet.update(db, db_obj=existing_closet, obj_in=closet_in)

    return closet


@router.delete("/delete", response_model=List[schemas.Closet])
async def delete_closet(
    *,
    closet_ids: schemas.ClosetDelete,
    db: Session = Depends(deps.get_db),
    cred: dict = Depends(deps.get_current_user),
) -> List[schemas.Closet]:
    removed_closets = []

    for closet_id in closet_ids.closet_ids:
        existing_closet = crud.closet.get_by_id_and_user(
            db, closet_id=closet_id, user_id=cred.get("uid")
        )
        if not existing_closet:
            raise HTTPException(
                status_code=404, detail=f"Closet with ID {closet_id} not found."
            )

        removed_closet = crud.closet.remove(db, id=closet_id)
        removed_closets.append(removed_closet)

    return removed_closets


@router.get("/get/{closet_id}", response_model=schemas.Closet)
async def read_closet(
    *,
    closet_id: str,
    db: Session = Depends(deps.get_db),
    cred: dict = Depends(deps.get_current_user),
) -> schemas.Closet:
    # ここで特定のclosetをuidとcloset_idで検索し、存在しない場合はエラーを返す
    existing_closet = crud.closet.get_by_id_and_user(
        db, closet_id=closet_id, user_id=cred.get("uid")
    )
    if not existing_closet:
        raise HTTPException(status_code=404, detail="Closet not found.")

    return existing_closet
