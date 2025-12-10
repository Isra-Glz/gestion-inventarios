import pyodbc

def get_connection():
    """
    Retorna una conexión a SQL Server usando pyodbc.
    Las credenciales se configurarán más adelante.
    """
    server = "TU_SERVIDOR"
    database = "InventarioDB"
    username = "TU_USUARIO"
    password = "TU_PASSWORD"

    connection_string = (
        f"DRIVER={{SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )

    return pyodbc.connect(connection_string)

