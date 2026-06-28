from sqlalchemy.orm import Session
from app.schemas.note import NoteCreate
from app.models.note import Note
from app.models.user import User


def create_note(db: Session, note: NoteCreate, user: User):
    db_note = Note(title=note.title, content=note.content, owner_id=user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_notes(db: Session, user: User):
    return db.query(Note).filter(Note.owner_id == user.id).all()


def get_note(db: Session, note_id: int, user: User):
    return (
        db.query(Note)
        .filter(Note.id == note_id)
        .filter(Note.owner_id == user.id)
        .first()
    )


def delete_note(db: Session, note_id: int, user: User):
    note = (
        db.query(Note)
        .filter(Note.id == note_id)
        .filter(Note.owner_id == user.id)
        .first()
    )
    if not note:
        return False

    db.delete(note)
    db.commit()
    return True
