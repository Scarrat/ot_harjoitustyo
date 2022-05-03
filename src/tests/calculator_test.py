import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.calc_basic("5+5"),10)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calc_basic("5-5"),0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calc_basic("5*5"),25)
    
    def test_division(self):
        self.assertEqual(self.calculator.calc_basic("5/5"),1)

    def test_addition_base(self):
        self.assertEqual(self.calculator.addition(5,5),10)

    def test_subtraction_base(self):
        self.assertEqual(self.calculator.subtraction(5,5),0)

    def test_multiplication_base(self):
        self.assertEqual(self.calculator.multiplication(5,5),25)
    
    def test_division_base(self):
        self.assertEqual(self.calculator.division(5,5),1)
        
    def test_division_zero(self):
        self.assertEqual(self.calculator.calc_basic("5/0"),0)

