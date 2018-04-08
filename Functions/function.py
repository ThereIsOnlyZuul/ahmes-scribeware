from enum import Enum

import sympy as sp

class Function:

	def __init__(self):
		self.constants = []
		self.operands = []

	def express(self,variable):
		pass

	def set_up(self):
		self.constants = find_constants()

	def find_constants(self):
		found = []
		for x in self.operands:
			if isinstance(x,RandomConstant):
				found.append(self.constants.append(x))
			else:
				found = x.find_constants()
		return found

class RandomConstant(Function):

	def __init__(self):
		super().__init__()
		self.quantity = None

	def value(self,number):
		self.quantity = number

	def express(self,variable):
		return self.quantity


class Sum(Function):

	def __init__(self,addend1,addend2):
		super().__init__()
		self.addend1 = addend1
		self.addend2 = addend2
		self.operands.extend((addend1,addend2))

	def express(self,variable):
		return sp(addend1.express(variable) + addend2.express(variable))

class Variable(Function):

	def __init__(self):
		super().__init__()

	def express(self,variable):
		return variable

class Product(Function):

	def __init__(self,factor1,factor2):
		super().__init__()
		self.factor1 = factor1
		self.factor2 = factor2
		self.operands.extend((factor1,factor2))

	def express(self,variable):
		return sp(factor1.express(variable) * factor2.express(variable))

class Power(Function):

	def __init__(self,base,exponent):
		super().__init__()
		self.base = base
		self.exponent = exponent
		self.operands.extend((base,exponent))

	def express(self,variable):
		return sp(base.express(variable) ** exponent.express(variable))

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
