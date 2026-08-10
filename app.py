from fastapi import FastAPI

app = FastAPI()

@app.get("/{path:path}")
def todo(path: str):
    return {
        "ruta": path
    }
