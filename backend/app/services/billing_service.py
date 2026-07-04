from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.sale import Sale


def create_sale(db: Session, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    if product.stock < quantity:
        return {"error": "Insufficient stock"}

    total = product.selling_price * quantity

    product.stock -= quantity

    sale = Sale(
        product_id=product.id,
        quantity=quantity,
        total_amount=total
    )

    db.add(sale)
    db.commit()
    db.refresh(sale)

    return {
        "message": "Sale completed successfully",
        "sale_id": sale.id,
        "product": product.name,
        "quantity": quantity,
        "total": total,
        "remaining_stock": product.stock
    }