from fastapi import APIRouter, HTTPException
from app.schemas.note import NoteCreate, NoteOut
from app.services.notes_service import create_note, get_notes, get_note, delete_note

router = APIRouter()


@router.post("/", response_model=NoteOut)
def create(note: NoteCreate):
    return create_note(note)


@router.get("/", response_model=list[NoteOut])
def list_notes():
    return get_notes()


@router.get("/{note_id}", response_model=NoteOut)
def read(note_id: int):
    note = get_note(note_id)
    if not note:
        raise HTTPException(404, "Not found")
    return note


@router.delete("/{note_id}")
def remove(note_id: int):
    deleted = delete_note(note_id)
    if not deleted:
        raise HTTPException(404, "Not found")
    return {"ok": True}
