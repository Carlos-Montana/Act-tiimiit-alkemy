# Practica de testing unidad 10, hare una calculadora.
import logging

# ##Loggings## #
# logger
logger = logging.getLogger('Calculadora')
logger.setLevel(logging.INFO)
# Formatter
fm = logging.Formatter('%(asctime)s - %(name)s - \
%(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# StreamHandler
st = logging.StreamHandler()
st.setLevel(logging.INFO)
st.setFormatter(fm)
# FileHandler
fh = logging.FileHandler('./logs/test.log')
fh.setLevel(logging.INFO)
fh.setFormatter(fm)
# Agregando handlers
# logger.addHandler(st)
logger.addHandler(fh)


class Calculadora:
    '''
    This class resolved simples operations -> addition, subtraction,
    division, multiplication
    '''
    def add(*args: float) -> float:
        '''
        This method return the sums of arguments

        :return: sums of arguments obteined
        :rtype: float
        '''
        logger.info('Addition numbers')
        sum = 0
        try:
            # check if numbers arguments is more than 2
            assert len(args) >= 2, 'Insuficientes argumentos'
            for num in args:
                # check if item is numeric
                assert type(num) != str,\
                    'Es un string, no se puede realizar operacion'
                sum += num
        except AssertionError as ex:
            logger.error(ex)
            raise (ex)
        else:
            return sum

    def multiplication(*args: float) -> float:
        '''
        This method return the multiplication of arguments

        :return: multiplication of arguments obteined
        :rtype: float
        '''
        logger.info('Multiplication numbers')
        mult = 1
        try:
            # check if numbers arguments is more than 2
            assert len(args) >= 2, 'Insuficientes argumentos'
            for num in args:
                # check if item is numeric
                assert type(num) != str,\
                    'Es un string, no se puede realizar operacion'
                mult *= num
        except AssertionError as ex:
            logger.error(ex)
            raise (ex)
        else:
            return mult

    def substract(*args: float) -> float:
        '''
        This method return subtraction of arguments received

        :return: subtract of arguments obteined
        :rtype: float
        '''
        logger.info('Subtraction numbers')
        try:
            # check if numbers arguments is more than 2
            assert len(args) >= 2, 'La lista no tiene los arguments necesarios'
            # check if args not is empty
            args = list(args)
            subs = args.pop(0)
            for num in args:
                # check if item is numeric
                assert type(num) != str,\
                    'Es un string, no se puede realizar operacion'
                subs -= num
        except AssertionError as ex:
            raise (ex)
        else:
            return subs

    def divide(*args: float) -> float:
        '''
        This method return division of arguments received

        :return: division of arguments obteined
        :rtype: float
        '''
        logger.info('Division numbers')
        try:
            # check if numbers arguments is more than 2
            assert len(args) >= 2, 'Insuficientes argumentos'
            # check if args no is empty
            args = list(args)
            div = args.pop(0)
            for num in args:
                # check if divisor es zero
                assert num != 0, ZeroDivisionError.__doc__
                # check if item is numeric
                assert type(num) != str,\
                    'Es un string, no se puede realizar operacion'
                div /= num
        except AssertionError as ex:
            raise (ex)
        else:
            return div
