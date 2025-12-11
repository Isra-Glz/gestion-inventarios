from fastapi import FastAPI
from app.routes import inventory_routes  # lo crearemos después
from app.routes import users_routes      # lo crearemos después

app = FastAPI(
    title="API de Gestión de Inventario",
    description="Backend con Python, FastAPI y SQL Server",
    version="1.0.0"
)

# Registrar rutas
app.include_router(inventory_routes.router, prefix="/inventario", tags=["Inventario"])
app.include_router(users_routes.router, prefix="/usuarios", tags=["Usuarios"])

# Ruta de prueba
@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}


