from sqlalchemy.orm import Session

from app.database.models import User

from app.utils.security import hash_password
from app.utils.security import verify_password
from app.utils.security import create_access_token


def register_user(
    db: Session,
    username: str,
    email: str,
    password: str
):
    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:
        return {
            "error": "User already exists"
        }

    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    token = create_access_token({
        "user_id": user.id
    })

    return {
        "message": "User created",
        "token": token
    }


def login_user(
    db: Session,
    email: str,
    password: str
):
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "error": "Invalid email or password"
        }

    valid_password = verify_password(
        password,
        user.password
    )

    if not valid_password:
        return {
            "error": "Invalid email or password"
        }

    token = create_access_token({
        "user_id": user.id
    })

    return {
        "message": "Login success",
        "token": token
    }