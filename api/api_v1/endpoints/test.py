import models
from api import deps
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/test")
async def test(db: Session = Depends(deps.get_db)) -> str:
    user = db.query(models.User).first()
    return user.id
