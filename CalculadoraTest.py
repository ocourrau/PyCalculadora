from entities import Calculadora
import unittest

calc = Calculadora()

class CalculadoraTest(unittest.TestCase):
    def setup(self):
        pass

    def testSum(self):
        num1 = int(input('Ingrese un numero a sumar '))
        num2 = int(input('Ingrese otro numero a sumar '))
        self.assertEqual(calc.suma(num1,num2),4)

    def testSubtract(self):
        num1 = int(input('Ingrese un numero a restar '))
        num2 = int(input('Ingrese otro numero a restar '))
        self.assertEqual(calc.resta(num1,num2),6)

    def testMultiply(self):
        num1 = int(input('Ingrese un numero a multiplicar '))
        num2 = int(input('Ingrese otro numero a multiplicar '))
        self.assertEqual(calc.multiplicacion(num1,num2),8)

    def testDivide(self):
        num1 = int(input('Ingrese un numero a dividir '))
        num2 = int(input('Ingrese otro numero a dividir '))
        self.assertEqual(calc.division(num1,num2),10)

if __name__ == '__main__':
    unittest.main()
