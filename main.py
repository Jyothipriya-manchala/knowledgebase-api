from fastapi import FastAPI

app = FastAPI(title="Knowledgebase API")

@app.get("/health")
def health():
    return {"status" : "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message" : f"hello {name}"}

@app.get("/add")
def add(a :  int, b : int):
    return {"sum": a+b}

@app.get("/search")
def search(keyword: str, limit : int = 10):
    return { "keyword" : keyword, "limit" : limit}