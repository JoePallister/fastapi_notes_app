from app.db.memory import notes, next_id


def create_note(note):
    global next_id

    new_note = {"id": next_id, "title": note.title, "content": note.content}

    notes.append(new_note)
    next_id += 1
    return new_note


def get_notes():
    return notes


def get_note(note_id: int):
    return next((n for n in notes if n["id"] == note_id), None)


def delete_note(note_id: int):
    for i, n in enumerate(notes):
        if n["id"] == note_id:
            del notes[i]
            return True
    return False
