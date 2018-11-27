import sympy

from Generics.problem import ProblemToFind

# Simliar Triangles Problem - using ratios to calculate side lengths
'''
	For this problem there are two types, described here.

	Type 1
	Points ABC are collinear, as are points ADE. Triangles ABD and ACE are similar.
		In this version BC = AC - AB and DE = AE - AD

	Type 2
	Points ABC are collinear, as are points DBE. Triangles ABD and CBE are similar.
		In this version AC = AB + AC and DE = DB + BE
'''

class SimilarTrianglesProblem(ProblemToFind):

	# Initialization
	def __init__(self):
		self.condition("Two similar triangles are overapping each other.")


	# Behavior

	def new_data(self,min_length=2,max_length=12,question_type=1,min_k=1,max_k=5):
		sides = [self.oracle.randint(min_length,max_length) for _ in range(3)]
		points = self.oracle.random_capital_letters(5)
		triangle1 = Triangle(sides[0],sides[2],sides[3],points[0],points[1],points[2])
		while not triangle1.validate_triangle():
			sides = [self.oracle.randint(min_length,max_length) for _ in range(3)]
			triangle1.set_sides(sides[0],sides[1],sides[2])
		p = self.oracle.randint(min_k,max_k)
		q = self.oracle.randint(p*min_k,p*max_k)
		k = sympy.Rational(p,q)
		# Make the second triangle
		#  It will need to have similar sides
		#  The angles have a congruent angle with vertex v1
		triangle2 = Triangle(triangle1.s1*k,triangle1.s2*k,triangle1.s3*k,points[0],points[3],points[4])
		# Type 1: The triangles overlap at point[0]
		#         All of the data is given for the small triangle.
		#         On the large triangle the side opposite the shared angle is given.
		if question_type == 1:
			self.data = {triangle1.v1+triangle1.v2 : triangle1.s3,
						 triangle1.v2+triangle1.v3 : triangle1.s1,
						 traingle1.v3+triangle1.v1 : triangle1.s2,
						 triangle2.v2+triangle2.v3 : triangle2.s1}
			self.unknown = {triangle2.v1+triangle2.v2 : triangle2.s3,
							triangle2.v1+triangle2.v3 : triangle2.s2}


class Triangle:
	def __init__(self,s1 = 0, s2 = 0, s3 = 0, v1 = 'A', v2 = 'B', v3 = 'C'):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3


	def validate_triangle(self):
		return self.s1 + self.s2 > self.s3 and \
			self.s1 + self.s3 > self.s2 and \
			self.s3 + self.s2 > self.s1

	def set_sides(self,side1=None,side2=None,side3=None):
		if side1 != None:
			self.s1 = side1
		if side2 != None:
			self.s2 = side2
		if side3 != None:
			self.s3 = side3
