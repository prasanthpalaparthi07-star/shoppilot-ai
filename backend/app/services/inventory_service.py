from sqlalchemy.orm import Session

from app.models.product import Product


def add_stock(db: Session, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    product.stock += quantity
    db.commit()
    db.refresh(product)

    return product


def remove_stock(db: Session, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    if product.stock < quantity:
        return {"error": "Insufficient stock"}

    product.stock -= quantity
    db.commit()
    db.refresh(product)

    return product