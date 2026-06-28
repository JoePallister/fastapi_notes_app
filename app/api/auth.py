from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from app.auth.deps import get_current_user
from app.auth.passwords import create_token
from app.db.deps import get_db
from app.services.auth_service import create_user, login_user
from app.schemas.auth import LoginRequest
from app.models.user import User

router = APIRouter()

DBSession = Annotated[Session, Depends(get_db)]

CurrentUser = Annotated[
    User,
    Depends(get_current_user),
]


# FastAPI is looking for specific annotations, e.g. Depends
# If it doesn't see those then it assumes the data must come from the request
# That's how it knows data in the request body and db is not
@router.post("/register")
def register(db: DBSession, data: LoginRequest):
    user = create_user(db, username=data.username, password=data.password)
    return {"username": user.username}


@router.post("/login")
def login(db: DBSession, data: LoginRequest):
    user = login_user(db, username=data.username, password=data.password)
    return {"access_token": create_token(user.id), "token_type": "bearer"}


@router.get("/me")
def me(user: CurrentUser):
    return {"username": user}
