import crud
import schemas
from api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create", response_model=schemas.User)
async def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    cred: dict = Depends(deps.get_current_user),
) -> schemas.User:
    uid = cred.get("uid")
    display_name = cred.get("displayName", None)  # FirebaseからdisplayNameを取得

    if not uid:
        raise HTTPException(status_code=401, detail="Could not retrieve user ID.")

    existing_user = crud.user.get(db, id=uid)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")

    user = crud.user.create_with_uid_and_display_name(
        db=db, uid=uid, obj_in=user_in, display_name=display_name
    )

    return user


@router.get("/get_my_profile", response_model=schemas.User)
async def read_user_me(
    *, db: Session = Depends(deps.get_db), cred: dict = Depends(deps.get_current_user)
) -> schemas.User:
    user = crud.user.get(db, id=cred.get("uid"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@router.put("/update", response_model=schemas.User)
async def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserUpdate,
    cred: dict = Depends(deps.get_current_user),
) -> schemas.User:
    user = crud.user.get(db, id=cred.get("uid"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
