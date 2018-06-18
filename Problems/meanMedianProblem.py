# Imports

from pylatex import Math
from pylatex.utils import NoEscape

from Generics.problem import ProblemToFind

# Problem Classes

class simpleMeanMedianProblem(ProblemToFind):
	# A simple mean, median, mode problem that provides a complete data set

	# Initialization ----------------------------------------------------------!
	
	def __init__(self):
		super().__init__()
		self.condition = "A set of data is given"

	# Behavior ---------------------------------------------------------------!
	
	def new_data(self,n=5,c_min=0,c_max=10):
		self.data = self.oracle.randint_series(length=n,min=c_min,max=c_max,unique=False)

	def evaluate(self):
		self.answer_dict = {}
		self.answer_dict['mean'] = self.oracle.arithmetic_mean(self.data)
		self.answer_dict['median'] =  self.oracle.median(self.data)

	# Output -----------------------------------------------------------------!

	def question(self):
		representation = ', '.join([str(x) for x in self.data])
		return Math(data=NoEscape(representation))

	def answer(self):
		return 'Mean: {mean}\nMedian: {median}'.format(mean=self.answer_dict['mean'],median=self.answer_dict['median'])