# app/crud.py
from .database import get_connection
from .auth import hashear_password

def crear_usuario(nombre, correo, contrasena, rol='usuario', cargo=None, id_jefe=None):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hashear_password(contrasena)

    cursor.execute(
        "INSERT INTO usuarios (nombre, correo, contrasena, rol, cargo, id_jefe) VALUES (?, ?, ?, ?, ?, ?)",
        (nombre, correo, hashed, rol, cargo, id_jefe)
    )
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


def obtener_jerarquia_por_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    WITH RECURSIVE jerarquia AS (
        SELECT id, nombre, cargo, id_jefe, 1 AS nivel
        FROM usuarios
        WHERE id = ?
        UNION ALL
        SELECT u.id, u.nombre, u.cargo, u.id_jefe, j.nivel + 1
        FROM usuarios u
        INNER JOIN jerarquia j ON u.id = j.id_jefe
    )
    SELECT * FROM jerarquia ORDER BY nivel;
    """

    cursor.execute(query, (user_id,))
    resultados = cursor.fetchall()

    conn.close()
    return resultados