from pylatex import Math
from pylatex.utils import NoEscape
import sympy

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import Oracle

# Problem Classes
class FractionAdditionProblem(ProblemToFind):
	"""
	FractionAdditionProblem - find the sum of a sequence of rational numbers 
	"""

	# Initialization
	def __init__(self):
		super().__init__()
		self.condition = "The sum of rational numbers"

	# Behavior
	def new_data(self,quantity=2,dmin=2,dmax=10,nmin=1,nmax=10):
		self.data = []
		for _ in range(quantity):
			self.data.append(self.oracle.randfrac_complexity(dmin,dmax,nmin,nmax))

	def evaluate(self):
            self.unknown = sum(self.data)

	# Output
	def question(self):
		representation = ""
		if len(self.data) > 1:
			representation += self.formatter.rational(self.data[0].p,self.data[0].q)
			for x in range(len(self.data)-1):
                            representation += " + "+self.formatter.rational(self.data[x+1].p,self.data[x+1].q)
		else:
			representation = 'Error'
		return Math(data=NoEscape(representation))

	def answer(self):
		return Math(data=NoEscape(self.formatter.rational(self.unknown.p,self.unknown.q)))

class FractionArithmeticProblem(ProblemToFind):

	def __init__(self):
		super().__init__()
		self.condition = "Rational numbers and arithmetic operations"

	def new_data(self,fractions=2,dmin=2,dmax=10,nmin=1,nmax=10):
		self.data = []
		self.data.append(self.oracle.randfrac_complexity(dmin,dmax,nmin,nmax))
		for x in range(1,fractions):
			self.data.append(self.oracle.random_operator(top=3))
			self.data.append(self.oracle.randfrac_complexity(dmin,dmax,nmin,nmax))

	def evaluate(self):
		expr = ''
		for x in range(len(self.data)):
			if x % 2 == 0:
				expr += ' '+str(self.data[x].p)+'/'+str(self.data[x].q)+' '
			else:
				expr += self.oracle.sympy_string_operand(self.data[x])
		self.unknown = sympy.S(expr)

	def question(self):
		expr = ''
		for x in range(len(self.data)):
			if x % 2 == 0:
				expr += self.formatter.rational(self.data[x].p,self.data[x].q)
			else:
				expr += self.formatter.latex_string_operand(self.data[x])
		return Math(data=NoEscape(expr))

	def answer(self):
		return Math(data=NoEscape(self.formatter.rational(self.unknown.p,self.unknown.q)))
