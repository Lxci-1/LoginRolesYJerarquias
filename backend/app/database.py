# app/database.py
import pyodbc
from fastapi import HTTPException

def get_connection():
    try:
        return pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=bdd_usuarios;'
            'Trusted_Connection=yes;'
            'TrustServerCertificate=yes;'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión a la base de datos: {str(e)}")
