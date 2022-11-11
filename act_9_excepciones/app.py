# Ejercicio practico
# Lista de transporte

from typing import Any
import signal
import sys


def def_handler(sig, frame):
    print('\n[!] Saliendo...\n')
    sys.exit(1)


# controlando salida del script ctrl + c
signal.signal(signal.SIGINT, def_handler)

# Lista de trabajo
medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']

default_msg = '[**] Vuelva a ingresar un numero valido: '


def get_index(num_index: str) -> Any:
    '''
    Función que recibe un parametro y lo utiliza como
    indice para mostrar un item en la lista medios_transporte
    en el caso de generara alguna excepcion, tiene que volver a
    ingresar un parametro valido.

    :param num_index: parametro que se usara como indice
    :type num_index: str
    '''
    try:
        print(f'\n[+] Eligio -> {medios_transporte[int(num_index)].upper()}\n')
    except IndexError as ex:
        # Error poruqe puede ser mayor que el tamaño de la lista
        # o es negativo
        print(f'\n[!] Error -> {ex}\n')
        num_index = input(default_msg)
        get_index(num_index)
    except Exception as ex:
        # Otras excepciones que no estan contempladas.
        print(f'\n[!] Error -> {type(ex)} -> {ex}\n')
        num_index = input(default_msg)
        get_index(num_index)
    else:
        # Sino entra en excepcion tiene la opcion de seguir o cortar el script
        if input('\n[!] Seguir?? y/n: ') == 'y':
            num_index = input('\n[**] Ingrese numero para mostrar: ')
            get_index(num_index)


if __name__ == '__main__':
    # Comenzando
    num_index = input('[**] Ingrese numero para mostrar: ')
    get_index(num_index)
