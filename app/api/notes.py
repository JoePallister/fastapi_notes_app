from typing_extensions import Annotated

from fastapi import APIRouter, HTTPException, Depends
from app.schemas.note import NoteCreate, NoteOut
from app.services.notes_service import create_note, get_notes, get_note, delete_note
from app.db.deps import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.deps import get_current_user

CurrentUser = Annotated[
    User,
    Depends(get_current_user),
]

router = APIRouter()

# This is attaching metadata to the Session type
# FastAPI is looking for specific annotations, e.g. Depends
# when it finds that it knows the is a dependency and will inject it
DBSession = Annotated[Session, Depends(get_db)]

NOT_FOUND_RESPONSE = {404: {"description": "Resource not found"}}


@router.post("/", response_model=NoteOut)
def create(note: NoteCreate, db: DBSession, user: CurrentUser):
    return create_note(db, note, user)


@router.get("/", response_model=list[NoteOut])
def list_notes(db: DBSession, user: CurrentUser):
    return get_notes(db, user)


@router.get("/{note_id}", response_model=NoteOut, responses=NOT_FOUND_RESPONSE)
def read(note_id: int, db: DBSession, user: CurrentUser):
    note = get_note(db, note_id, user)
    if not note:
        raise HTTPException(404, "Not found")
    return note


@router.delete("/{note_id}", responses=NOT_FOUND_RESPONSE)
def remove(note_id: int, db: DBSession, user: CurrentUser):
    deleted = delete_note(db, note_id, user)
    if not deleted:
        raise HTTPException(404, "Not found")
    return {"ok": True}
