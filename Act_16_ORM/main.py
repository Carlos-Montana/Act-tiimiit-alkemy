'''
Aca se podran realizar las diferentes opeacions sobre
las tablas mapeadas, en este caso es una llamada
customer.
'''
import logging
import logging.config
from db import session
from models import Customer

# abriendo archivo de configuración
logging.config.fileConfig('logs.conf')
# creando logger
logger = logging.getLogger('main')


def save_info(
        name: str, age: int, email: str, address: str, zip_code: int) -> None:
    '''
    Función para guardar un registro en la base de datos
    '''
    # Crear un nuevo objeto/registro
    try:
        new_item = Customer(name, age, email, address, zip_code)
        session.add(new_item)
        session.commit()
        session.close()
        logger.info('Datos Guardados.')
    except Exception:
        logger.error(
            'Problemas para agregar items en la base de datos.', exc_info=True)


def update_info() -> None:
    '''
    Función que se encarga de actualizar los registros
    '''
    # En este caso se actualiza el customer con id 3
    try:
        customer_update = session.query(Customer).get(3)
        customer_update.name = 'fulano'
        customer_update.age = 99
        customer_update.email = 'theold@old.com'
        customer_update.address = 'avenida siempre viva'
        customer_update.zip_code = '8899NN'
        session.add(customer_update)
        session.commit()
        session.close()
        logger.info('Registro Actualizado')
    except Exception:
        logger.error('No se pudo actualizar registro', exc_info=True)


def delete_info() -> None:
    '''
    Función para borrar un registro
    '''
    # En este caso se borrara un registro con id 2
    try:
        item_delete = session.query(Customer).get(2)
        session.delete(item_delete)
        session.commit()
        session.close()
        logger.info('Registro borrado exitosamente')
    except Exception:
        logger.error('No se puedo borrar registro', exc_info=True)


def select_info() -> None:
    '''
    Funión para mostrar todos los registros de la db
    '''
    all_data = session.query(Customer).all()
    for data in all_data:
        print(
            f'Customer-> {data.name} / Age-> {data.age} / mail-> {data.email}')
    session.close()


def run() -> None:
    '''
    Esta función se encarga de organizar las distintas
    operaciones como insertar, mostrar, etc.
    '''
    # Creando nuevo registro
    logger.info('Creando registros')
    save_info('honguito', 18, 'honguit@honguito.com', 'nose 14 sur', '234SS')
    save_info('pepito', 25, 'pepito@pepito.com', 'sise 21 este', '5432NS')
    # Mostrar todos los registro de la base de datos
    logger.info('Mostrando registros')
    select_info()
    # Actualizando registro con id 3
    logger.info('Actualizando registro con id 3')
    update_info()
    # Borrando registro con id 2
    logger.info('Borrando registro con id 2')
    delete_info()


if __name__ == '__main__':
    # begin script
    logger.info('Iniciando Script')
    run()
    logger.info('Fin del Script')
