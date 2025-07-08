from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    nombre: str
    correo: str
    contrasena: str
    rol: str = 'usuario'  # Valor por defecto si no se especifica
    cargo: Optional[str] = None
    id_jefe: Optional[int] = None

    class Config:
        from_attributes = True  # Reemplaza a orm_mode en Pydantic v2

class ShowUser(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str

    class Config:
        from_attributes = True
