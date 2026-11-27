from database import Base, engine
import models
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Knowledgebase API")

# @app.get("/health")
# def health():
#     return {"status" : "ok"}

# @app.get("/hello/{name}")
# def hello(name: str):
#     return {"message" : f"hello {name}"}

# @app.get("/add")
# def add(a :  int, b : int):
#     return {"sum": a+b}

# @app.get("/search")
# def search(keyword: str, limit : int = 10):
#     return { "keyword" : keyword, "limit" : limit}



class NoteCreate(BaseModel):
    title : str
    content : str

class Note(BaseModel):
    id : int
    title : str
    content : str

notes : list[Note] = []
next_id = 1

@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate):
    global next_id
    #print(next_id)
    new_note = Note(id = next_id, title = note.title, content = note.content)
    notes.append(new_note)
    next_id += 1
    return new_note

@app.get("/notes", response_model=list[Note])
def list_notes():
    return notes

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id : int):
    for note in notes:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail = "Note not found")

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id : int, note : NoteCreate):
    for index, existing_note in enumerate(notes):
        if existing_note.id == note_id:
            updated_note = Note(id = note_id, title = note.title, content = note.content)
            notes[index] = updated_note
            return updated_note
    raise HTTPException(status_code=404, detail= "Note not found")

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id : int):
    for index, existing_note in enumerate(notes):
        if existing_note.id == note_id:
            notes.pop(index)
            return
    raise HTTPException(status_code=404, detail= "Note not found")
