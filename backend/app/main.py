# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from . import crud, schemas, deps, auth
from .models import UserCreate
from fastapi import Body
from .schemas import UserCreate
from .database import get_connection


# ESTO ES LO IMPORTANTE: La variable debe llamarse 'app'
app = FastAPI(title="Sistema de Usuarios", version="1.0.0")

# Permitir acceso desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint: Health check
@app.get("/")
def root():
    return {"message": "API de Sistema de Usuarios funcionando correctamente"}

# Endpoint: Login
@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    try:
        usuario = crud.obtener_usuario_por_correo(form.username)
        print("Usuario desde DB:", usuario)  # Debug
        print("Password ingresada:", form.password)  # Debug
        if not usuario or not auth.verificar_password(form.password, usuario[3]):
            raise HTTPException(status_code=400, detail="Credenciales incorrectas")

        token = auth.generar_token({
            "id": usuario[0],
            "nombre": usuario[1],
            "correo": usuario[2],
            "rol": usuario[4]
        })
        return {"access_token": token, "token_type": "bearer"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en login: {str(e)}")


# Endpoint: Registrar (solo admin)
@app.post("/registro")
def registrar(
    user: UserCreate = Body(...),
    current_user=Depends(deps.get_current_user)
):
    try:
        if current_user["rol"] != "admin":
            raise HTTPException(status_code=403, detail="No autorizado")

        existing_user = crud.obtener_usuario_por_correo(user.correo)
        if existing_user:
            raise HTTPException(status_code=400, detail="El usuario ya existe")

        crud.crear_usuario(
            nombre=user.nombre,
            correo=user.correo,
            contrasena=user.contrasena,
            rol=user.rol,
            cargo=user.cargo,
            id_jefe=user.id_jefe
        )
        return {"mensaje": "Usuario registrado exitosamente"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en registro: {str(e)}")



# Endpoint: Ver un usuario (usuario o admin)
@app.get("/usuario/{id}", response_model=schemas.ShowUser)
def ver_usuario(id: int, current_user=Depends(deps.get_current_user)):
    try:
        if current_user["id"] != id and current_user["rol"] != "admin":
            raise HTTPException(status_code=403, detail="Acceso denegado")
        
        u = crud.obtener_usuario_por_id(id)
        if not u:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return schemas.ShowUser(id=u[0], nombre=u[1], correo=u[2], rol=u[3])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuario: {str(e)}")

# Endpoint: Ver todos los usuarios (solo admin)
@app.get("/usuarios", response_model=list[schemas.ShowUser])
def ver_usuarios(current_user=Depends(deps.get_current_user)):
    try:
        if current_user["rol"] != "admin":
            raise HTTPException(status_code=403, detail="No autorizado")
        
        rows = crud.obtener_usuarios()
        return [schemas.ShowUser(id=r[0], nombre=r[1], correo=r[2], rol=r[3]) for r in rows]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")
    
    # Endpoint: Jerarquía de un usuario (con CTE recursivo)
@app.get("/jerarquia/{id}")
def jerarquia(id: int, current_user=Depends(deps.get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            WITH jerarquia AS (
                SELECT id, nombre, cargo, id_jefe, 1 AS nivel
                FROM usuarios
                WHERE id = ?
                UNION ALL
                SELECT u.id, u.nombre, u.cargo, u.id_jefe, j.nivel + 1
                FROM usuarios u
                JOIN jerarquia j ON u.id = j.id_jefe
            )
            SELECT nivel, nombre, cargo FROM jerarquia ORDER BY nivel;
        """, (id,))
        
        resultado = cursor.fetchall()
        conn.close()

        return [{"nivel": row[0], "nombre": row[1], "cargo": row[2]} for row in resultado]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener jerarquía: {str(e)}")
