from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import json

app = FastAPI()

with open("empleados.json", "r", encoding="utf8") as f:
    empleados = json.load(f)


@app.get("/", response_class=HTMLResponse)
def validar(t: str = ""):

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
            font-size:35px;
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
        font-size:65px;
        margin-bottom:15px;
    }}

    h2{{
        font-size:55px;
        margin-bottom:35px;
    }}

    .dato{{
        font-size:30px;
        margin:10px;
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
