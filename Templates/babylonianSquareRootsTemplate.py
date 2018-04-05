from Addition.additionProblem import IntegerAdditionProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection
from BabylonianSquareRoots.babylonianSquareRoots import BabylonianSquareRootsProblem

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
		self.add_collection(easyCollection)


