from fastapi import FastAPI
from database import get_connection
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()

#------------------------------------
# POST: Productos
#------------------------------------

class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    id_categoria: int
    stock: int
    precio: float


@app.post("/productos")
def create_producto(producto: ProductoCreate):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Productos (nombre, descripcion, id_categoria, stock, precio)
            VALUES (?, ?, ?, ?, ?)
        """,
        producto.nombre,
        producto.descripcion,
        producto.id_categoria,
        producto.stock,
        producto.precio
        )

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        conn.close()

    return {
        "mensaje": "Producto creado correctamente",
        "producto": producto
    }

#------------------------------------
#PUT
#------------------------------------
@app.put("/productos/{id_producto}")
def update_producto(id_producto: int, producto: ProductoCreate):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE Productos
            SET 
                nombre = ?,
                descripcion = ?,
                id_categoria = ?,
                stock = ?,
                precio = ?
            WHERE id_producto = ?
        """,
        producto.nombre,
        producto.descripcion,
        producto.id_categoria,
        producto.stock,
        producto.precio,
        id_producto
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        conn.close()

    return {"mensaje": "Producto actualizado correctamente"}


#-----------------------------------
#Delete
#-----------------------------------
@app.delete("/productos/{id_producto}")
def delete_producto(id_producto: int):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM Productos
            WHERE id_producto = ?
        """, id_producto)

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        conn.close()

    return {"mensaje": "Producto eliminado correctamente"}





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
