from enum import Enum
from random import Random

from mpmath import floor, ceil, nint
from sympy import Rational, sqrt

class Oracle(Random):
	"""
	Oracle.py - This is the object that knows how to deal with numbers
	"""

	def __init__(self):
		super().__init__()

	# Random Number Generating Functions

	def randint_nonmultiple(self,min,max,nonmultiple):
		number = self.randint(min,max)
		while number % nonmultiple == 0:
			number = self.randint(min,max)
		return number

	# Number Theory Functions

	def round(self,decimal,decimal_places):
		enlarged = decimal * 10 ** (decimal_places)
		if enlarged - floor(enlarged) == 0.5:
			enlarged = ceil(enlarged)
		else:
			enlarged = nint(enlarged)
		return enlarged / 10.0 ** decimal_places

	def babylonian_root(self,radicand,guess):
		'''Given a radicand and a guess, produce a better guess'''
		return (guess + radicand / guess) / 2

	def square_root_guess(self,radicand,number_type,precision):
		return {
			NumberType.RATIONAL:
				Rational(sqrt(radicand).evalf(precision)).limit_denominator(precision),
			NumberType.INTEGER:
				sqrt(radicand).evalf(0),
			NumberType.REAL:
				self.round(sqrt(radicand).evalf(precision+2),precision)
		}[number_type]

	def is_square(self,number):
		'''Determine if the number is a perfect square'''
		if number == 1:
			return True
		elif number < 4:
			return False
		x = number // 2
		seen = set([x])
		while x * x != number:
			x = (x + (number // x)) // 2
			if x in seen:
				return False
			seen.add(x)
		return True

class NumberType(Enum):
	RATIONAL = 'R'
	INTEGER = 'Z'
	REAL = 'Q'