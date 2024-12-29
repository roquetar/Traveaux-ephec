import unittest
from tp7 import Fraction


class FractionTestCase(unittest.TestCase):
    """Extended unit tests for the Fraction class."""

    def test_initialization(self):
        """Test initialization of a fraction."""
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3, "Numerator should be 3")
        self.assertEqual(f.denominator, 4, "Denominator should be 4")

    def test_initialization_error(self):
        with self.assertRaises(Exception, msg="Denominator cannot be zero"):
            Fraction(3, 0)

    def test_setters(self):
        f = Fraction(3, 4)
        f.numerator = 5
        self.assertEqual(f.numerator, 5, "Numerator should be 5")
        f.denominator = 6
        self.assertEqual(f.denominator, 6, "Denominator should be 6")

    def test_str(self):
        """Test string representation of a fraction."""
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2", "String representation should be '1/2' after simplification")

    def test_as_mixed_number(self):
        """Test conversion to mixed number."""
        f = Fraction(5, 2)
        self.assertEqual(f.as_mixed_number(), "2 + 1/2", "Mixed number should be '2 + 1/2'")

    def test_addition(self):
        """Test addition of two fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5, "Numerator should be 5 after addition")
        self.assertEqual(result.denominator, 6, "Denominator should be 6 after addition")

    def test_addition_int(self):
        f1 = Fraction(1, 2)
        result = f1 + 2
        self.assertEqual(result.numerator, 5, "Numerator should be 3 after addition")
        self.assertEqual(result.denominator, 2, "Denominator should be 2 after addition")

    def test_addition_error(self):
        with self.assertRaises(TypeError, msg="Addition requires a Fraction"):
            Fraction(1, 2) + "1"

    def test_subtraction(self):
        """Test subtraction of two fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1, "Numerator should be 1 after subtraction")
        self.assertEqual(result.denominator, 3, "Denominator should be 3 after subtraction")

    def test_subtraction_int(self):
        """Test subtraction of two fractions."""
        f1 = Fraction(2, 3)
        result = f1 - 2
        self.assertEqual(result.numerator, -4, "Numerator should be 1 after subtraction")
        self.assertEqual(result.denominator, 3, "Denominator should be 3 after subtraction")

    def test_subtraction_error(self):
        with self.assertRaises(TypeError, msg="Subtraction requires a Fraction"):
            Fraction(2, 3) - "2"

    def test_multiplication(self):
        """Test multiplication of two fractions."""
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        result = f1 * f2
        self.assertEqual(result.numerator, 3, "Numerator should be 6 after multiplication")
        self.assertEqual(result.denominator, 10, "Denominator should be 20 after multiplication")

    def test_multiplication_int(self):
        """Test multiplication of two fractions."""
        f1 = Fraction(3, 4)
        result = f1 * 2
        self.assertEqual(result.numerator, 3, "Numerator should be 6 after multiplication")
        self.assertEqual(result.denominator, 2, "Denominator should be 20 after multiplication")

    def test_multiplication_error(self):
        with self.assertRaises(TypeError, msg="Multiplication requires a Fraction"):
            Fraction(3, 4) * "2"

    def test_division(self):
        """Test division of two fractions."""
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        result = f1 / f2
        self.assertEqual(result.numerator, 15, "Numerator should be 15 after division")
        self.assertEqual(result.denominator, 8, "Denominator should be 8 after division")

    def test_division_error(self):
        with self.assertRaises(ZeroDivisionError, msg="Division by zero"):
            Fraction(3, 4) / Fraction(0, 1)

    def test_power(self):
        """Test exponentiation of a fraction."""
        f = Fraction(2, 3)
        result = f ** 2
        self.assertEqual(result.numerator, 4, "Numerator should be 4 after exponentiation")
        self.assertEqual(result.denominator, 9, "Denominator should be 9 after exponentiation")

    def test_power_error(self):
        with self.assertRaises(TypeError, msg="Exponentiation requires an integer"):
            Fraction(2, 3) ** Fraction(1, 2)

    def test_equality(self):
        """Test equality of two fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 6)
        self.assertTrue(f1 == f2, "Fractions should be equal")

    def test_equality_error(self):
        with self.assertRaises(AttributeError, msg="Equality requires a Fraction"):
            Fraction(2, 3) == 1

    def test_inequality(self):
        """Test inequality of two fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertTrue(f1 != f2, "Fractions should not be equal")

    def test_less_than(self):
        """Test less-than comparison."""
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 < f2, "Fraction 1/3 should be less than 1/2")

    def test_less_than_or_equal(self):
        """Test less-than-or-equal comparison."""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 <= f2, "Fraction 1/2 should be less than or equal to 2/4")

    def test_greater_than(self):
        """Test greater-than comparison."""
        f1 = Fraction(2, 3)
        f2 = Fraction(1, 3)
        self.assertTrue(f1 > f2, "Fraction 2/3 should be greater than 1/3")

    def test_greater_than_or_equal(self):
        """Test greater-than-or-equal comparison."""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        self.assertTrue(f1 >= f2, "Fraction 3/4 should be greater than or equal to 6/8")

    def test_float_conversion(self):
        """Test float conversion of a fraction."""
        f = Fraction(3, 4)
        self.assertAlmostEqual(float(f), 0.75, msg="Float value should be 0.75")

    def test_int_conversion(self):
        """Test int conversion of a fraction."""
        f = Fraction(9, 4)
        self.assertEqual(int(f), 2, "Integer value should be 2 after conversion")

    def test_round(self):
        """Test rounding of a fraction."""
        f = Fraction(3, 7)
        self.assertEqual(round(f, 2), 0.43, "Rounded value should be 0.43 to 2 decimal places")

    def test_is_zero(self):
        """Test if a fraction is zero."""
        f = Fraction(0, 5)
        self.assertTrue(f.is_zero(), "Fraction 0/5 should be zero")

    def test_is_integer(self):
        """Test if a fraction is an integer."""
        f = Fraction(4, 2)
        self.assertTrue(f.is_integer(), "Fraction 4/2 should be an integer")

    def test_is_proper(self):
        """Test if a fraction is proper."""
        f = Fraction(1, 2)
        self.assertTrue(f.is_proper(), "Fraction 1/2 should be proper")

    def test_is_unit(self):
        """Test if a fraction is a unit fraction."""
        f = Fraction(1, 3)
        self.assertTrue(f.is_unit(), "Fraction 1/3 should be a unit fraction")

    def test_is_adjacent_to(self):
        """Test if two fractions are adjacent."""
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 4)
        self.assertTrue(f1.is_adjacent_to(f2), "Fractions 1/3 and 1/4 should be adjacent")

    def test_is_not_adjacent_to(self):
        """Test if two fractions are not adjacent."""
        f1 = Fraction(2, 3)
        f2 = Fraction(1, 4)
        self.assertFalse(f1.is_adjacent_to(f2), "Fractions 2/3 and 1/4 should not be adjacent")

    def test_simplify(self):
        """Test simplification of a fraction."""
        f = Fraction(4, 8)
        f.simplify()
        self.assertEqual(f.numerator, 1, "Numerator should be 1 after simplification")
        self.assertEqual(f.denominator, 2, "Denominator should be 2 after simplification")

    def test_simplify_error(self):
        with self.assertRaises(ValueError, msg="Cannot simplify zero denominator"):
            Fraction(0, 0).simplify()

    def test_simplify_negative(self):
        f = Fraction(3, -5)
        f.simplify()
        self.assertEqual(f.numerator, -3, "Numerator should be -3 after simplification")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
