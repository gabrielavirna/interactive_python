"""
Euclid’s Algorithm: the greatest common divisor of 2 integers m and n is: n if n divides m evenly. However, if n does
not divide m evenly, then the answer is the greatest common divisor of n and the remainder of m divided by n.
"""


def gcd(m,n):
    while m % n is not 0:
        m, n = n, m % n
    return n


print(gcd(44, 16))