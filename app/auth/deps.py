from typing import Annotated
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

from app.models.user import User
from app.db.deps import get_db
from sqlalchemy.orm import Session
from jose import JWTError, jwt

# Duplication here, should be refactored to avoid hardcoding the secret key and algorithm in multiple places.
SECRET_KEY = "dev-secret"
ALGORITHM = "HS256"

bearer_scheme = HTTPBearer()

users = []

Credentials = Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)]


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload["sub"])
    except JWTError:
        raise HTTPException(401, "Invalid token")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(401, "User not found")

    return user
