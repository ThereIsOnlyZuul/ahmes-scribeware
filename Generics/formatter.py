class Formatter:

	def sqrt(self,number):
		return '\\sqrt{%s}' % number

	def frac(self, numerator, denominator):
		return '\\frac{%s}{%s}' % (numerator, denominator)

	def seperate_list_items(self,list_of_values,seperator):
		if len(list_of_values) < 2:
			return list_of_values
		result = [list_of_values[0]]
		for x in list_of_values[1:]:
			result.append(seperator)
			result.append(x)
		return result