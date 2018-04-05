from Addition.additionProblem import IntegerAdditionProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection

class AdditionTemplate(Template):

	def __init__(self):
		super().__init__()
		self.preamble("Addition Worksheet")
		self.add_title()
		firstCollection = ProblemCollection('Integer Addition')
		firstCollection.set_instructions("Find the following sums.")
		for x in range(10):
			newProblem = IntegerAdditionProblem()
			newProblem.new_data()
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)
		self.collections.append(firstCollection)

		secondCollection = ProblemCollection('Longer Series')
		secondCollection.set_instructions("Find the following sums.")
		for x in range(10):
			newProblem = IntegerAdditionProblem()
			newProblem.new_data(quantity=6)
			newProblem.evaluate()
			secondCollection.add_problem(newProblem)
		self.collections.append(secondCollection)

		thirdCollection = ProblemCollection('Larger Sums')
		thirdCollection.set_instructions("Find the following sums.")
		for x in range(10):
			newProblem = IntegerAdditionProblem()
			newProblem.new_data(min=100,max=10000)
			newProblem.evaluate()
			thirdCollection.add_problem(newProblem)
		self.collections.append(thirdCollection)