# Aca desarrollare la parte del main donde llamo
# a la function para que cuente palabras y renglones
import logging
import logging.config
from function import count_words

# main


def main(nombre_path: str) -> any:
    '''
    Función principal donde abro el archivos y posteriormente
    llamo a la función count_words.

    :param nombre_path: nombre del archivo
    :type nombre_path: str
    '''
    try:
        logger.info('...Leyendo el archivo...')
        with open(nombre_path, 'r') as file:
            archivo = file.read()
            count_words(archivo, nombre_path)
        logger.info('Archivo Procesado Correctamente')

    except OSError:
        logger.error('No se puedo abrir el archivo')


if __name__ == '__main__':
    # abriendo archivo de configuración
    logging.config.fileConfig('log_config_file.conf')
    # creando logger
    logger = logging.getLogger('main')
    nombre_path = 'cuento.txt'
    main(nombre_path)
