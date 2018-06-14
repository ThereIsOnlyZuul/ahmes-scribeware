from pylatex import Math
from pylatex.utils import NoEscape
import sympy

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import Oracle

class DecimalArithmeticProblem(ProblemToFind):

	def __init__(self): 
		super().__init__()
		self.condition = "Decimals and arithmetic operations"

	def new_data(self,decimals=2,emin=1,emax=10,cmax=9,operators=3):
		self.data = []
		self.data.append(self.oracle.randfrac_complexity(dmin,dmax,nmin,nmax))
		for x in range(1,fractions):
			self.data.append(self.oracle.random_operator(top=operators))
			self.data.append(self.oracle.rand_decimal(emin,emax,cmax))

	#UPDATE FOR DECIMALS
	def evaluate(self):
		expr = ''
		for x in range(len(self.data)):
			if x % 2 == 0:
				expr += ' '+str(self.data[x].p)+'/'+str(self.data[x].q)+' '
			else:
				expr += self.oracle.sympy_string_operand(self.data[x])
		self.unknown = sympy.S(expr)

	#UPDATE FOR DECIMALS
	def question(self):
		expr = ''
		for x in range(len(self.data)):
			if x % 2 == 0:
				expr += self.formatter.rational(self.data[x].p,self.data[x].q)
			else:
				expr += self.formatter.latex_string_operand(self.data[x])
		return Math(data=NoEscape(expr))

	#UPDATE FOR DECIMALS
	def answer(self):
		return Math(data=NoEscape(self.formatter.rational(self.unknown.p,self.unknown.q)))