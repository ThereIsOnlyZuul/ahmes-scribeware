from pylatex import Math
from pylatex.utils import NoEscape
import sympy

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import NumberType

class BabylonianSquareRootsProblem(ProblemToFind):

	def __init__(self):
		super().__init__()

	def new_data(self,number_type=NumberType.RATIONAL,
			min_radicand=1, max_radicand=100, precision=10):
		radicand = self.oracle.randint(min_radicand,max_radicand)
		while self.oracle.is_square(radicand) :
			radicand = self.oracle.randint(min_radicand,max_radicand)
		guess = self.oracle.square_root_guess(radicand,number_type,precision)
		self.data = {'radicand': radicand, 'guess': guess}

	def evaluate(self):
		self.unknown = []
		guess = self.data['guess']
		for x in range(2):
			guess = self.oracle.babylonian_root(self.data['radicand'],guess)
			self.unknown.append(guess)

	def question(self):
		root = self.formatter.sqrt(self.data['radicand'])
		result = r"{} \approx {}".format(sympy.latex(root),sympy.latex(self.data['guess']))
		return Math(data=[NoEscape(result)])

	def answer(self):
		return Math(data=self.formatter.separate_list_items([NoEscape(sympy.latex(x)) for x in self.unknown],','))