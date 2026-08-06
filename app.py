from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

# Cargar la lista de empleados
with open("empleados.json", "r", encoding="utf8") as f:
    empleados = json.load(f)

@app.get("/", response_class=HTMLResponse)
def validar(t: str = ""):

    estado = None

    for emp in empleados:

        if emp["token"] == t:

            estado = emp["status"]

            break

    if estado == "ACTIVE":

        color = "#16a34a"
        mensaje = "🟢 ACCESO PERMITIDO"

    else:

        color = "#dc2626"
        mensaje = "🔴 ACCESO DENEGADO"

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Control de Acceso</title>

        <style>

            body{{
                margin:0;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                background:{color};
                font-family:Arial;
                color:white;
                text-align:center;
            }}

            h1{{
                font-size:60px;
            }}

        </style>

    </head>

    <body>

        <div>

            <h1>{mensaje}</h1>

        </div>

    </body>

    </html>
    """