'''
Aca se crearan la o las clases que hacen referencia a las tablas
en la base de datos.
'''
import db
from sqlalchemy import Column, Integer, String


class Customer(db.Base):
    '''
    Esta clase esta asociada a la tabla customer
    de la base de datos postgres
    '''
    # Nombre de la tabla asociada
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)

    def __init__(
        self, name: str, age: int, email: str, address: str, zip_code: int
            ) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

    def __repr__(self):
        # Sobrescribiendo repr, para que represente lo siguiente.
        return f'Customer ({self.name}, {self.zip_code})'

    def __str__(self):
        # Sobrescribiendo str, para muestre este nombre de clase.
        return self.name
