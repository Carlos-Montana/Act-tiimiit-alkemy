import unittest
from calculadora import Calculadora


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


if __name__ == '__main__':
    unittest.main()
