from Functions.function import Function, Sum, Product, Power, Variable,SpecificConstant

class Polynomial(Function):

	def __init__(self,coefficients):
		super().__init__()
		self.coefficients = []
		if coefficients != None:
			self.coefficients = coefficients

	def express(self,variable):
		super().express(variable)
		expression = None
		if len(self.coefficients) < 1:
			return expression
		else:
			expression = SpecificConstant(self.coefficients[0])
		for x in range(len(self.coefficients)-1):
			expression = Sum(expression,
				Product(SpecificConstant(self.coefficients[x+1]),
					Power(Variable(),SpecificConstant(x+1))))
		return expression.express(variable)

class FactoredPolynomial(Function):

	def __init__(self,factors=[]):
		super().init()
		self.factors = factors

	def express(self,variable):
		if len(factors) < 1:
			raise SizeError
		expression = factors[0]
		if len(factors) > 1:
			for x in factors[1:]:
				expression =  expression * x
		return expression.express(variable)

class SizeError(Exception):
	'''Some attribute of the class is not big enough to support this function'''