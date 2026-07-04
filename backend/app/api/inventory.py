from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.inventory import StockUpdate
from app.services.inventory_service import add_stock, remove_stock

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/add-stock")
def add_stock_api(stock: StockUpdate, db: Session = Depends(get_db)):
    return add_stock(db, stock.product_id, stock.quantity)


@router.post("/remove-stock")
def remove_stock_api(stock: StockUpdate, db: Session = Depends(get_db)):
    return remove_stock(db, stock.product_id, stock.quantity)