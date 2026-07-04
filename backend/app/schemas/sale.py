from pydantic import BaseModel


class SaleItem(BaseModel):
    product_id: int
    quantity: int