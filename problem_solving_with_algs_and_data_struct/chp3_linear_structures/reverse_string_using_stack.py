# Q. Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
import unittest

from projects.interactive_python.problem_solving_with_alg_and_data_struct import StackTopAtEnd


def rev_string(my_str):
    s = StackTopAtEnd()
    for ch in my_str:
        s.push(ch)

    reversed = ''
    while not s.is_empty():
        reversed += s.pop()
    return reversed

my_str = "reversed"
print("Reversed string of: %s is: %s" % (my_str, rev_string(my_str)))


class Test(unittest.TestCase):
    def test_equal_strings(self):
        self.assertEqual(rev_string('apple'), 'elppa')

    def test_single_char(self):
        self.assertEqual(rev_string('x'), 'x')

    def test_numbers(self):
        self.assertEqual(rev_string('1234567890'), '0987654321')

if __name__ == '__main__':
    unittest.main()

