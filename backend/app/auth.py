# app/auth.py
from jose import jwt, JWTError
from passlib.hash import bcrypt
from fastapi import HTTPException
import datetime

SECRET_KEY = "secreto"
ALGORITHM = "HS256"

def generar_token(data: dict):
    data.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=3)})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido")

def verificar_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

def hashear_password(password):
    return bcrypt.hash(password)