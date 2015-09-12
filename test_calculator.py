import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

  def setUp(self):
      self.calc = Calculator()

  def test_add_two_numbers(self):
      self.assertEqual(self.calc.calculate("2+2"), 4, "Should equal 4")

  def test_subtract(self):
      self.assertEqual(self.calc.calculate("4-1"), 3, "Should equal 3")

  def test_add_and_subtract(self):
      self.assertEqual(self.calc.calculate("4+3-1"), 6, "Should equal 6")

  def test_calculate_with_spaces(self):
      self.assertEqual(self.calc.calculate("4 - 3   +1"), 2, "Should equal 2")

  def test_raise_exception_when_unmatching_subtraction_operand(self):
      with self.assertRaises(RuntimeError) as ex:
          self.calc.calculate("3+2-")

      self.assertEqual(ex.exception.message, "Subtraction requires 2 operands")

  def test_raise_exception_when_unmatching_addition_operand(self):
      with self.assertRaises(RuntimeError) as ex:
          self.calc.calculate("3-2+")

      self.assertEqual(ex.exception.message, "Addition requires 2 operands")

if __name__ == '__main__':
    unittest.main()
