from app.services.auth_service import create_user
import app.models


def test_create_user(db):
    user = create_user(db, "alice", "password123")

    assert user.id is not None
    assert user.username == "alice"
    assert user.password_hash != "password123"
