from sqlalchemy import Column, String, Integer
from db.database import Base

class Products(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100)) 
    description = Column(String(100))
    quantity = Column(Integer)   
    price = Column(Integer)   

    __tablename__ = "mc_products" 
    