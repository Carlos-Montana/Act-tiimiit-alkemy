import functions.calculadora as c
import os
import sys
import unittest
from pathlib import Path
# setup del docs-from-tests -> pip install docs-from-tests
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)
# Get the path to load package or module,
# for example the calculadora
ruta = str(Path.cwd().parent)
sys.path.append(ruta)

# here loads the modules or packages
# function que contiene calculadora y function
instrument_and_import_package(
    os.path.join(
        Path(__file__).parent.absolute(), '..', 'functions'
        ), 'functions')


class MyTest(unittest.TestCase):
    '''
    This class check tests in calculadora and write
    one archive markdown how output

    :param unittest: TestCase
    :type unittest: unittest.TestCase
    '''

    def test_calculadora(self):
        '''
        Check oparation in calculadora and
        write archive .md how output
        '''
        # begin
        initialise_call_hierarchy('start')

        # set of tests
        # ##add##
        # self.assertEqual(c.Calculadora.add(1, 2, 3), 6)
        self._test_prueba()
        # ##multiplication##
        self.assertEqual(c.Calculadora.multiplication(1, 2, 3), 6)
        # ##substract##
        self.assertEqual(c.Calculadora.substract(10, 5), 5)
        self.assertEqual(c.Calculadora.substract(10, 5, 5), 0)
        # ##divide##
        self.assertEqual(c.Calculadora.divide(8, 2), 4)
        # NOTA -> los assertRaises no lo maneja docs-from-tests

        # finally
        root_call = finalise_call_hierarchy()

        # The sequence diagram is returned
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Write the archive
        sequence_diagram_filename = Path(
            Path.cwd().parent, 'docs', 'diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def _test_prueba(self):
        '''
        Probando si se puede poner en un funcion aparte
        Testing if it can be put in a separate function
        '''
        self.assertEqual(c.Calculadora.add(1, 2, 3), 6)


if __name__ == '__main__':
    unittest.main()
