from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import json
import os

app = FastAPI(title="LUSEO QR TEST")

@app.get("/test")
def test():
    return {
        "funciona": True,
        "version": "10 Agosto",
        "mensaje": "Hola LUSEO"
    }

# Ruta absoluta para que funcione tanto en Windows como en Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "empleados.json")


@app.get("/", response_class=HTMLResponse)
def validar(t: str = ""):

    # Leer el JSON en cada consulta (así siempre toma la versión actual)
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            empleados = json.load(f)
    except Exception as e:
        return HTMLResponse(
            f"""
            <html>
            <body style="font-family:Arial;background:#222;color:white;padding:40px">
            <h1>Error cargando empleados.json</h1>
            <pre>{e}</pre>
            </body>
            </html>
            """,
            status_code=500,
        )

    empleado = None

    for emp in empleados:
        if emp["token"] == t:
            empleado = emp
            break

    fecha = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%I:%M %p")

    if empleado is None:

        return f"""
        <html>

        <head>

        <title>Control de Acceso</title>

        <style>

        body{{
            margin:0;
            background:#d32f2f;
            color:white;
            font-family:Arial;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
        }}

        .card{{
            text-align:center;
        }}

        h1{{
            font-size:70px;
            margin-bottom:20px;
        }}

        h2{{
            font-size:40px;
        }}

        p{{
            font-size:22px;
        }}

        </style>

        </head>

        <body>

        <div class="card">

            <h1>🔴</h1>

            <h2>ACCESO DENEGADO</h2>

            <p>Token inválido</p>

        </div>

        </body>

        </html>
        """

    if empleado["status"] == "ACTIVE":

        color = "#16a34a"
        icono = "🟢"
        titulo = "ACCESO PERMITIDO"

    else:

        color = "#d32f2f"
        icono = "🔴"
        titulo = "ACCESO DENEGADO"

    return f"""
    <html>

    <head>

    <title>Control de Acceso</title>

    <style>

    body{{
        margin:0;
        background:{color};
        color:white;
        font-family:Arial;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }}

    .card{{
        text-align:center;
        padding:40px;
    }}

    h1{{
        font-size:70px;
        margin-bottom:10px;
    }}

    h2{{
        font-size:60px;
        margin-bottom:35px;
    }}

    .dato{{
        font-size:30px;
        margin:8px;
    }}

    .fecha{{
        margin-top:40px;
        font-size:22px;
        opacity:.9;
    }}

    </style>

    </head>

    <body>

    <div class="card">

        <h1>{icono}</h1>

        <h2>{titulo}</h2>

        <div class="dato"><b>{empleado["nombre"]}</b></div>

        <div class="dato">{empleado["cargo"]}</div>

        <div class="dato">{empleado["oficina"]}</div>

        <div class="fecha">

            {fecha}<br>
            {hora}

        </div>

    </div>

    </body>

    </html>
    """
