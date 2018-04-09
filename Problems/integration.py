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
		for c in integrand_template.find_constants():
			c.value(self.oracle.randint(c_min,c_max))
		self.expression = integrand_template.express(self.variable)

	def evaluate(self):
		self.unknown = sympy.integrate(self.expression,(self.variable,self.a,self.b))

	def set_bounds_of_integration(self,lower_bound,upper_bound):
		self.a = lower_bound
		self.b = upper_bound

	def random_bounds_of_integration(self,min,max):
		self.a = self.oracle.randint(min,max-1)
		self.b = self.oracle.randint(self.a+1,max)
		
	def question(self):
		return Math(data=[NoEscape(self.formatter.definite_integral(self.a,self.b,
			sympy.latex(self.expression),sympy.latex(self.variable)))])

	def answer(self):
		return Math(data=[NoEscape(sympy.latex(self.unknown))])