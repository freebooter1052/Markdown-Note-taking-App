from fastapi import FastAPI
from database import engine,SessionLocal
from models import Note
from schemas import Note as NoteCreate
from fastapi import UploadFile, File
import markdown
import language_tool_python

tool = language_tool_python.LanguageTool(
    'en-US'
)

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

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(content)
    return {"filename": file.filename, "content_type": file.content_type}
@app.get("/notes/{id}/html")
def render_notes(id:int):
    db = SessionLocal()
    note = db.query(Note).filter(Note.id == id).first()
    html =markdown.markdown(note.content)
    return {"title": note.title, "html_content": html}
@app.post("/grammar")
def grammar(text:str):

    matches = tool.check(text)

    return [
        {
            "message": m.message,
            "suggestions": m.replacements
        }
        for m in matches
    ]
Note.metadata.create_all(bind=engine)