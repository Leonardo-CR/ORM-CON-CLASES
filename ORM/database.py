# archivo database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configura el motor de la base de datos (en este caso, SQLite)
engine = create_engine('postgresql://postgres:admin@localhost:5432/clases')

# Crea una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Define la base de datos
Base = declarative_base()

# Cierra la sesión
def close_session():
    session.close()
