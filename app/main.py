from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "API funcionando"}

app = FastAPI()

app.include_router(user_router)