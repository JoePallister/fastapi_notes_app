from fastapi import FastAPI
from app.api import notes

app = FastAPI()

app.include_router(notes.router, prefix="/notes", tags=["notes"])
