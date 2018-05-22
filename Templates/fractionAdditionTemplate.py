from Problems.fractionProblem import FractionAdditionProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection

class FractionAdditionTemplate(Template):

	def __init__(self):
		super().__init__()

		# set up the title information
		self.preamble('Fraction Addition')
		self.add_title()

		# some simple sums

		easyCollection = ProblemCollection('2-part Sums')
		easyCollection.set_instructions('Find the following 2-part sums.')
		for x in range(10):
			newProblem = FractionAdditionProblem()
			newProblem.new_data()
			newProblem.evaluate()
			easyCollection.add_problem(newProblem)
		easyCollection.columns(2)
		self.add_collection(easyCollection)

		longerCollection = ProblemCollection('Longer Series')
		longerCollection.set_instructions('Find the following sums')
		for x in range(10):
			newProblem = FractionAdditionProblem()
			newProblem.new_data(quantity=5)
			newProblem.evaluate()
			longerCollection.add_problem(newProblem)
		longerCollection.columns(2)
		self.add_collection(longerCollection)