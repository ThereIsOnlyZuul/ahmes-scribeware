import unittest

import sympy

from Functions.function import *
from Functions.polynomial import Polynomial
from Functions.absoluteValue import AbsoluteValue

x, y, z, alpha, beta = sympy.symbols('x y z \\alpha \\beta')

variables = [x,y,z,alpha,beta]

class TestFunctions(unittest.TestCase):

	def test_find_constants(self):
		test = Sum(RandomConstant(),RandomConstant())
		self.assertEqual(len(test.find_constants()),2)

	def test_find_constants_nested(self):
		test = RandomConstant()
		for x in range(10):
			test = Sum(test,test)
			self.assertEqual(len(test.find_constants()),2**(1+x))

	def test_express_reject_nonvariable(self):
		failures = [1,None,'x',[x]]
		for fail_sauce in failures:
			with self.assertRaises(TypeError):
				fail = Function().express(fail_sauce)

class TestVariable(unittest.TestCase):

	def test_express_accept_variable(self):
		for var in variables:
			self.assertEqual(Variable().express(var),var)

class TestPolynomial(unittest.TestCase):

	def test_polynomial_expected(self):
		series = [1,2,3]
		test_poly = Polynomial(series).express(x)
		expected = Sum(Product(SpecificConstant(3),Power(Variable(),SpecificConstant(2))),
			Sum(Product(SpecificConstant(2),Variable()),SpecificConstant(1))).express(x)
		self.assertEqual(test_poly,expected)

	def test_polynomial_expected2(self):
		series = [1,0,1]
		test_poly = Polynomial(series).express(x)
		expected = x**2 + 1
		self.assertEqual(test_poly,expected)

class TestAbsoluteValue(unittest.TestCase):

	def test_express(self):
		result = AbsoluteValue(Sum(Variable),SpecificConstant(1))).express(x)
		expected = abs(x+1)
		self.assertEqual(result,expected)