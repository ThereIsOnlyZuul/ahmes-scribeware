from enum import Enum

from pylatex import Math
from pylatex.utils import NoEscape
import sympy
from sympy.ntheory.egyptian_fraction import egyptian_fraction as egypt

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection


class EgyptianFractionType(Enum):
	PROPER = 1 # A fraction p/q where p > 2 and q > p
	IMPROPER = 2 # a fraction p/q where q > 1 p > q
	ERDOS_STRAUSS = 3 # a fraction 4/q where q > 4

class EgyptianFractionsProblem(ProblemToFind):

	def __init__(self):
		super().__init__()

	def new_data(self,fraction_type=EgyptianFractionType.PROPER,max_component=50):
		numerator = self.oracle.randint(2,max_component-1)
		if fraction_type.name == 'IMPROPER':
			denominator = self.oracle.randint(2,numerator)
		else:
			denominator = self.oracle.randint_nonmultiple(numerator,max_component,numerator)
		if fraction_type.name == 'ERDOS_STRAUSS':
			numerator = 4 # the numerator is always four in an Erdos-Strauss Fraction
			# For the next line, we must make sure that the denominator is not even, or the fraction will reduce
			denominator = self.oracle.randint_nonmultiple(numerator,max_component,2)
		self.data = sympy.Rational(numerator,denominator)


	def evaluate(self):
		self.unknown = [sympy.Rational(1,x) for x in egypt(self.data)]

	def question(self):
		return Math(data=[NoEscape(sympy.latex(self.data))])

	def answer(self):
		return Math(data=self.formatter.separate_list_items([NoEscape(sympy.latex(x)) for x in self.unknown],','))