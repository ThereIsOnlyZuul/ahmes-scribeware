import unittest
from fractions import Fraction

from sympy import Rational, sqrt

from Oracle.oracle import Oracle, NumberType

test_oracle = Oracle()

class OracleTest(unittest.TestCase):


	# Number Theory

	## Rounding

	def test_round_down(self):
		self.assertEqual(test_oracle.round(3.141592,2),3.14)

	def test_round_up(self):
		self.assertEqual(test_oracle.round(3.141592,4),3.1416)

	## Perfect Squares
	def test_is_square_pass(self):
		for x in range(1234567891011121314151617181920,1234567891011121314151617181950):
			self.assertTrue(test_oracle.is_square(x**2))

	def test_is_square_fail(self):
		self.assertFalse(test_oracle.is_square(152415789666209426002111556165263283035677490))

	def test_is_square_negative(self):
		self.assertFalse(test_oracle.is_square(-1))

	def test_square_root_one(self):
		self.assertTrue(test_oracle.is_square(1))

	def test_square_root_primes(self):
		primes = [2,3,5,7,11,13,17,23]
		for x in primes:
			self.assertFalse(test_oracle.is_square(x))

	## Babylonian Roots
	def test_babylonian_root(self):
		self.assertEqual(test_oracle.babylonian_root(3,Fraction(7,4)),Fraction(97,56))

	def test_square_root_guess_rational(self):
		result = test_oracle.square_root_guess(3,NumberType.RATIONAL,5)
		self.assertEqual(Rational(7,4),result)

	def test_square_root_guess_integer(self):
		result = test_oracle.square_root_guess(50,NumberType.INTEGER,66)
		self.assertEqual(result,7)

	def test_square_root_guess_real(self):
		result = test_oracle.square_root_guess(5,NumberType.REAL,2)
		self.assertEqual(result,2.24)