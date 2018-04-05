import sympy

from fractions import Fraction

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import Oracle

# setup

def is_square(number):
	if number < 0:
		return False
	x = number // 2
	seen = set([x])
	while x * x != number:
		x = (x + (number // x)) // 2
		if x in seen:
			return False
		seen.add(x)
	return True

class BabylonianSquareRootsProblem(ProblemToFind):

	def __init__(self):
		super().__init__()

	def new_data(self,min_radicand=1,max_radicand=100,denominator_limit=10):
		radicand = self.oracle.randint(min_radicand,max_radicand)
		while is_square(radicand) :
			radicand = self.oracle.randint(min_radicand,max_radicand)
		guess = Fraction(radicand ** 0.5).limit_denominator(denominator_limit)
		self.data = {'radicand': radicand, 'guess': guess}

	def evaluate(self):
		self.unknown = []
		for x in range(3):
			self.data['guess'] = (self.data['guess'] + self.data['radicand']*self.data['guess'])/ 2
			self.unknown.append(self.data['guess'])

	def question(self):
		sqrt = sympy.sqrt(self.data['radicand'])
		frac = sympy.Rational(self.data['guess'].numerator,self.data['guess'].denominator)
		return sympy.latex(sqrt) + ' \approx ' + sympy.latex(frac)

	def answer(self):
		response = sympy(latex(self.unknown[0].numerator,self.unknown[0].denominator)
		for x in unknown[1:]:
			response +=
