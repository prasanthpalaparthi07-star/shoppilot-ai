from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate


def create_customer(db: Session, customer: CustomerCreate):
    existing = db.query(Customer).filter(
        Customer.mobile == customer.mobile
    ).first()

    if existing:
        return {"error": "Customer already exists"}

    new_customer = Customer(
        name=customer.name,
        mobile=customer.mobile
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def get_customers(db: Session):
    return db.query(Customer).all()
def add_credit(db: Session, customer_id: int, amount: float):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        return {"error": "Customer not found"}

    customer.balance += amount

    db.commit()
    db.refresh(customer)

    return customer


def pay_credit(db: Session, customer_id: int, amount: float):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        return {"error": "Customer not found"}

    if customer.balance < amount:
        return {"error": "Payment exceeds balance"}

    customer.balance -= amount

    db.commit()
    db.refresh(customer)

    return customer

def add_credit(db: Session, customer_id: int, amount: float):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        return {"error": "Customer not found"}

    customer.balance += amount

    db.commit()
    db.refresh(customer)

    return customer


def pay_credit(db: Session, customer_id: int, amount: float):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        return {"error": "Customer not found"}

    if customer.balance < amount:
        return {"error": "Payment exceeds balance"}

    customer.balance -= amount

    db.commit()
    db.refresh(customer)

    return customer