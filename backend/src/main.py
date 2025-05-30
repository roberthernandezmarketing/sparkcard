# sparkcard/backend/src/main.py
from fastapi import FastAPI
# from src.api.v1.routes import card_routes
from backend.src.api.v1.routes import card_routes

app = FastAPI(
    title="Sparkcard API.",
    description="API for managing flashcards and study content by Rob Hernandez @kreativedevlab.",
    version="1.0.0",
)

# Incluir routers por categoría para mejor organización en la documentación de la API
app.include_router(card_routes.router, prefix="/api/v1/cards", tags=["Cards"])

# Puedes añadir más routers aquí a medida que los crees
# app.include_router(list_routes.router, prefix="/api/v1/lists", tags=["Lists"])
# app.include_router(session_routes.router, prefix="/api/v1/sessions", tags=["Sessions"])

@app.get("/")
async def root():
    return {"message": "Welcome to Sparkcard API!"}