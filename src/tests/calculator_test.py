import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=Calculator()

    def test_plussa_toimii(self):
        self.assertEqual(self.calculator.calc("5+5"),10)

    def test_miinus_toimii(self):
        self.assertEqual(self.calculator.calc("5-5"),0)

    def test_kerto_toimii(self):
        self.assertEqual(self.calculator.calc("5*5"),25)
    
    def test_jako_toimii(self):
        self.assertEqual(self.calculator.calc("5/5"),1)
