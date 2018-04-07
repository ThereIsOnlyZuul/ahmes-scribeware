from Problems.egyptianFractionsProblem import EgyptianFractionsProblem, EgyptianFractionType
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import NumberType

class EgyptianFractionsTemplate(Template):

	def __init__(self):
		super().__init__()

		self.preamble('Egyptian Fractions')
		self.add_title()

		# Add the first collection of Egyptian Fraction problems
		firstCollection = ProblemCollection('Egyptian Fractions')
		firstCollection.set_instructions('Decompose the following fractions into unique unit fractions.')
		for x in range(8):
			newProblem = EgyptianFractionsProblem()
			newProblem.new_data()
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)
		firstCollection.columns(2)
		self.add_collection(firstCollection)

		# secondCollection = ProblemCollection('Improper Egyptian Fractions')
		# secondCollection.set_instructions('Decompose the following fractions into unique unit fractions.')
		# for x in range(10):
		# 	newProblem = EgyptianFractionsProblem()
		# 	newProblem.new_data(fraction_type=EgyptianFractionType.IMPROPER)
		# 	newProblem.evaluate()
		# 	secondCollection.add_problem(newProblem)
		# self.add_collection(secondCollection)

		thirdCollection = ProblemCollection('Erdös- Strauss Egyptian Fractions')
		thirdCollection.set_instructions('Decompose the following fractions into unique unit fractions.')
		for x in range(8):
			newProblem = EgyptianFractionsProblem()
			newProblem.new_data(fraction_type=EgyptianFractionType.ERDOS_STRAUSS)
			newProblem.evaluate()
			thirdCollection.add_problem(newProblem)
		thirdCollection.columns(2)
		self.add_collection(thirdCollection)
