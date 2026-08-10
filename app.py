from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"ok": True}

@app.get("/test")
def test():
    return {
        "mensaje": "hola"
    }
