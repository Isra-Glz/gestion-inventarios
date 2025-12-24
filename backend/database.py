import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_DATABASE};"
    "Trusted_Connection=yes;"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

def get_connection():
    return pyodbc.connect(connection_string)
