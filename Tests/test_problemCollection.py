import unittest

from Generics.problemCollection import ProblemCollection
from Generics.problem import Problem

test_collection = ProblemCollection('Test Collection')
test_problem =  Problem()

class ProblemCollectionTests(unittest.TestCase):

	def setUp(self):
		test_collection.set_instructions('Default Text')
		test_collection.add_problem(test_problem)


	def tearDown(self):
		test_collection.problems = []

	def test_setting_instructions(self):
		test_collection.set_instructions('Look ma, no hands!')
		self.assertEqual(test_collection.instructions,'Look ma, no hands!')

	def test_getting_problems(self):
		self.assertEqual(test_collection.get_problems(),[test_problem])

	def test_adding_problems(self):
		new_problem = Problem()
		test_collection.add_problem(new_problem)
		self.assertEqual(len(test_collection.get_problems()),2)

	def test_can_only_add_problem_objects(self):
		with self.assertRaises(TypeError):
			test_collection.add_problem(1)