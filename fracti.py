import math

class Fraction(object):
    """ 
        Behold! The fraction class made by Shounak Ghosh, a rudimentary Python module used 
        for working with fractions.
        
        Still in development and is a bit rough around the edges. Recommended to use with caution
     """
    def __init__(self, numerator, denominator, barSize=None):
        self.numerator = numerator
        self.denominator = denominator
        greater = self.numerator if self.numerator >= self.denominator else self.denominator
        self.barSize = len(str(greater)) if greater % 2 == 0 else len(str(greater)) + 2
        
    def print(self, text=None): # implement the end="" thingy
        """ Attempts to print the fraction in a *reasonable* way. """
        if self.denominator == 1:
            print()
            print(self.numerator)
            print()
        else:
            print()
            print(' ' + str(self.numerator).center(self.barSize) + ' ')
            if text:
                print(' ' + '-' * self.barSize + ' ', text)
            else:
                print(' ' + '-' * self.barSize + ' ')
            print(' ' + str(self.denominator).center(self.barSize) + ' ')
            print()


    def simplify(self):
        """ Returns a new fraction object in it's simplest terms of the fraction it is called upon.
            Use it like:
                a = a.simplify()
            to get 1/2 for 1/4. """
        numerator, denominator = self.numerator, self.denominator
        divisor = math.gcd(self.numerator, self.denominator)
        numerator //= divisor
        denominator //= divisor

        return Fraction(numerator, denominator)

    def add(self, frac):
        """ Returns the result of the addition of two fractions (in simplest terms).
            Use it like:
                c = a.add(b) """
        num1, den1 = self.numerator, self.denominator
        num2, den2 = frac.numerator, frac.denominator
        num = num1 * den2 + num2 * den1
        den = den1 * den2

        result = Fraction(num, den)
        return result.simplify()

    def subtract(self, frac):
        """ Returns the result of the subtraction of two fractions (in simplest terms).
            Use it like:
                c = a.subtract(b) """
        num1, den1 = self.numerator, self.denominator
        num2, den2 = frac.numerator, frac.denominator
        num = num1 * den2 - num2 * den1
        den = den1 * den2

        result = Fraction(num, den)
        return result.simplify()

    def multiply(self, frac):
        """ Returns the result of the multiplication of two fractions (in simplest terms).
            Use it like:
                c = a.multiply(b) """
        num1, den1 = self.numerator, self.denominator
        num2, den2 = frac.numerator, frac.denominator
        num = num1 * num2
        den = den1 * den2

        result = Fraction(num, den)
        return result.simplify()

    def divide(self, frac):
        """ Returns the result of the division of two fractions (in simplest terms).
            Use it like:
                c = a.divide(b) """
        num1, den1 = self.numerator, self.denominator
        num2, den2 = frac.numerator, frac.denominator
        num = num1 * den2
        den = den1 * num2

        result = Fraction(num, den)
        return result.simplify()
    
    def reciprocal(self):
        """ Returns the reciprocal of a given fraction (NOT in simplified form).
            Use it like:
                b = a.reciprocal() """
        num, den = self.denominator, self.numerator
        result = Fraction(num, den)
        return result