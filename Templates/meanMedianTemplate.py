from Problems.meanMedianProblem import simpleMeanMedianProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection

##### Mean Median Template ---- Assess understanding of basic statistics -----!

class simpleMeanMedianTemplate(Template):

	def __init__(self):
		super().__init__()

		# Set up title information
		self.preamble('Simple Data Analysis')
		self.add_title()

		# A simple mean median collection

		easyCollection = ProblemCollection('Means and Medians')
		easyCollection.set_instructions('Find the mean and median for each of the following sets.')
		for x in range(10):
			new_problem = simpleMeanMedianProblem()
			new_problem.new_data()
			new_problem.evaluate()
			easyCollection.add_problem(new_problem)
		easyCollection.columns(2)
		self.add_collection(easyCollection)

		# A small number mean median collection

		smallCollection = ProblemCollection('Means and Medians')
		smallCollection.set_instructions('Find the mean and median for each of the following sets.')
		for x in range(10):
			new_problem = simpleMeanMedianProblem()
			new_problem.new_data(c_min=25,c_max=50)
			new_problem.evaluate()
			smallCollection.add_problem(new_problem)
		smallCollection.columns(2)
		self.add_collection(smallCollection)