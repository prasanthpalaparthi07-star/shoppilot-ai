from sqlalchemy import Column, Integer, String
from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    mobile = Column(String)
    shop_name = Column(String)
    language = Column(String)