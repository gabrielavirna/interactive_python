"""
Binary conversion for any base
===============================
In CS different encodings are used: binary, octal (base 8), and hexadecimal (base 16).

The decimal number 233 and its corresponding octal and hexadecimal equivalents 351_(8) and E9_(16)
are interpreted as: 3×8^2+5×8^1+1×8^0 and 14×16^1+9×16^0.

Implementation:
===============
- extend the algorithm from binary_conversion_for_decimals.py; replace the “Divide by 2” idea with “Divide by base”.
- modify divide_by_2() to accept not only a decimal value but also a base for the intended conversion.

E.g.
Convert decimal numbers: 351 to base 8: 351 // 8 = 43 -> rem = 7, 43 // 8 = 5 -> rem = 3, 5 // 8 = 0 -> rem = 5
=> Stack representation: bottom -> 7 5 3 <- top of stack (push and pop from here)

A new function called baseConverter, takes a decimal number and any base between 2 and 16 as parameters.
The remainders are still pushed onto the stack until the value being converted becomes 0. The same left-to-right string
construction technique can be used with one slight change. Base 2 through base 10 numbers need a maximum of 10 digits,
so the typical digit characters 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 work fine. The problem comes when we go beyond base 10.
We can no longer simply use the remainders, as they are themselves represented as two-digit decimal numbers.
Instead we need to create a set of digits that can be used to represent those remainders beyond 9.

A solution to this problem is to extend the digit set to include some alphabet characters.
E.g. hexadecimal uses the ten decimal digits along with the first six alphabet characters for the 16 digits.
To implement this, a digit string is created, that stores the digits in their corresponding positions:
0 is at position 0, 1 is at position 1, A is at position 10, B is at position 11, and so on. When a remainder is removed
from stack, it can be used to index into the digit string & the correct resulting digit can be appended to the answer.
E.g. if the remainder 13 is removed from the stack, the digit D is appended to the resulting string.


Questions:
-----------
What is value of 25 expressed as an octal number ?
-> A. 31 (25 // 8 = 3 ->rem = 1, 3 // 8 = 0 -> rem = 1)

What is value of 256 expressed as a hexidecimal number?
-> A. 100 (256 // 16 = 16 -> rem = 0, 16 // 16 = 1 -> rem = 1, 1 // 16 = 0 -> rem = 1)

What is value of 26 expressed in base 26?
-> A. 10 (26 // 26 = 1 -> rem = 0, 1 // 26 = 0 -> rem = 1 )
"""

import unittest

from projects.interactive_python.problem_solving_with_alg_and_data_struct import StackTopAtEnd


# Divide by base
def divide_by_base(decimal_number, base):
    # set of digits used to represent those remainders beyond 9
    digits = "0123456789ABCDEF"
    rem_stack = StackTopAtEnd()

    while decimal_number > 0:
        # extract the remainder
        rem = decimal_number % base
        # push it onto the stack
        rem_stack.push(rem)
        decimal_number //= base

    new_string = ""

    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]

    return new_string


def main():
    dec_number = 25
    base = 2
    print(divide_by_base(dec_number, base))

main()


class Test(unittest.TestCase):
    def test_base_conversion_8(self):
        return self.assertEqual(divide_by_base(351, 8), '537')

    def test_base_conversion_2(self):
        return self.assertEqual(divide_by_base(233, 2), '11101001')

    def test_base_conversion_16(self):
        return self.assertEqual(divide_by_base(25, 16), '19')

if __name__ == '__main__':
    unittest.main()