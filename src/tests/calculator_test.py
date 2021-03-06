import unittest
from entities.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.calc("5","+","5"),10)
    
    def test_addition_neg(self):
        self.assertEqual(self.calculator.calc("5","+","-4"),1)

    def test_addition_dot(self):
        self.assertEqual(self.calculator.calc("5.2","+","1.2"),6.4)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calc("5","-","5"),0)
    
    def test_subtraction_neg(self):
        self.assertEqual(self.calculator.calc("5","-","-4"),9)

    def test_subtraction_dot(self):
        self.assertEqual(self.calculator.calc("5.1","-","4.1"),1)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calc("5","*","5"),25)

    def test_multiplication_dot(self):
        self.assertEqual(self.calculator.calc("5.2","*","5"),26.0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calc("5","*","-5"),-25)
    
    def test_division(self):
        self.assertEqual(self.calculator.calc("5","/","5"),1)

    def test_division(self):
        self.assertEqual(self.calculator.calc("6.4","/","2"),3.2)

    def test_division(self):
        self.assertEqual(self.calculator.calc("10","/","-5"),-2)
       
    def test_division_zero(self):
        self.assertEqual(self.calculator.calc("5","/","0"),"Please don't divide by zero")

    def test_incorrect_input(self):
        self.assertEqual(self.calculator.calc("5","/","/0"),"Please use correct expression format")

    def test_incorrect_input(self):
        self.assertEqual(self.calculator.calc("5.5","/","0"),"Please don't divide by zero")

    def test_incorrect_input(self):
        self.assertEqual(self.calculator.calc("5.5","/","0"),"Please don't divide by zero")
