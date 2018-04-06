import unittest

from Generics.formatter import Formatter

test_formatter = Formatter()

class FormatterTest(unittest.TestCase):

	# Test LaTeX formatters

	def test_sqrt(self):
		result = test_formatter.sqrt(5)
		self.assertEqual(result,'\\sqrt{5}')

	def test_frac(self):
		result = test_formatter.frac(2,4)
		self.assertEqual(result,'\\frac{2}{4}')

	# Test List formatters

	def test_seperate_typical_list(self):
		list_of_values = [1,2,3,4,5]
		result  = test_formatter.seperate_list_items(list_of_values,'+')
		expected = [1,'+',2,'+',3,'+',4,'+',5]
		self.assertEqual(result,expected)

	def test_seperate_one_item_list(self):
		list_of_values = [1]
		result  = test_formatter.seperate_list_items(list_of_values,'+')
		expected = [1]
		self.assertEqual(result,expected)

	def test_seperate_empty_list(self):
		list_of_values = []
		result  = test_formatter.seperate_list_items(list_of_values,'+')
		expected = []
		self.assertEqual(result,expected)