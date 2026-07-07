from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.product import Product
from app.models.sale import Sale
from app.models.customer import Customer
from app.models.user import User
from app.api.users import router as user_router
from app.api.products import router as product_router
from app.api.inventory import router as inventory_router
from app.api.billing import router as billing_router
from app.api.customer import router as customer_router
from app.api.dashboard import router as dashboard_router
app = FastAPI(title="ShopPilot AI API")
app.add_middleware(
    CORSMiddleware,
   allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(billing_router)
app.include_router(customer_router)
app.include_router(dashboard_router)
@app.get("/")
def home():
    return {
        "message": "Welcome to ShopPilot AI 🚀"
    }