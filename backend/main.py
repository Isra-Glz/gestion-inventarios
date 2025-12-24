from fastapi import FastAPI
from database import get_connection

app = FastAPI()

# -----------------------------------
# GET: Productos con nombre categoría
# -----------------------------------
@app.get("/productos-con-categoria")
def get_productos_con_categoria():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            p.id_producto,
            p.nombre,
            p.descripcion,
            c.nombre AS categoria,
            p.stock,
            p.precio
        FROM Productos p
        INNER JOIN Categorias c
            ON p.id_categoria = c.id_categoria
    """)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    data = [dict(zip(columns, row)) for row in rows]

    conn.close()
    return data


# -------------------------
# GET: Todos los productos
# -------------------------
@app.get("/productos")
def get_productos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            id_producto,
            nombre,
            descripcion,
            id_categoria,
            stock,
            precio
        FROM Productos
    """)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    data = [dict(zip(columns, row)) for row in rows]

    conn.close()
    return data


# -------------------------
# GET: Producto por ID
# -------------------------
@app.get("/productos/{id_producto}")
def get_producto(id_producto: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            id_producto,
            nombre,
            descripcion,
            id_categoria,
            stock,
            precio
        FROM Productos
        WHERE id_producto = ?
    """, id_producto)

    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"error": "Producto no encontrado"}

    columns = [column[0] for column in cursor.description]
    return dict(zip(columns, row))
