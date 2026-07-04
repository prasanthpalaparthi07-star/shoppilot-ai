from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    mobile: str

class CreditUpdate(BaseModel):
    customer_id: int
    amount: float