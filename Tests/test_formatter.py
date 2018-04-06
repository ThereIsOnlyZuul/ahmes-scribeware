import unittest

from Generics.formatter import Formatter

test_formatter = Formatter()

class NumberFormatterTest(unittest.TestCase):

	def test_sqrt(self):
		result = test_formatter.sqrt(5)
		self.assertEqual(result,'\\sqrt{5}')

	def test_frac(self):
		result = test_formatter.frac(2,4)
		self.assertEqual(result,'\\frac{2}{4}')