from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.customer import CustomerCreate, CreditUpdate
from app.services.customer_service import (
    create_customer,
    get_customers,
    add_credit,
    pay_credit,
)

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("")
def add_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)


@router.get("")
def list_customers(db: Session = Depends(get_db)):
    return get_customers(db)


@router.post("/add-credit")
def add_credit_api(data: CreditUpdate, db: Session = Depends(get_db)):
    return add_credit(db, data.customer_id, data.amount)


@router.post("/pay")
def pay_credit_api(data: CreditUpdate, db: Session = Depends(get_db)):
    return pay_credit(db, data.customer_id, data.amount)