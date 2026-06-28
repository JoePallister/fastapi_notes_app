from app.services.auth_service import create_user
import app.models
from app.auth.passwords import verify_password


def test_create_user(db):
    user = create_user(db, "alice", "password123")

    assert user.id is not None
    assert user.username == "alice"


def test_password_hashing(db):
    user = create_user(db, "alice", "password123")
    assert user.password_hash != "password123"
    assert verify_password("password123", user.password_hash)
