import unittest

from Problems.similarTrianglesProblem import Triangle

class TriangleTest(unittest.TestCase):

	test_triangle = Triangle()

	def setUp(self):
		pass

	def tearDown(self):
		self.test_triangle.set_sides(0,0,0)

	def test_validate_triangle_known_values(self):
		# test some known triangles, they should pass
		triangle = Triangle(3,4,5)
		for x in range(100):
			self.assertTrue(triangle.validate_triangle())
			triangle.s1 += x
			triangle.s2 += x
			triangle.s3 += 2*x

	def test_fail_triangle_known_values(self):
		# test some known triangles, they should pass
		triangle = Triangle(3,1,5)
		for x in range(100):
			self.assertFalse(triangle.validate_triangle())
			triangle.s1 += x
			triangle.s2 += x
			triangle.s3 += 2*x

	def test_set_sides_simultaneous(self):
		# test the ability to change the side lenghts of a triangle all at once
		for x in range(5):
			for y in range(5):
				for z in range(5):
					self.test_triangle.set_sides(x,y,z)
					self.assertEqual(self.test_triangle.s1,x)
					self.assertEqual(self.test_triangle.s2,y)
					self.assertEqual(self.test_triangle.s3,z)

	def test_set_sides_individual(self):
		# test the ability to change the side lenghts of a triangle individually
		for x in range(1,125):
			self.assertEqual(self.test_triangle.s1,x-1)
			self.test_triangle.set_sides(side1=x)
			self.assertEqual(self.test_triangle.s1,x)
			self.assertEqual(self.test_triangle.s2,x-1)
			self.test_triangle.set_sides(side2=x)
			self.assertEqual(self.test_triangle.s2,x)
			self.assertEqual(self.test_triangle.s3,x-1)
			self.test_triangle.set_sides(side3=x)
			self.assertEqual(self.test_triangle.s3,x)

