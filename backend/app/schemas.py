# app/schemas.py
from pydantic import BaseModel

class ShowUser(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str

    class Config:
        from_attributes = True  # Cambiado de orm_mode a from_attributes (Pydantic v2)