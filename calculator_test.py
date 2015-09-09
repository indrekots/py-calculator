import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

  def test_add_two_numbers(self):
      calc = Calculator()
      self.assertEqual(calc.calculate("2+2"), 4, "Should equal 4")

if __name__ == '__main__':
    unittest.main()
