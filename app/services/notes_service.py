from sqlalchemy.orm import Session
from app.schemas.note import NoteCreate
from app.models.note import Note


def create_note(db: Session, note: NoteCreate):
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_notes(db: Session):
    return db.query(Note).all()


def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()


def delete_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        return False

    db.delete(note)
    db.commit()
    return True
