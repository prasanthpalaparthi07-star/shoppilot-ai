from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.customer import Customer
from app.models.sale import Sale


def get_dashboard(db: Session):
    total_products = db.query(Product).count()
    total_customers = db.query(Customer).count()
    total_sales = db.query(Sale).count()

    total_credit = sum(
        customer.balance for customer in db.query(Customer).all()
    )

    low_stock_products = db.query(Product).filter(Product.stock < 10).count()

    return {
        "total_products": total_products,
        "total_customers": total_customers,
        "total_sales": total_sales,
        "total_credit": total_credit,
        "low_stock_products": low_stock_products
    }