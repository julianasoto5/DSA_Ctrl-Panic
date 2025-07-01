from flask import Flask, render_template, request, redirect, url_for, session
from database import Database
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from sqlalchemy.sql import select
import random
import string
import base64
import os

app = Flask(__name__)
clubes = ["Estudiantes de La Plata", "Boca Juniors", "River Plate", "Racing Club", "Independiente", "San Lorenzo", "Vélez Sarsfield", "Newell"]
paso1=0
paso2=0    

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def elegir_club():
    return random.choice(clubes)

USUARIOS = [{"id": 1, "usuario": "user", "contrasena": "pass", "apellido": "Panic", "nombre": "Ctrl", "club": clubes[0]},
            {"id": random.randint(32,100), "usuario": "admin", "contrasena": generar_contrasena(8), "apellido": "Tengo una flag", "nombre": "Flagger", "club": os.environ.get("FLAG1")},
            {"id": random.randint(100,110),"usuario": "DSA","contrasena": "123456789", "apellido": "Segurisimo", "nombre": "Seguridad","club": os.environ.get("FLAG2")}]

for i in range(1,30):
    usuario = {}
    usuario["id"] = i+1
    usuario["usuario"] = "usuario" + str(i + 1)
    usuario["contrasena"] = generar_contrasena(8)
    usuario["apellido"] = "Apellido" + str(i + 1)
    usuario["nombre"] = "Nombre" + str(i + 1)
    usuario["club"] = elegir_club()
    USUARIOS.append(usuario)

# Renderiza la página de inicio
@app.route("/")
def index():
    return render_template("index.html")

# Renderiza la página de inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        for usuario_bd in USUARIOS:
            if usuario_bd["usuario"] == usuario and usuario_bd["contrasena"] == contrasena:
                if usuario == "admin":
                    session["paso1"] = True  # Marcar que pasó por admin
                    return redirect(url_for("perfil", id=usuario_bd["id"]))
                elif usuario == "DSA":
                    if not session.get("paso1"):  # Si no pasó por admin primero
                        usuario_bd["club"] = os.environ.get("WARNING")
                    else:
                        session["paso2"] = True  # Marcar que pasó por DSA
                        usuario_bd["club"] = os.environ.get("FLAG2")
                    return render_template("perfil.html", usuario_actual=usuario_bd)
                return redirect(url_for("perfil", id=usuario_bd["id"]))
        error = "Nombre de usuario o contraseña incorrectos"
    return render_template("index.html", error=error)


# Renderiza la página de perfil
@app.route("/perfil/<int:id>", methods=["GET", "POST"])
def perfil(id):
    usuario_bd = None
    for usuario in USUARIOS:
        if usuario["id"] == id:
            usuario_bd = usuario
            break
    if usuario_bd is None:
        return redirect(url_for("index"))

    if request.method == "POST":
        usuario_bd["nombre"] = request.form["nombre"]
        usuario_bd["club"] = request.form["club"]
        return redirect(url_for("perfil", id=id))
    return render_template("perfil.html", usuario_actual=usuario_bd)

@app.route("/buscar", methods=["GET"])
def buscar():
    resultados = None
    pasos_completos = False
    if "club" in request.args:
        club = request.args.get("club", "")
        db = Database()
        
        # Verificar si completó los pasos
        pasos_completos = session.get('paso1') and session.get('paso2')
        
        # Detectar intentos de SQLi (patrones comunes)
        intento_sqli = any(
            keyword in club.upper() 
            for keyword in ["' OR ", "--", "1=1", "UNION", "/*"]
        )
        
        if intento_sqli:
            if pasos_completos:
                # Permitir ver toda la tabla (incluyendo flag)
                resultados = db.buscar_por_club("' OR 1=1 -- ", mostrar_flag=True)
            else:
                # Engañar al atacante con datos falsos
                resultados = [{
                    'id': 0,
                    'nombre': 'Tenemos un plan aquí che',
                    'partidos': os.environ.get("WARNING")
                }]
        else:
            # Búsqueda normal (filtra flag si no hay permisos)
            resultados = db.buscar_por_club(club, mostrar_flag=pasos_completos)
    
    return render_template("buscar.html", 
                        resultados=resultados,
                        pasos_completos=pasos_completos)
if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)

