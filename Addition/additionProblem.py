import sympy

from Generics.problem import ProblemToFind
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import Oracle

# Problem Classes
class IntegerAdditionProblem(ProblemToFind):
	"""
	integerAdditionProblem - find the sum of a sequence of integers
	"""

	# Initialization
	def __init__(self):
		super().__init__()
		self.condition = "The sum of integers"

	# Behavior
	def new_data(self,quantity=2,min=1,max=10):
		self.data = []
		for _ in range(quantity):
			self.data.append(self.oracle.randint(min,max))

	def evaluate(self):
		self.unknown = sum(self.data)

	# Output
	def question(self):
		representation = ""
		if len(self.data) > 1:
			representation += str(self.data[0])
			for x in range(len(self.data)-1):
				representation += " + "+str(self.data[x+1])
		else:
			representation = 'Error'
		return representation

	def answer(self):
		return self.unknown

# Collection Classes

class additionCollection(ProblemCollection):

	def __init__(self):
		super().__init__()
		self.instructions = "Find the following sums."