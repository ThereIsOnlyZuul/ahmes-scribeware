from pylatex import Math
from pylatex.utils import NoEscape
import sympy

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import NumberType

class DefiniteIntegralProblem(ProblemToFind):

	def __init__(self):
		super().__init__()
		self.a = 0 # the lower bound of integration
		self.b = 1 # the upper bound of integration
		self.expression = None
		self.variable = sympy.symbols('x')

	def new_data(self,integrand_template,c_min=0,c_max=10):
		for c in integrand_template.constants:
			c.value(self.oracle.randint(10))
		self.expression = integrand_template.express(self.variable)

	def evaluate(self):
		self.unknown = sympy.integrate(self.expression,self.variable,(self.a,self.b))

	def set_bounds_of_integration(self,lower_bound,upper_bound):
		self.a = lower_bound
		self.b = upper_bound