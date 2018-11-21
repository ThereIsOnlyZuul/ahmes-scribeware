#!/usr/bin/python3

import unittest
from Generics.template import Template
test_template = Template()

class TemplateTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_output_location_can_be_set(self):
		test_template.out('testing_location_123')
		self.assertEqual(test_template.output_file, 'testing_location_123')

if __name__ == '__main__':
    unittest.main()