from Functions.function import RandomConstant, Variable, Sum, Product, Power
from Problems.integration import DefiniteIntegralProblem
from Generics.template import Template, ProblemPart
from Generics.problemCollection import ProblemCollection

class IntegrationTemplate(Template):

	def __init__(self):
		super().__init__()

		self.preamble('Integration Worksheet')
		self.add_title()

		firstCollection = ProblemCollection('Definite Integrals')
		firstCollection.set_instructions('Find the following definite integrals.')
		firstCollection.columns(2)

		template1 = Power(Variable(),RandomConstant())
		for x in range(4):
			newProblem = DefiniteIntegralProblem()
			newProblem.new_data(template1,c_min=2)
			newProblem.random_bounds_of_integration(1,10)
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)

		template2 = Sum(Product(Variable(),RandomConstant()),RandomConstant())
		for x in range(4):
			newProblem = DefiniteIntegralProblem()
			newProblem.new_data(template2,c_min=1)
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)

		for x in range(4):
			newProblem = DefiniteIntegralProblem()
			newProblem.random_polynomial_integrand()
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)

		for x in range(4):
			newProblem = DefiniteIntegralProblem()
			newProblem.random_polynomial_integrand(degree=5)
			newProblem.random_bounds_of_integration(-10,10)
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)

		template3 = Product(Sum(Product(Variable(),RandomConstant()),RandomConstant()),
			Sum(Product(Variable(),RandomConstant()),RandomConstant()))
		for x in range(4):
			newProblem = DefiniteIntegralProblem()
			newProblem.new_data(template3,c_min=1)
			newProblem.evaluate()
			firstCollection.add_problem(newProblem)

		self.add_collection(firstCollection)