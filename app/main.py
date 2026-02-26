from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello World"}

@app.get('/')
def health():
    return {"status": "ok"}
