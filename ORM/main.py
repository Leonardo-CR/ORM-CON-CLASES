from database import engine, Base, close_session
from Tabla1 import Tabla1
from Tabla2 import Tabla2
from Tabla3 import Tabla3

# Crea las tablas en la base de datos
Base.metadata.create_all(engine)


"""
# Ejemplo de cómo agregar datos a las tablas
from database import session
registro_tabla1 = Tabla1(nombre='Ejemplo de dato para tabla1')
session.add(registro_tabla1)

registro_tabla2 = Tabla2(descripcion='Ejemplo de dato para tabla2')
session.add(registro_tabla2)

# Confirma las transacciones
session.commit()

# Cierra la sesión
close_session()
"""