# aca desarrollaremos la parte de contar renglones y palabras
import logging
import logging.config

# abriendo archivo de configuración
logging.config.fileConfig('log_config_file.conf')
# creando el logger
logger = logging.getLogger('functions')


def count_words(file, nombre_path: str) -> any:
    '''
    Función que cuenta renglones y
    cantidad de palabras por renglon

    :param file: archivo abierto
    :type file: file
    :param nombre_path: nombre del archivo
    :type nombre_path: str
    '''
    new_file = file
    # cantidad de renglones
    renglones = new_file.split("\n")
    logger.info(f'{nombre_path} - Cantidad de renglones: {len(renglones)}')
    # cantidad de palabras por renglon
    for n_renglon, renglon in enumerate(renglones):
        cword = renglon.split(" ")
        logger.info(f'Renglón {n_renglon+1}: {len(cword)} palabras')
