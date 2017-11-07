"""
Balanced Symbols (A General Case)
=================================
The balanced_parentheses.py problem is a specific case of a general situation that arises in many programming languages.
The general problem of balancing and nesting different kinds of opening and closing symbols occurs frequently.

E.g. in Python square brackets, [ and ], are used for lists; curly braces, { and }, are used for dictionaries;
and parentheses, ( and ), are used for tuples and arithmetic expressions.
It is possible to mix symbols as long as each maintains its own open and close relationship.

Strings of symbols such as those bellow are properly balanced in that:
not only does each opening symbol have a corresponding closing symbol, but the types of symbols match as well:
{ { ( [ ] [ ] ) } ( ) }     [ [ { { ( ( ) ) } } ] ]     [ ] [ ] [ ] ( ) { }

Compare those with the following strings that are not balanced:
( [ ) ]     ( ( ( ) ] ) )       [ { ( ) ]


The simple parentheses checker from balanced_parenthesis.py can easily be extended to handle these new types of symbols.
Recall: each opening symbol is pushed on stack to wait for the matching closing symbol to appear later in the sequence.
When a closing symbol does appear, the only difference is that we must check to be sure that it correctly matches the
type of the opening symbol on top of the stack. If the two symbols do not match, the string is not balanced.
Once again, if the entire string is processed and nothing is left on the stack, the string is correctly balanced.

"""
import unittest

from projects.interactive_python.problem_solving_with_alg_and_data_struct import StackTopAtEnd


def balanced_symbols(symbol_string):
    s = StackTopAtEnd()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open_p,close_p):
    opens = "([{"
    closers = ")]}"
    return opens.index(open_p) == closers.index(close_p)


class Test(unittest.TestCase):
    def test_balanced1(self):
        self.assertEqual(balanced_symbols('{{([][])}()}'), True)

    def test_balanced2(self):
        self.assertEqual(balanced_symbols('[{()]'), False)

if __name__ == "__main__":
    unittest.main()