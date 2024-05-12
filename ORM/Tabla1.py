# archivo tabla1.py
from sqlalchemy import Column, Integer, String
from database import Base

class Tabla1(Base):
    __tablename__ = 'tabla1'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
