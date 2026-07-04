from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.customer import CustomerCreate
from app.services.customer_service import create_customer, get_customers

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("")
def add_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)


@router.get("")
def list_customers(db: Session = Depends(get_db)):
    return get_customers(db)