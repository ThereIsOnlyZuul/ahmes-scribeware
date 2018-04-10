from enum import Enum

from sympy.core.symbol import Symbol

class Function:

	def __init__(self):
		self.operands = []

	def express(self,variable):
		if not isinstance(variable,Symbol):
			raise TypeError
		pass

	def find_constants(self):
		found = []
		for x in self.operands:
			if isinstance(x,RandomConstant):
				found.append(x)
			else:
				found.extend(x.find_constants())
		return found

class RandomConstant(Function):

	def __init__(self):
		super().__init__()
		self.quantity = None

	def value(self,number):
		self.quantity = number

	def express(self,variable):
		super().express(variable)
		return self.quantity

class SpecificConstant(Function):

	def __init__(self,value):
		super().__init__()
		self.value = value

	def express(self,variable):
		super().express(variable)
		return self.value


class Sum(Function):

	def __init__(self,addend1,addend2):
		super().__init__()
		self.addend1 = addend1
		self.addend2 = addend2
		self.operands.extend((addend1,addend2))

	def express(self,variable):
		super().express(variable)
		return self.addend1.express(variable) + self.addend2.express(variable)

class Variable(Function):

	def __init__(self):
		super().__init__()

	def express(self,variable):
		super().express(variable)
		return variable

class Product(Function):

	def __init__(self,factor1,factor2):
		super().__init__()
		self.factor1 = factor1
		self.factor2 = factor2
		self.operands.extend((factor1,factor2))

	def express(self,variable):
		super().express(variable)
		return self.factor1.express(variable) * self.factor2.express(variable)

class Power(Function):

	def __init__(self,base,exponent):
		super().__init__()
		self.base = base
		self.exponent = exponent
		self.operands.extend((base,exponent))

	def express(self,variable):
		super().express(variable)
		return self.base.express(variable) ** self.exponent.express(variable)

class FunctionType(Enum):
	CONSTANT = 'measure'
	VARIABLE = 'find'
	SUM = 'add'
	DIFFERENCE = 'subtract'
	PRODUCT = 'multiply'
	QUOTIENT = 'divide'
	POWER = 'power'
	TRIGONOMETRIC = 'trig'
	LOGARITHMIC = 'log'
