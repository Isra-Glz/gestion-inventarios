from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_inventory():
    return [
        {"id": 1, "name": "Laptop", "stock": 10, "price": 15000},
        {"id": 2, "name": "Mouse", "stock": 50, "price": 250},
        {"id": 3, "name": "Teclado", "stock": 20, "price": 800},
    ]
