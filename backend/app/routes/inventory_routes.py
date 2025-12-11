from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def obtener_inventario():
    return {"message": "Lista de productos del inventario"}

