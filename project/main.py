from fastapi import FastAPI
from database import engine
from models import Note
app =FastAPI()

@app.get("/")

def home():
    return {"message":"welcome home"}

Note.metadata.create_all(bind=engine)