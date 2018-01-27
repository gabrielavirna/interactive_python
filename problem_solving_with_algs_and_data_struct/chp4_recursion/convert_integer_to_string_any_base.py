"""
Converting an Integer to a String in Any Base
---------------------------------------------

Suppose you want to convert an integer to a string in some base between binary and hexadecimal.
E.g. convert the integer 10 to a string representation in decimal: "10"; to its string representation in binary: "1010".

Example: convert number 769 in base 10
----------------------------------------
Suppose we have a sequence of characters corresponding to the first 10 digits, like convString = "0123456789".
It is easy to convert a number less than 10 to its string equivalent by looking it up in the sequence.
E.g. if the number is 9, then the string is convString[9] or "9".
Break up the number 769 into three single-digit numbers: 7, 6, and 9, then converting it to a string is simple.

I. Base case: number n < base, where base = 10.

The overall algorithm will involve three components:

1. Reduce the original number to a series of single-digit numbers.
2. Convert the single digit-number to a string using a lookup.
3. Concatenate the single-digit strings together to form the final result.

II. Change state and make progress toward the base case.

We are working with an integer => consider what mathematical operations might reduce a number: division & substraction.

Convert 769 to its string representation
Using integer division: toStr(769) => 769 // 10 + '9
-> remainder < our base => can be converted to a string immediately by lookup.
-> 769 < our original and moves us toward the base case of having a single number less than our base.

Convert 76 to its string representation:
Again use integer division: toStr(76) => 76 // 10 + '10'
-> remainder < our base => can be converted to a string immediately by lookup.
-> 76 < our original and moves us toward the base case of having a single number less than our base.

Convert 7 to its string representation:
Using integer division: toStr(7) => 7 // 10 + '7'
-> remainder < our base => can be converted to a string immediately by lookup.
-> 7 < our original and moves us toward the base case of having a single number less than our base.

III. We have reduced the problem to converting 7, which satisfies the base case condition of n < base, where base = 10.


Solution 2:
Stack Frames: Implementing Recursion
Suppose that instead of concatenating the result of the recursive call to convert_tosString with the string from
convertString, we modified our algorithm to push the strings onto a stack prior to making the recursive call.
"""


# Solution 1:
def convert_number_to_string(number, base):
    convert_string = "0123456789ABCDEF"
    # check for the base case: n < base we are converting to.
    if number < base:
        # if base case, stop recursing & return the string from the convertString sequence.
        return convert_string[number]
    else:
        # making the recursive call & reducing the problem size–using division.
        return convert_number_to_string(number // base, base) + convert_string[number % base]


# Solution 2:
class StackTopAtEnd:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


rstack = StackTopAtEnd()


# each time we make a call to the function, we push a character on the stack.
def convert_to_string(number, base):
    convert_string = "0123456789ABCDEF"
    while number > 0:
        if number < base:
            rstack.push(convert_string[number])
        else:
            rstack.push(convert_string[number % base])
        number = number // base

    result = ""
    while not rstack.is_empty():
        # simply pop the characters off the stack and concatenate them into the final result
        result += str(rstack.pop())
    return result


def main():

    print(convert_number_to_string(769, 10))
    print(convert_number_to_string(1453, 16))
    print(convert_number_to_string(10, 2))

    print(convert_to_string(1453, 16))

if __name__ == "__main__":
    main()