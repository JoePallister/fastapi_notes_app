from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import notes
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
