from functions.calculadora import Calculadora
import unittest
import sys
import datetime
from pathlib import Path
ruta = Path.cwd().parent
ruta = str(ruta)
sys.path.append(ruta)


class TestCalculadora(unittest.TestCase):
    '''
    This class tests the operation of the calculator

    :param unittest: class test
    :type unittest: TestCase
    '''
    # Addition
    def test_add_is_equal(self):
        '''
        Test that the sum is correct
        '''
        self.assertEqual(Calculadora.add(1, 2, 3), 6)

    def test_checking_is_not_numeric(self):
        '''
        Test that arguments are numerical
        '''
        self.assertRaises(AssertionError, Calculadora.add, 1, 2, 'hola')

    def test_add_negative(self):
        '''
        Test that the sum of negatives numbers is correct
        '''
        self.assertEqual(Calculadora.add(-1, 2, -3), -2)

    def test_add_arguments_more_two(self):
        '''
        check if numbers arguments is more than 2
        '''
        self.assertRaises(AssertionError, Calculadora.add, 1)

    # Multiplication
    def test_multiplication_is_equal(self):
        '''
        Test that the multiplication is correct
        '''
        self.assertEqual(Calculadora.multiplication(1, 2, 3), 6)

    def test_checking_multiplication_is_not_numeric(self):
        '''
        Test that arguments are numerical
        '''
        self.assertRaises(AssertionError, Calculadora.multiplication, 2, 'foo')

    def test_multiplication_negative(self):
        '''
        Test that the sum of negatives numbers is correct
        '''
        self.assertEqual(Calculadora.multiplication(1, 2, -3), -6)

    def test_multiplication_arguments_more_two(self):
        '''
        check if numbers arguments is more than 2
        '''
        self.assertRaises(AssertionError, Calculadora.multiplication, 1)

    # # Substract
    def test_substract_is_equal(self):
        '''
        Test that the multiplication is correct
        '''
        self.assertEqual(Calculadora.substract(10, 5), 5)
        self.assertEqual(Calculadora.substract(10, 5, 5), 0)

    def test_checking_if_substraction_is_not_numeric(self):
        '''
        Test that arguments are numerical
        '''
        self.assertRaises(AssertionError, Calculadora.substract, 1, 5, 'foo')

    def test_substraction_negative(self):
        '''
        Test that the substract of negatives numbers is correct
        '''
        self.assertEqual(Calculadora.substract(-1, -5), 4)
        self.assertEqual(Calculadora.substract(-1, 5), -6)

    def test_substract_is_empty(self):
        '''
        Test that the lista of arguments is empty
        '''
        self.assertRaises(AssertionError, Calculadora.substract,)
        # check if numbers arguments is more than 2
        self.assertRaises(AssertionError, Calculadora.substract, 1)

    # # Divide
    def test_divide_is_equal(self):
        '''
        Test that the multiplication is correct
        '''
        self.assertEqual(Calculadora.divide(8, 2), 4)

    def test_checking_is_not_numeric_div(self):
        '''
        Test that arguments are numerical
        '''
        self.assertRaises(AssertionError, Calculadora.divide, 8, 2, 'hola')

    def test_checking_if_divisor_is_zero(self):
        '''
        Test that arguments are numerical
        '''
        self.assertRaises(AssertionError, Calculadora.divide, 8, 2, 0)


# Writing archive .txt
def insert_header(f):
    f.write('\n')
    f.write('******************TESTING**************************')
    f.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f.write(date_time)
    f.write('\n')
    return f


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('testing.txt', 'a') as f:
        f = insert_header(f)
        main(f)
