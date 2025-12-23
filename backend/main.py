from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import inventory_routes

app = FastAPI(
    title="API de Gestión de Inventario",
    description="Backend con Python, FastAPI y SQL Server",
    version="1.0.0",
)

# CORS (permitir React en desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # SOLO para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(
    inventory_routes.router,
    prefix="/inventario",
    tags=["Inventario"],
)

# Ruta raíz de prueba
@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
