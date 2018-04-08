import unittest

import sympy

from Functions.function import *

class TestFunctions(unittest.TestCase):

	def test_find_constants(self):
		test = Sum(RandomConstant(),RandomConstant())
		self.assertEqual(len(test.find_constants()),2)