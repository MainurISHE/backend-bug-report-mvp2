from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.models import User

from app.schemas.auth import RegisterSchema

from app.utils.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/register")
def register(
    data: RegisterSchema,
    db: Session = Depends(get_db)
):
    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "User created",
        "user_id": user.id
    }