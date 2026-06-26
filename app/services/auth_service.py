from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.passwords import hash_password


def create_user(db: Session, username: str, password: str):
    user = User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
