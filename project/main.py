from fastapi import FastAPI
from database import engine,SessionLocal
from models import Note
from schemas import Note as NoteCreate

app =FastAPI()

@app.get("/")

def home():
    return {"message":"welcome home"}

@app.post("/notes")
def create_note(note: NoteCreate):
    db = SessionLocal()
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    return {"message": "Note created successfully", "note": new_note}

@app.get("/notes")
def get_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    return {"notes": notes}
    
Note.metadata.create_all(bind=engine)