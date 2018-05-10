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