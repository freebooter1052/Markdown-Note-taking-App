# Markdown-Note-taking-App

A lightweight FastAPI project for creating, storing, and rendering Markdown notes. The app exposes REST endpoints to create notes, list notes, render a note's Markdown as HTML, upload Markdown files, and run grammar checks. It is designed as a learning-friendly project that demonstrates:

Project reference: https://roadmap.sh/projects/markdown-note-taking-app

- Basic FastAPI routing and request handling
- File uploads via `UploadFile`
- Markdown parsing and HTML rendering
- Simple grammar checks using `language-tool-python`
- Database-backed CRUD with SQLAlchemy

## Features

- Create notes with a title and Markdown content
- List all stored notes
- Render a note's Markdown into HTML
- Upload Markdown files to the server
- Grammar checking endpoint for text

## Project Structure

```
project/
	main.py        FastAPI app and routes
	database.py    SQLAlchemy engine and session setup
	models.py      SQLAlchemy models
	schemas.py     Pydantic schemas
	uploads/       Uploaded files land here
```

## Requirements

- Python 3.9+ recommended
- FastAPI
- Uvicorn
- SQLAlchemy
- Markdown
- language-tool-python

## Installation

1) Clone the repo and create a virtual environment

```
python -m venv venv
```

2) Activate the environment

- Windows (PowerShell)

```
venv\Scripts\Activate.ps1
```

- macOS/Linux

```
source venv/bin/activate
```

3) Install dependencies

```
pip install fastapi uvicorn sqlalchemy markdown language-tool-python
```

## Run the App

From the `project` directory:

```
uvicorn main:app --reload
```

Open your browser at:

```
http://127.0.0.1:8000
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create a Note

```
POST /notes
```

Example JSON body:

```
{
	"title": "My First Note",
	"content": "# Hello\nThis is **Markdown**."
}
```

### List Notes

```
GET /notes
```

### Render Note as HTML

```
GET /notes/{id}/html
```

Example:

```
http://127.0.0.1:8000/notes/1/html
```

### Upload a Markdown File

```
POST /upload
```

Use a multipart form with a `file` field.

### Grammar Check

```
POST /grammar
```

Example query:

```
http://127.0.0.1:8000/grammar?text=This%20are%20bad%20grammar
```

## FastAPI Tutorial Guide (Quick Start)

This project follows common FastAPI patterns. If you are new to FastAPI, use the steps below to understand how it works in this repo.

1) Create the app instance

In `main.py`:

```
app = FastAPI()
```

2) Add routes with decorators

```
@app.get("/")
def home():
		return {"message": "welcome home"}
```

3) Use Pydantic schemas for input

The `Note` schema in `schemas.py` defines what input fields are required. FastAPI automatically validates the request body.

4) Connect to the database

`database.py` creates an SQLAlchemy engine and a session factory. In each route, a new session is opened:

```
db = SessionLocal()
```

5) Query and return data

Example from the HTML render endpoint:

```
note = db.query(Note).filter(Note.id == id).first()
html = markdown.markdown(note.content)
```

6) Explore with the Swagger UI

Open `http://127.0.0.1:8000/docs` and try each endpoint directly from the browser.

## Common Issues

- If an endpoint is not found, confirm the route starts with a leading `/`.
- If `note` is `None`, create a note first and retry using a valid ID.
- If grammar checks are slow, `language-tool-python` may be downloading data the first time it runs.

## Next Steps

- Add delete and update endpoints
- Add HTML sanitization before returning rendered Markdown
- Add a front-end for note editing
