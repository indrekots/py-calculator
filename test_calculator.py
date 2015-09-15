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

  def test_calculate_with_one_operand(self):
      self.assertEqual(self.calc.calculate("5"), 5, "Should equal 5")

  def test_calculate_with_missing_operator(self):
      with self.assertRaises(RuntimeError) as ex:
          self.calc.calculate("2 5")

      self.assertEqual(ex.exception.message, "Input has too many values")

  def test_raise_exception_when_no_operands_or_operators_found(self):
      with self.assertRaises(RuntimeError) as ex:
          self.calc.calculate("gibberish")

      self.assertEqual(ex.exception.message, "No operands or operators provided")

  def test_multiplication(self):
      self.assertEqual(self.calc.calculate("3 * 3"), 9, "Should equal 9")

  def test_add_subtract_and_multiply(self):
      self.assertEqual(self.calc.calculate("3-2*5"), -7, "Should equal -7")
      self.assertEqual(self.calc.calculate("3+2*5-3*10"), -17, "Should equal -17")

  def test_division(self):
      self.assertEqual(self.calc.calculate("6/2"), 3, "Should equal 3")

  def test_divide_and_multiply(self):
      self.assertEqual(self.calc.calculate("6/2*4"), 12, "Should equal 12")

  def test_add_subtract_and_divide(self):
      self.assertEqual(self.calc.calculate("6-4/2"), 4, "Should equal 4")

  def test_add_subtract_multiply_and_divide(self):
      self.assertEqual(self.calc.calculate("4-6/2+4*2"), 9, "Should equal 9")

  def test_calculate_with_parenthesis(self):
      self.assertEqual(self.calc.calculate("2*(3+5)"), 16, "Should equal 16")

  def test_raise_exception_when_missing_right_parenthesis(self):
      with self.assertRaises(RuntimeError) as ex:
          self.calc.calculate("2*(3+5")

      self.assertEqual(ex.exception.message, "Mismatching parenthesis")

  def test_raise_exception_when_missing_left_parenthesis(self):
      with self.assertRaises(RuntimeError) as ex:
          self.calc.calculate("2*3+5)")

      self.assertEqual(ex.exception.message, "Mismatching parenthesis")

  def test_raise_to_power(self):
      self.assertEqual(self.calc.calculate("2^2"), 4, "Should equal 4")
      self.assertEqual(self.calc.calculate("2^2*5"), 20, "Should equal 20")
      self.assertEqual(self.calc.calculate("5-2^2*5"), -15, "Should equal -15")

if __name__ == '__main__':
    unittest.main()
