# archivo tabla3.py
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Tabla3(Base):
    __tablename__ = 'tabla3'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    IdTabla1 = Column(Integer, ForeignKey('tabla1.id'))

