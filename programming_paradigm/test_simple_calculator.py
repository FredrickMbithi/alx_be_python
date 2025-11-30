import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Prepare a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # -------------------------
    # Addition Tests
    # -------------------------
    def test_addition(self):
        """Test addition with normal numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_addition_edge_cases(self):
        """Test addition edge cases like floats and zeros."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # -------------------------
    # Subtraction Tests
    # -------------------------
    def test_subtraction(self):
        """Test subtraction with normal numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_subtraction_edge_cases(self):
        """Test subtracting floats and zeros."""
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # -------------------------
    # Multiplication Tests
    # -------------------------
    def test_multiplication(self):
        """Test multiplication with normal numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_edge_cases(self):
        """Test multiplying floats and zeros."""
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    # -------------------------
    # Division Tests
    # -------------------------
    def test_division(self):
        """Test normal division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(5.0, 2), 2.5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_edge_cases(self):
        """Test odd cases to ensure stability."""
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(100, -10), -10)


if __name__ == '__main__':
    unittest.main()
