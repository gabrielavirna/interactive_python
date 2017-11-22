"""
Palindrome-Checker
------------------

- palindrome problem: input a string of characters and check whether it is a palindrome; easy solution: using the deque.
- A palindrome is a string that reads the same forward and backward, e.g. radar, toot, and madam.
- We would like to construct an algorithm to input a string of characters and check whether it is a palindrome.

Implementation
-------------
- use a deque to store the characters of the string.
- process the string from left to right and add each character to the rear of the deque (acts like an ordinary queue).
- use the dual functionality of the deque: The front holds the 1st character & the rear hold the last character.
- Since we can remove both of them directly, we can compare them and continue only if they match.
- If we can keep matching first and the last items, we will eventually either run out of characters or be left with a
deque of size 1 depending on whether the length of the original string was even or odd => the string must a palindrome.


          rear                          front
---------------------------------------------------
add      ->
                     r  a   d   a   r
remove   ->                               -> remove
---------------------------------------------------
                    items


"""

from projects.interactive_python.problem_solving_with_algs_and_data_struct.chp3_linear_structures.deque import Deque


def palindrome_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal


def main():
    my_string1 = "lsdkjfskf"
    my_string2 = "radar"
    print(palindrome_checker(my_string1))
    print(my_string2)

if __name__ == "__main__":
    main()


