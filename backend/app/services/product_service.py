from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate
from app.schemas.product import ProductCreate

products = []


def create_product(db: Session, product: ProductCreate):
    new_product = Product(
        name=product.name,
        category=product.category,
        buying_price=product.buying_price,
        selling_price=product.selling_price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def get_products(db: Session):
    return db.query(Product).all()