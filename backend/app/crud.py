# app/crud.py
from .database import get_connection
from .auth import hashear_password

def crear_usuario(nombre, correo, contrasena, rol='usuario'):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hashear_password(contrasena)
    # CORREGIDO: Los parámetros deben ir en una tupla
    cursor.execute("INSERT INTO usuarios (nombre, correo, contrasena, rol) VALUES (?, ?, ?, ?)",
                   (nombre, correo, hashed, rol))
    conn.commit()
    conn.close()

def obtener_usuario_por_correo(correo):
    conn = get_connection()
    cursor = conn.cursor()
    # CORREGIDO: El parámetro debe ir en una tupla
    cursor.execute("SELECT id, nombre, correo, contrasena, rol FROM usuarios WHERE correo = ?", (correo,))
    result = cursor.fetchone()
    conn.close()
    return result

def obtener_usuario_por_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    # CORREGIDO: El parámetro debe ir en una tupla
    cursor.execute("SELECT id, nombre, correo, rol FROM usuarios WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, correo, rol FROM usuarios")
    result = cursor.fetchall()
    conn.close()
    return result