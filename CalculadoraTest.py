from entities import Calculadora
import unittest

calc = Calculadora()

class CalculadoraTest(unittest.TestCase):
    def setup(self):
        pass

    def testSum(self):
        num1 = int(input('Ingrese un numero '))
        num2 = int(input('Ingrese otro numero '))
        self.assertEqual(calc.suma(num1,num2),4)

if __name__ == '__main__':
    unittest.main()
