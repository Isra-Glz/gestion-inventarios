from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def obtener_usuarios():
    return {"message": "Lista de usuarios del sistema"}

