from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db

from app.schemas.product import ProductCreate
from app.services.product_service import create_product, get_products

router = APIRouter()


@router.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)
