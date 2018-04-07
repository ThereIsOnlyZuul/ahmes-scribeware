from Problems.babylonianSquareRoots import BabylonianSquareRootsProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection
from Oracle.oracle import NumberType

class BabylonianSquareRootsTemplate(Template):

	def __init__(self):
		super().__init__()

		# set up the title information
		self.preamble('Babylonian Square Roots Worksheet')
		self.add_title()

		# put in some easy small square roots

		easyCollection = ProblemCollection('Basic Babylonian Square Roots')
		easyCollection.set_instructions('Use the given approximations to generate some more accurate fractions for the given roots.')
		for x in range(10):
			newProblem = BabylonianSquareRootsProblem()
			newProblem.new_data()
			newProblem.evaluate()
			easyCollection.add_problem(newProblem)
		easyCollection.columns(2)
		self.add_collection(easyCollection)

		decimalCollection = ProblemCollection('Decimal Babylonian Square Roots')
		decimalCollection.set_instructions('Use the given approximations to generate more accurate decimals for the given roots.')
		for x in range(6):
			newProblem = BabylonianSquareRootsProblem()
			newProblem.new_data(number_type=NumberType.REAL,precision=1)
			newProblem.evaluate()
			decimalCollection.add_problem(newProblem)
		decimalCollection.columns(2)
		self.add_collection(decimalCollection)
	

