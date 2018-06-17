from enum import Enum
from random import Random

from Functions.polynomial import Polynomial

from mpmath import floor, ceil, nint
from sympy import Rational, sqrt, S

class Oracle(Random):
    """
    Oracle.py - This is the object that knows how to deal with numbers
    """

    def __init__(self):
        super().__init__()

#### Random Number Generating Functions --------------------------------------!

    def randint_nonmultiple(self,min,max,nonmultiple):
        if nonmultiple == 1:
            raise ValueError
        number = self.randint(min,max)
        while number % nonmultiple == 0:
            number = self.randint(min,max)
        return number

    def randfrac_complexity(self,dmin,dmax,nmin,nmax):
        if dmin == 1:
            raise ValueError
        denominator = self.randint(dmin,dmax)
        numerator = self.randint_nonmultiple(nmin,nmax,denominator)
        x = S(str(numerator)+'/'+str(denominator))
        return x

    def randint_series(self,length,min,max,banned=[],unique=False):
        series = []
        while len(series) < length:
            new = self.randint(min,max)
            while new in banned:
                new = self.randint(min,max)
            if unique:
                banned.append(new)
            series.append(new)
        return series

    def random_polynomial(self,degree,number_of_terms,c_min,c_max,banned=[0]):
        if number_of_terms < 2:
            raise ValueError
        the_coefficients = self.randint_series(number_of_terms-1,c_min,c_max,banned)
        the_coefficients.extend([0 for x in range(degree - number_of_terms + 1)])
        self.shuffle(the_coefficients)
        the_coefficients.append(self.randint(c_min,c_max))
        return Polynomial(the_coefficients)

#### Operand Management ------------------------------------------------------!

    def random_operator(self,bot=0,top=4):
        return list(Operand)[self.randint(bot,top)]

    def sympy_string_operand(self,operand):
        return {
            Operand.ADD:
                '+',
            Operand.SUBTRACT:
                '-',
            Operand.MULTIPLY:
                '*',
            Operand.DIVIDE:
                '/',
            Operand.POWER:
                '**'
        }[operand]

#### Number Theory Functions -------------------------------------------------!

    def round(self,decimal,decimal_places):
        enlarged = decimal * 10 ** (decimal_places)
        if enlarged - floor(enlarged) == 0.5:
            enlarged = ceil(enlarged)
        else:
            enlarged = nint(enlarged)
        return enlarged / 10.0 ** decimal_places

    def babylonian_root(self,radicand,guess):
        '''Given a radicand and a guess, produce a better guess'''
        return (guess + radicand / guess) / 2

    def square_root_guess(self,radicand,number_type,precision):
        return {
            NumberType.RATIONAL:
                Rational(sqrt(radicand).evalf(precision)).limit_denominator(precision),
            NumberType.INTEGER:
                sqrt(radicand).evalf(0),
            NumberType.REAL:
                self.round(sqrt(radicand).evalf(precision+2),precision)
        }[number_type]

    def is_square(self,number):
        '''Determine if the number is a perfect square'''
        if number == 1:
            return True
        elif number < 4:
            return False
        x = number // 2
        seen = set([x])
        while x * x != number:
            x = (x + (number // x)) // 2
            if x in seen:
                return False
            seen.add(x)
        return True

#### Statistics Functions ----------------------------------------------------!

    def arithmetic_mean(self,data):
        return sum(data)/len(data)

    def median(self,data):
        if len(data) % 2 == 1: # an odd number of items
            # We can just take the item in the middle spot
            return sorted(data)[int((len(data) + 1)/2 - 1)]
        else: # an even number of items
            # We should return the average of the two middle numbers
            middle = data[int(len(data)/2-1):int(len(data)/2+1)]
            return self.arithmetic_mean(middle)

    def mode(self,data):
        pass


class NumberType(Enum):
    RATIONAL = 'Q'
    INTEGER = 'Z'
    REAL = 'R'

class Operand(Enum):
    ADD  = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3
    POWER = 4