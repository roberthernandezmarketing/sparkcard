# 
# sparkcard/backend/src/main.py
#
# Main file that initializes the FastAPI application, configures the CORS middleware, 
#   and registers API routers. It defines the application's entry point.
# 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer

from backend.src.api.v1.routes import card_routes, list_routes, auth_routes
from backend.src.core.config import settings

app = FastAPI(
    title="Sparkcard Super API w/OAuth2.",
    description="API for managing flashcards and study content by Rob Hernandez @kreativedevlab.",
    version="1.2.0",
)

# Define the allowed origins. In production, only your domain.
# You can use an environment variable for this in production.
# Example using an environment variable called FRONTEND_URL
# which you will set in Render.
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000") # Default for development

origins = [
    FRONTEND_URL,
    "http://localhost:3000",  # For local development of your frontend
    "http://localhost:8000",  # If you run your frontend on 8000 locally for testing
    "https://sparkcard.kreativedevlabs.com/",
]

# If your frontend can be on multiple subdomains or you need more flexibility,
# you can be more permissive during development, but restrictive in production.
# For production, it's better to have only your frontend domain.
# Another option: allow any origin in development if FRONTEND_URL is not defined.
# if not os.getenv("RENDER"): # Only in development, if not in Render
# origins.append("*") # Allow everything for local debugging

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Include routers by category for better organization in the API documentation
app.include_router(card_routes.router, prefix="/api/v1/cards", tags=["Cards"])
app.include_router(list_routes.router, prefix="/api/v1/lists", tags=["Lists"])
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Authentication"])

# You can add more routers here as you create them
# app.include_router(list_routes.router, prefix="/api/v1/lists", tags=["Lists"])
# app.include_router(session_routes.router, prefix="/api/v1/sessions", tags=["Sessions"])

@app.get("/")
async def root():
    return {"message": "Welcome to Sparkcard API!"}

# 🔒 OAuth2PasswordBearer para que Swagger muestre el botón "Authorize"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SparkCard API",
        version="1.0",
        description="API para SparkCard",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": "/api/v1/auth/login",
                    "scopes": {}
                }
            }
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi