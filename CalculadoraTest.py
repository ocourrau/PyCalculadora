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

    def testResta(self):
        num1 = int(input('Ingrese un numero '))
        num2 = int(input('Ingrese un numero '))
        self.assertEqual(calc.resta(num1,num2),6)

    def testMultiplicacion(self):
        num1 = int(input('Ingrese un numero '))
        num2 = int(input('Ingrese un numero '))
        self.assertEqual(calc.multiplicacion(num1,num2),8)

    def testDivision(self):
        num1 = int(input('Ingrese un numero '))
        num2 = int(input('Ingrese un numero '))
        self.assertEqual(calc.division(num1,num2),10)

if __name__ == '__main__':
    unittest.main()
