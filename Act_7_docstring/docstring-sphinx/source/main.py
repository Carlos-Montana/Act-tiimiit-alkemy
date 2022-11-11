# Palabras reservadas para docstring->sphinx
# :param : valor del parámetro.
# :type : tipo de variable.
# :return : valor devuelto.
# :rtype : tipo de valor devuelto.
# :raises : describe los errores que genera el código.
# ..seealso:: : otras lecturas de interés.
# ..notes:: : agrega una nota
# ..warning:: agrega una advertencia
from datetime import datetime


class Empleados:
    '''
    This class save data of employed

    :param first_name: Name of employed
    :param last_name: Lastname of employed
    :param date_born: Date of born wiht date -> 'YYYY-mm-dd'
    :param dni: Number of document
    .. warning::
        Becareful with the format born date -> 'YYYY-mm-dd'
    .. note::
        This is note test
    .. seealso::
        This is see also test
    '''

    def __init__(self, first_name: str, last_name: str, date_born: str, dni: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.date_born = date_born
        self.dni = dni

    def get_age(self) -> int:
        '''
        This method no recieved parameters

        :return: Age of employed
        :rtype: float

        '''
        calculate_born = datetime.strptime(self.date_born, '%Y-%m-%d')
        calculate_now = datetime.now()
        calculate_age = calculate_now - calculate_born
        return int((calculate_age.days/365))

    def presentation(self) -> str:
        '''
        This method no recived parameters

        :return: first and last name, born and DNI
        :rtype: string

        '''
        return f"Hi, I'm {self.first_name} {self.last_name} :: born {self.date_born} :: and my DNI is {self.dni}"


prueba = Empleados('pepe', 'honguito', '1920-06-29', 123456789)
print(prueba.get_age())
print(prueba.presentation())
