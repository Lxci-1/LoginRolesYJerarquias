# app/models.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre: str
    correo: str
    contrasena: str

class UserLogin(BaseModel):
    correo: str
    contrasena: str