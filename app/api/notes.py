from fastapi import APIRouter, HTTPException, Depends
from app.schemas.note import NoteCreate, NoteOut
from app.services.notes_service import create_note, get_notes, get_note, delete_note
from app.db.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=NoteOut)
def create(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note)


@router.get("/", response_model=list[NoteOut])
def list_notes(db: Session = Depends(get_db)):
    return get_notes(db)


@router.get("/{note_id}", response_model=NoteOut)
def read(note_id: int, db: Session = Depends(get_db)):
    note = get_note(db, note_id)
    if not note:
        raise HTTPException(404, "Not found")
    return note


@router.delete("/{note_id}")
def remove(note_id: int, db: Session = Depends(get_db)):
    deleted = delete_note(db, note_id)
    if not deleted:
        raise HTTPException(404, "Not found")
    return {"ok": True}
