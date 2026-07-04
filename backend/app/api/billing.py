from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.sale import SaleItem
from app.services.billing_service import create_sale

router = APIRouter(prefix="/billing", tags=["Billing"])


@router.post("/create-sale")
def create_sale_api(sale: SaleItem, db: Session = Depends(get_db)):
    return create_sale(db, sale.product_id, sale.quantity)