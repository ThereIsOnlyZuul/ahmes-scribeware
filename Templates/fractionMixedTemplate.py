from Problems.fractionProblem import FractionArithmeticProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection

class FractionMixedTemplate(Template):

	def __init__(self):
		super().__init__()

		# set up the title information
		self.preamble('Mixed Fractions')
		self.add_title()

		# some simple sums

		easyCollection = ProblemCollection('2-part Problems')
		easyCollection.set_instructions('Evaluate.')
		for x in range(10):
			newProblem = FractionArithmeticProblem()
			newProblem.new_data()
			newProblem.evaluate()
			easyCollection.add_problem(newProblem)
		easyCollection.columns(2)
		self.add_collection(easyCollection)

		mediumCollection = ProblemCollection('4-part Problems')
		mediumCollection.set_instructions('Evaluate.')
		for x in range(10):
			newProblem = FractionArithmeticProblem()
			newProblem.new_data(fractions=4)
			newProblem.evaluate()
			mediumCollection.add_problem(newProblem)
		mediumCollection.columns(2)
		self.add_collection(mediumCollection)