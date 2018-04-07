from Generics.problem import Problem

class ProblemCollection:

	def __init__(self,name):
		self.name = name
		self.instructions = ''
		self.problems = []
		self.cols = 1

	def set_instructions(self, instruction_string):
		self.instructions = instruction_string

	def columns(self,n):
		self.cols = n

	def add_problem(self, problem):
		if isinstance(problem, Problem):
			self.problems.append(problem)
		else :
			raise TypeError

	def get_problems(self):
		return self.problems