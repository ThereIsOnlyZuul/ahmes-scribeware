# Imports

from Generics.problem import ProblemToFind

# Problem Classes

class simpleMMMproblem(ProblemToFind):
	# A simple mean, median, mode problem that provides a complete data set

	# Initialization
	def __init__(self):
		super().__init__()
		self.condition = "A set of data is given"

	# Behavior
	def new_data(self,n=5,c_min:0,c_max:10):
		self.data = self.oracle.randint_series(length=n,min=c_min,max=c_max,unique=False)

	def evaluate(self):
		answers = {}
		answers['mean'] = self.oracle.arithmetic_mean(self.data)
		answers['median'] =  self.oracle.median(self.data)
		answers['mode'] = self.oracle.mode(self.data)