from fastapi import FastAPI
from app.api.users import router as user_router

app = FastAPI(title="ShopPilot AI API")

app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "Welcome to ShopPilot AI 🚀"}