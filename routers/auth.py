from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import SessionLocal

from app.schemas.auth import RegisterSchema
from app.schemas.auth import LoginSchema

from app.services.auth_service import register_user
from app.services.auth_service import login_user

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
    return register_user(
        db,
        data.username,
        data.email,
        data.password
    )


@router.post("/login")
def login(
    data: LoginSchema,
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        data.email,
        data.password
    )