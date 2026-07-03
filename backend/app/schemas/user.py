from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    mobile: str
    shop_name: str
    language: str