from Oracle.oracle import Oracle
from Generics.formatter import Formatter

class Problem:

	oracle = Oracle()
	formatter = Formatter()

	def __init__(self):
		self.question
		self.answer

	def question(self):
		return self.question

	def answer(self):
		return self.answer


class ProblemToFind(Problem):

	def __init__(self):
		super().__init__()
		self.condition = None
		self.data = None
		self.unknown = None