from flask import Flask, render_template, request, redirect, flash
import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Conexión MySQL usando variables del entorno
def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=DictCursor
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_contact", methods=["POST"])
def add_contact():
    nombre = request.form["nombre"]
    email = request.form["email"]
    telefono = request.form.get("telefono")

    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO contacts (nombre, email, telefono)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (nombre, email, telefono))
            conn.commit()

        flash("Contacto agregado correctamente", "success")
    except pymysql.err.IntegrityError:
        flash("El correo ya está registrado", "error")
    except Exception:
        flash("Error al conectar con la base de datos", "error")
    finally:
        conn.close()

    return redirect("/")


@app.route("/contacts")
def contacts():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM contacts ORDER BY fecha_registro DESC;")
            data = cursor.fetchall()
        return render_template("contacts.html", contacts=data)
    except Exception:
        flash("Error al obtener contactos", "error")
        return render_template("contacts.html", contacts=[])
