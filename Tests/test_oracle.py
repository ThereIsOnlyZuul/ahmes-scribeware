import unittest
from fractions import Fraction

from sympy import Rational, sqrt

from Oracle.oracle import Oracle, NumberType

test_oracle = Oracle()

class OracleTest(unittest.TestCase):


#### Number Theory -----------------------------------------------------------!

    ## Rounding

    def test_round_down(self):
        self.assertEqual(test_oracle.round(3.141592,2),3.14)

    def test_round_up(self):
        self.assertEqual(test_oracle.round(3.141592,4),3.1416)

    ## Perfect Squares
    def test_is_square_pass(self):
        for x in range(1234567891011121314151617181920,1234567891011121314151617181950):
            self.assertTrue(test_oracle.is_square(x**2))

    def test_is_square_fail(self):
        self.assertFalse(test_oracle.is_square(152415789666209426002111556165263283035677490))

    def test_is_square_negative(self):
        self.assertFalse(test_oracle.is_square(-1))

    def test_square_root_one(self):
        self.assertTrue(test_oracle.is_square(1))

    def test_square_root_primes(self):
        primes = [2,3,5,7,11,13,17,23]
        for x in primes:
            self.assertFalse(test_oracle.is_square(x))

    def test_randint_series_length(self):
        for x in range(10):
            result = test_oracle.randint_series(x,1,10)
            self.assertEqual(len(result),x)

    ## Babylonian Roots
    def test_babylonian_root(self):
        self.assertEqual(test_oracle.babylonian_root(3,Fraction(7,4)),Fraction(97,56))

    def test_square_root_guess_rational(self):
        result = test_oracle.square_root_guess(3,NumberType.RATIONAL,5)
        self.assertEqual(Rational(7,4),result)

    def test_square_root_guess_integer(self):
        result = test_oracle.square_root_guess(50,NumberType.INTEGER,66)
        self.assertEqual(result,7)

    def test_square_root_guess_real(self):
        result = test_oracle.square_root_guess(5,NumberType.REAL,2)
        self.assertEqual(result,2.24)

    ## Non-Multiple Generation
    def test_nonmultiple_of_one_is_null(self):
        with self.assertRaises(ValueError):
            test_oracle.randint_nonmultiple(2,3,1)

#### Statistics --------------------------------------------------------------!
    
    data_001 = [0,0,0,0,0]
    data_002 = [1,1,1,1,1]
    data_003 = [0,1,2,3,4]
    data_004 = [2,3,4,5,6]
    data_005 = [2,2,2,2,7]
    data_006 = [2,2,4,6,8,8]
    data_007 = [0,1,4,9,16]
    data_008 = [0,1,1,2,3,5]
    data_009 = [1,1,2,2,3,9]

    def test_arithmetic_mean_of_known_data(self):
        result = test_oracle.arithmetic_mean(self.data_001)
        self.assertEqual(result,0)
        result = test_oracle.arithmetic_mean(self.data_002)
        self.assertEqual(result,1)
        result = test_oracle.arithmetic_mean(self.data_003)
        self.assertEqual(result,2)
        result = test_oracle.arithmetic_mean(self.data_004)
        self.assertEqual(result,4)
        result = test_oracle.arithmetic_mean(self.data_005)
        self.assertEqual(result,3)
        result = test_oracle.arithmetic_mean(self.data_006)
        self.assertEqual(result,5)
        result = test_oracle.arithmetic_mean(self.data_007)
        self.assertEqual(result,6)
        result = test_oracle.arithmetic_mean(self.data_008)
        self.assertEqual(result,2)
        result = test_oracle.arithmetic_mean(self.data_009)
        self.assertEqual(result,3)


    def test_median_of_known_data(self):
        result = test_oracle.median(self.data_001)
        self.assertEqual(result,0)
        result = test_oracle.median(self.data_002)
        self.assertEqual(result,1)
        result = test_oracle.median(self.data_003)
        self.assertEqual(result,2)
        result = test_oracle.median(self.data_004)
        self.assertEqual(result,4)
        result = test_oracle.median(self.data_005)
        self.assertEqual(result,2)
        result = test_oracle.median(self.data_006)
        self.assertEqual(result,5)
        result = test_oracle.median(self.data_007)
        self.assertEqual(result,4)
        result = test_oracle.median(self.data_008)
        self.assertEqual(result,1.5)
        result = test_oracle.median(self.data_009)
        self.assertEqual(result,2)

    def test_mode_of_known_data(self):
        result = test_oracle.mode(self.data_001)
        self.assertEqual(result,[0])
        result = test_oracle.mode(self.data_002)
        self.assertEqual(result,[1])
        result = test_oracle.mode(self.data_003)
        self.assertEqual(result,None)
        result = test_oracle.mode(self.data_005)
        self.assertEqual(result,[2])
        result = test_oracle.mode(self.data_008)
        self.assertEqual(result,[1])
        result = test_oracle.mode(self.data_009)
        self.assertEqual(result,[1,2])