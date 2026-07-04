from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    buying_price = Column(Float)
    selling_price = Column(Float)
    stock = Column(Integer)