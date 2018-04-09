import unittest

import sympy

from Functions.function import *

class TestFunctions(unittest.TestCase):

	def test_find_constants(self):
		test = Sum(RandomConstant(),RandomConstant())
		self.assertEqual(len(test.find_constants()),2)

	def test_find_constants_nested(self):
		test = RandomConstant()
		for x in range(10):
			test = Sum(test,test)
			self.assertEqual(len(test.find_constants()),2**(1+x))