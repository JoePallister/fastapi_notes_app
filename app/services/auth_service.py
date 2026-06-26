from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.passwords import hash_password, verify_password
from fastapi import HTTPException


def create_user(db: Session, username: str, password: str):
    user = User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(401)

    if not verify_password(password, user.password_hash):
        raise HTTPException(401)

    return user
