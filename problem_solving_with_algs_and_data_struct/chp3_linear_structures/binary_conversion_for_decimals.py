"""
Converting Decimal Numbers to Binary Numbers
=============================================
Binary representation: all values stored within a computer exist as a string of binary digits, a string of 0s and 1s.
To interact with computers we need the ability to convert back & forth between common representations & binary numbers.

Integer values:
- common data items, used in computer programs and computation, represented using the decimal number system, or base 10.
The decimal number 233_(10) and its corresponding binary equivalent 11101001_(2) are interpreted respectively as:
2×10^2+3×10^1+3×10^0 and 1×2^7+1×2^6+1×2^5+0×2^4+1×2^3+0×2^2+0×2^1+1×2^0.


Divide by 2 algorithm
=====================
- to easily convert integer values into binary numbers, uses a stack to keep track of the digits for the binary result.

- Algorithm assumes that we start with an integer > 0. A simple iteration then continually divides the decimal number
by 2 and keeps track of the remainder. The first division by 2 gives information as to whether the value is even or odd.
An even (/odd) value value will have a remainder of 0 (/1). It will have the digit 0 (/1) in the ones place.
We think about building our binary number as a sequence of digits; the first remainder we compute will actually be the
last digit in the sequence.

Observation: The reversal property ==> a stack is likely to be the appropriate data structure for solving the problem.

E.g. Divide by 2 the integer 233
233 // 2 = 116 -> rem = 1, 116 // 2 = 58 -> rem = 0, 58 // 2 = 29 -> rem = 0, 29 // 2 = 14 -> rem = 1,
 14 // 2 = 7   -> rem = 0,   7 // 2 = 3  -> rem = 1,  3 // 2 = 1  -> rem = 1,  1 // 2 = 0  -> rem = 1

==> Stack: bottom -> 1 0 0 1 0 1 1 1 <- top at end (push and pop from here)

"""

import unittest

from projects.interactive_python.problem_solving_with_alg_and_data_struct import StackTopAtEnd


# Divide by 2: to convert a decimal number value into a binary number
def divide_by_2(decimal_number):
    rem_stack = StackTopAtEnd()

    while decimal_number > 0:
        # extract the remainder
        rem = decimal_number % 2
        # push it on the stack
        rem_stack.push(rem)
        decimal_number //= 2

    # After the division process reaches 0, a binary string is constructed
    binary_string = ""
    while not rem_stack.is_empty():
        binary_string += str(rem_stack.pop())

    return binary_string


def main():
    dec_number = 233
    print(divide_by_2(dec_number))

main()


class Test(unittest.TestCase):
    def test_equality(self):
        return self.assertEqual(divide_by_2(233), '11101001')


if __name__ == "__main__":
    unittest.main()
