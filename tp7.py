from __future__ import annotations

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE :
            num : un entier correspondant au numérateur valant par défaut 0
            den : un entier non-nul correspondant au dénominateur valant par défaut 1
        POST :
            self.num : le numerateur
            self.den : le denominateur
        """
        self.__num = num
        if den == 0:
            raise ValueError("denominator cannot be 0")
        self.__den = den
        self.simplify()

    @property
    def numerator(self):
        return self.__num

    @numerator.setter
    def numerator(self, value: int):
        self.__num = value

    @property
    def denominator(self):
        return self.__den

    @denominator.setter
    def denominator(self, value: int):
        if value != 0:
            self.__den = value

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : ?
        POST : ?
        """
        self.simplify()
        return str(self.__num) + "/" + str(self.__den)

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction
        POST :
            renvoie un string
        """
        n = str(self.__num // self.__den)
        f = str(self.__num % self.__den) + "/" + str(self.__den)
        return n + " + " + f

    # ------------------ Operators overloading ------------------

    def __add__(self, other) -> Fraction :
        """Overloading of the + operator for fractions

         PRE :
            other : la fraction additionneur
         POST :
            renvoie la fraction résultante
         """
        if type(other) == int:
            return Fraction(self.__num + self.__den * other, self.__den)
        elif type(other) == Fraction:
            num = self.__num * other.denominator + other.numerator * self.__den
            den = self.__den * other.denominator
            return Fraction(num, den)
        else:
            raise TypeError("unsupported operand type")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE :
            other : la fraction soustracteurs
         POST :
            renvoie la fraction résultante
        """
        if type(other) == int:
            return Fraction(self.__num - self.__den * other, self.__den)
        elif type(other) == Fraction:
            num = self.__num * other.denominator - other.numerator * self.__den
            den = self.__den * other.denominator
            return Fraction(num, den)
        else:
            raise TypeError("unsupported operand type")

    def __mul__(self, other)-> Fraction:
        """Overloading of the * operator for fractions

        PRE :
            other : la fraction multiplicateur
         POST :
            renvoie la fraction résultante
        """
        if type(other) == int:
            return Fraction(self.__num * other, self.__den)
        elif type(other) == Fraction:
            num = self.__num * other.numerator
            den = self.__den * other.denominator
            return Fraction(num, den)
        else:
            raise TypeError("unsupported operand type")

    def __truediv__(self, other:Fraction)-> Fraction:
        """Overloading of the / operator for fractions

        PRE :
            other : la fraction diviseur
         POST :
            renvoie la fraction résultante
        """
        if other.numerator == 0:
            raise ZeroDivisionError
        num = self.__num * other.denominator
        den = self.__den * other.numerator
        return Fraction(num, den)

    def __pow__(self, other:int)-> Fraction:
        """Overloading of the ** operator for fractions

        PRE : other : un entier positif représentant la puissance
        POST : la fraction après
        """
        if type(other) != int:
            raise TypeError
        return Fraction(self.__num ** other, self.__den ** other)

    def __eq__(self, other: Fraction)-> bool:
        """Overloading of the == operator for fractions

        PRE :
            other : la fraction à comparer
         POST :
            renvoie True si la valeur est la même, False si non
        """
        return self.__num / self.__den == other.__num / other.__den

    def __float__(self)-> float:
        """Returns the decimal value of the fraction

        POST : renvoie le float de la fraction
        """
        return self.__num / self.__den

    def __ne__(self, other: Fraction)-> bool:
        """Overloading of the != operator for fractions

        PRE :
            other : la fraction à comparer
         POST :
            renvoie True si la valeur est différente, False si non
        """
        return not self == other

    def __round__(self, n: int = 0):
        """Return the rounded value of the fraction

        PRE : n: a positive integer
        POST : returns the rounded form of the fraction n number after the decimal point
        """
        return round(self.__float__(), n)

    def __lt__(self, other):
        """Overloading of the < operator for fractions

        PRE : other, another fraction
        POST : return True if the fraction is lesser than other
        """
        return self.__float__() < float(other)

    def __le__(self, other):
        """Overloading of the <= operator for fractions

        PRE : other, another fraction
        POST : return True if the fraction is lesser than or equal to other
        """
        return self.__float__() <= float(other)

    def __gt__(self, other):
        """Overloading of the > operator for fractions

        PRE : other, another fraction
        POST : return True if the fraction is greater than other
        """
        return self.__float__() > float(other)

    def __ge__(self, other):
        """Overloading of the >= operator for fractions

        PRE : other, another fraction
        POST : return True if the fraction is greater than or equal to other
        """
        return self.__float__() >= float(other)

    def __int__(self):
        """Return the integer value of the fraction

        PRE : /
        POST : return the integer of the fraction
        """
        return int(self.__float__())


    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : return True si le numérateur est 0, False sinon
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : return True si la fraction est entière, False sinon
        """
        return self.__num % self.__den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : return True si la fraction est entre -1 et 1, False sinon
        """
        return abs(self.__float__()) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : return True si la fraction est simplifiable jusqu'à 1/x, False sinon
        """
        return self.__den % self.__num == 0

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : other, l'autre fraction

        POST : return True si les fractions sont adjacentes, False sinon
        """
        self.simplify()
        other.simplify()
        if abs(self.__den) == abs(other.denominator):
            return (abs(self.__num) + 1 == abs(other.numerator)) or (abs(self.numerator) == abs(other.numerator + 1))
        elif self.__den % other.denominator == 0:
            other.denominator *= self.__den // other.denominator
        elif other.numerator % self.__den == 0:
            self.__den *= other.numerator // self.__den
        return False

    def simplify(self):
        """
        simplifies the fraction to the smallest denominator

        PRE:/
        POST: the numerator and denominator are now the smallest possible
        """
        if self.__den < 0:
            self.__num = -self.__num
        pgcd = 1
        for i in range(2, max(self.__num, self.__den)//2+2):
            if self.__den % i == 0 and self.__num % i == 0:
                pgcd = i
        self.__num //= pgcd
        self.__den //= pgcd

