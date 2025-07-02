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
import requests

RECAPTCHA_SECRET_KEY = '6Ld0EHIrAAAAANo67b4KNnxRKnpUwWdfXqTkLdl8'
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Necesario para usar sesiones

clubes = ["Estudiantes de La Plata", "Boca Juniors", "River Plate", "Racing Club", "Independiente", "San Lorenzo", "Vélez Sarsfield", "Newell"]
        
def generar_contrasena(longitud):
        caracteres = string.ascii_letters + string.digits
        contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
        return contrasena

def elegir_club():
        return random.choice(clubes)

USUARIOS = [{"id": 1, "usuario": "user", "contrasena": "pass", "apellido": "Panic", "nombre": "Ctrl", "club": clubes[0]},
                {"id": random.randint(32,100), "usuario": "admin", "contrasena": generar_contrasena(8), "apellido": "Tengo una flag", "nombre": "Flagger", "club": os.environ.get("FLAG1")},
                {"id": random.randint(101,150),"usuario": "DSA","contrasena": "123456789", "apellido": "Segurisimo", "nombre": "Seguridad","club": os.environ.get("FLAG2")}]

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
                # Verificar CAPTCHA
            captcha_response = request.form.get('g-recaptcha-response')
            if not captcha_response:
                return render_template('index.html', error="Captcha no completado")

            # Validar con Google
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                'secret': RECAPTCHA_SECRET_KEY,
                'response': captcha_response
            })
            result = r.json()
            if not result.get('success'):
                return render_template('index.html', error="Captcha inválido")
            
            referer = request.headers.get("Referer", "")
            if not referer.startswith("http://localhost:15000/login"):
                return "Acceso denegado: Referer inválido", 403
            
            usuario = request.form["usuario"]
            contrasena = request.form["contrasena"]
            for usuario_bd in USUARIOS:
                if usuario_bd["usuario"] == usuario and usuario_bd["contrasena"] == contrasena:
                    session["user_id"] = usuario_bd["id"] # Guarda en el objeto session
                    return redirect(url_for("perfil", id=usuario_bd["id"]))
            error = "Nombre de usuario o contraseña incorrectos"
        return render_template("index.html", error=error)


    # Renderiza la página de perfil
@app.route("/perfil/<int:id>", methods=["GET", "POST"])
def perfil(id):
        if "user_id" not in session or session["user_id"] != id:       #Comprueba que el usuario al que se quiere acceder es el logueado 
            return redirect(url_for('index'))
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
        if "club" in request.args:
            club = request.args.get("club")
            db = Database()
            resultados = db.buscar_por_club(club)  # <-- función nueva que agregás ahora
        return render_template("buscar.html", resultados=resultados)

if __name__ == "__main__":
        app.run(host = "0.0.0.0", debug=True)
