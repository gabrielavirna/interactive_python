"""
Simple Balanced Parentheses
===========================
- Using stacks to solve real computer science problems. In both bellow ex, parentheses appear in a balanced fashion.

You have no doubt written arithmetic expressions where parentheses are used to order the performance of operations:
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)

You may also have some experience programming in a language such as Lisp with constructs like:
(defun square(n)
     (* n n))

* Balanced parentheses:
each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested.

Consider the following correctly balanced strings of parentheses:
(()()()())      (((())))       (()((())()))
Compare those with the following, which are not balanced:
((((((())       ()))           (()()(()


Implementation:
The algorithm will read a string of parentheses from left to right and decide whether the symbols are balanced.
Observation: As you process symbols from left to right, the most recent opening parenthesis must match the next closing
symbol. Also, the first opening symbol processed may have to wait until the very last symbol for its match.
Closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out.
==>  Solution: stack is the appropriate data structure for keeping the parentheses.

Starting with an empty stack, process the parenthesis strings from left to right.
If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to
appear later. If, on the other hand, a symbol is a closing parenthesis, pop the stack.
As long as it's possible to pop the stack to match every closing symbol, the parentheses remain balanced.
If at any time there is no opening symbol on the stack to match a closing symbol, the string isn't balanced properly.
At the end of the string, when all symbols were processed, the stack should be empty.

"""

import unittest

from projects.interactive_python.problem_solving_with_alg_and_data_struct import StackTopAtEnd


# uses a Stack class and returns a boolean result as to whether the string of parentheses is balanced.
def balanced_parenthesis(symbol_string):
    s = StackTopAtEnd()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        elif s.is_empty():
            balanced = False
        else:
            s.pop()

        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test_symbol_string1(self):
        self.assertEqual(balanced_parenthesis('((()))'), True)

    def test_symbol_string2(self):
        self.assertEqual(balanced_parenthesis('(()'), False)

if __name__ == '__main__':
    unittest.main()
