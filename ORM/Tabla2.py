# archivo tabla2.py
from sqlalchemy import Column, Integer, String
from database import Base

class Tabla2(Base):
    __tablename__ = 'tabla2'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
