# 
# sparkcard/backend/src/main.py
# 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from backend.src.api.v1.routes import card_routes

app = FastAPI(
    title="Sparkcard API.",
    description="API for managing flashcards and study content by Rob Hernandez @kreativedevlab.",
    version="1.0.0",
)

# Define los orígenes permitidos. En producción, solo tu dominio.
# Puedes usar una variable de entorno para esto en producción.
# Ejemplo usando una variable de entorno llamada FRONTEND_URL
# que configurarás en Render.
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000") # Por defecto para desarrollo

origins = [
    FRONTEND_URL,
    "http://localhost:3000",  # Para desarrollo local de tu frontend
    "http://localhost:8000",  # Si corres tu frontend en 8000 localmente para pruebas
]

# Si tu frontend puede estar en múltiples subdominios o necesitas más flexibilidad,
# puedes ser más permisivo durante el desarrollo, pero restrictivo en producción.
# Para producción, es mejor tener solo el dominio de tu frontend.
# Otra opción: permitir cualquier origen en desarrollo si FRONTEND_URL no está definido.
# if not os.getenv("RENDER"): # Solo en desarrollo, si no estamos en Render
#     origins.append("*") # Permitir todo para depuración local

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir routers por categoría para mejor organización en la documentación de la API
app.include_router(card_routes.router, prefix="/api/v1/cards", tags=["Cards"])

# Puedes añadir más routers aquí a medida que los crees
# app.include_router(list_routes.router, prefix="/api/v1/lists", tags=["Lists"])
# app.include_router(session_routes.router, prefix="/api/v1/sessions", tags=["Sessions"])

@app.get("/")
async def root():
    return {"message": "Welcome to Sparkcard API!"}