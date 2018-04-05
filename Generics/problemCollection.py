class ProblemCollection:

	def __init__(self,name):
		self.name = name
		self.instructions = ''
		self.problems = []

	def instructions(self, instruction_string):
		self.instructions = instruction_string

	def add_problem(self, problem):
		self.problems.append(problem)