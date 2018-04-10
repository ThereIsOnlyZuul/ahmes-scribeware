from Functions.function import Function

class AbsoluteValue(Function):

	def __init__(self,dummy_variable):
		super().__init__()
		self.dummy = dummy_variable
		self.operands = [dummy_variable]

	def express(self,variable):
		super().express(variable)
		return abs(self.dummy.express(variable))