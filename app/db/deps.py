from app.db.database import SessionLocal


# Yield will let the db be used before returning here to do db.close()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
