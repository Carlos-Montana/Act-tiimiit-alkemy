'''
Aca se creara la variable engine que conectara con el motor de base de datos,
la variable sesion para poder realizar operaciones en las tablas,
y la variable Base la cual es heredada para crear en el modelo la clases que
hacen referencias a las distintas tablas.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cfg import HOST, DB, USER_DB, PASSWORD_DB, DIALECTO, PORT

engine = create_engine(
    f'{DIALECTO}://{USER_DB}:{PASSWORD_DB}@{HOST}:{PORT}/{DB}')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
