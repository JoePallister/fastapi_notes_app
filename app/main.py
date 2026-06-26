from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import notes

app = FastAPI()

app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
