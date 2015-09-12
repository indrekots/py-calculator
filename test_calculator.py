import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

  def test_add_two_numbers(self):
      calc = Calculator()
      self.assertEqual(calc.calculate("2+2"), 4, "Should equal 4")

  def test_subtract(self):
      calc = Calculator()
      self.assertEqual(calc.calculate("4-1"), 3, "Should equal 3")

if __name__ == '__main__':
    unittest.main()
