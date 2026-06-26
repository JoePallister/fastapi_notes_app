from typing import Annotated
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

bearer_scheme = HTTPBearer()

users = []

Credentials = Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)]


def get_current_user(
    credentials: Credentials,
):
    token = credentials.credentials  # already stripped of "Bearer "

    if token != "user1":
        raise HTTPException(401)

    return token
