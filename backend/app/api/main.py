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
app = FastAPI(title="ShopPilot AI API")
Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(billing_router)
app.include_router(customer_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to ShopPilot AI 🚀"
    }