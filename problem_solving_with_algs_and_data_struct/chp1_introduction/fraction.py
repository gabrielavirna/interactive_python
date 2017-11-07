"""
A fraction
- consists of 2 parts: The top value (the numerator) - any integer, the bottom value (the denominator) - any integer > 0
"""

def gcd(m,n):
    while m % n is not 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # allow the Fraction object to print itself as a string
    def show(self):
        print(self.numerator, '/', self.denominator)

    # build a string representation
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def get_nominator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    # a/b + c/d = (ad + bc)/ bd
    def __add__(self, other):
        new_nominator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator

        # return Fraction(new_nominator, new_denominator)
        common = gcd(new_nominator, new_denominator)
        return Fraction(new_nominator // common, new_denominator // common)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.numerator * other.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // common, new_denominator // common)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // common, new_denominator // common)

    def __truediv__(self, other):
        sign = 1
        if other.numerator == 0:
            return None  # divide by 0
        if other.numerator < 0:
            sign = -1
            other_num = - other.numerator
        else:
            other_num = other.numerator

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other_num
        common = gcd(new_numerator, new_denominator)
        return Fraction(sign * new_numerator // common, sign * new_denominator // common)

    # deep equality: for functions a/b, c/d, compare values: ad == bc
    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = self.denominator * other.numerator
        return first_num == second_num

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        first_num = self.numerator * other.denominator
        second_num = self.denominator * other.numerator
        return first_num < second_num

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __float__(self, other):
        return float(self.numerator) / float(self.denominator)


# To create an instance of the Fraction class, invoke the constructor:
my_fraction = Fraction(9, 3)
# if __str__() is not defined: print shows the actual reference that is stored in the variable (the address itself)
print(my_fraction)
my_fraction.show()
print(my_fraction.__str__())
print(my_fraction.__repr__())

print("\n")

# adding 2 fractions
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1 == f2)
print(f1 < f2)
print(f1 <= f2)
print(f1 > f2)
print(f1 >= f2)