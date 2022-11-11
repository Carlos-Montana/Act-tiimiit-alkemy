# Practicando logs
# crear ambientes virtuales --> python3 -m virtualenv path y
# nombre_de_ambiente o
# virtualenv path y nombre_de_ambiente
import logging
from time import sleep
# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# formatter
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d')
# filehandler
fh = logging.FileHandler('./src/results.log')
fh.setLevel(logging.INFO)
fh.setFormatter(log_format)
# treamhandler
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(log_format)
# agregando handleres al logger
logger.addHandler(fh)
logger.addHandler(sh)

# probando logs
fruits = ['Frutilla', 'Melón', 'PERA', 99.6, 'NaranJA', 'mORa', 'NisPERo', 99]

print('Usando for/if')
for fruit in fruits:
    if type(fruit) is str:
        logger.info(f'Conversión fue exitosa: {fruit} --> {fruit.lower()}')
    else:
        logger.error(f"conversión fallida: {fruit}")
sleep(2)

print('Usando try/except')
for fruit in fruits:
    try:
        logger.info(f'Conversión fue exitosa: {fruit} --> {fruit.lower()}')
    except Exception:
        logger.error(f"conversión fallida: {fruit}")
