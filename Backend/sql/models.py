from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sql.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(50), index=True, unique=True)
    name = Column(String(50), index=True)
    password = Column(String(70))

class Stylist(Base):
    __tablename__ = "stylists"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(50), index=True, unique=True)
    name = Column(String(50), index=True)
    password = Column(String(70))
    profession = Column(String(50), index=True)

