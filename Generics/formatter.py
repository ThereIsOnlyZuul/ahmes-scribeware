class Formatter:

	def sqrt(self,number):
		return '\\sqrt{%s}' % number

	def frac(self, numerator, denominator):
		return '\\frac{%s}{%s}' % (numerator, denominator)