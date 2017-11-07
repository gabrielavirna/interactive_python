"""
Stack
======
A stack (“push-down stack”) is an ordered collection of items where the addition of new items and the removal of
existing items always takes place at the same end. This end is a.k.a the “top”,  the end opposite is a.k.a the “base.”

LIFO (last-in first-out) ordering principle:
The most recently added item is the one that's in position to be removed first.

It provides an ordering based on length of time in the collection. Newer items are near the top, while older items are
near the base.Items stored in the stack that are closer to the base are those that have been in the stack the longest.

E.g. Stack:

Top -> 8.4     True    "dog"   4   -> Base
        [........items.......]

E.g. (Observe items as they are added and then removed).
Assume you start out with a clean desktop. Now place books one at a time on top of each other. You are constructing a
stack. Consider what happens when you begin removing books.
The order that they are removed is exactly the reverse of the order that they were placed.
Stacks can be used to reverse the order of items. The order of insertion is the reverse of the order of removal.

Reversal property -> examples of stacks: every web browser has a Back button.
As you navigate from web page to web page, those pages(actually the URL's) are placed on a stack.
The current page that you are viewing is on the top and the first page you looked at is at the base.
If you click on the Back button, you begin to move in reverse order through the pages.


The Stack Abstract Data Type
=============================
A Stack ADT is defined by structure and operations.
- A stack: structured as an ordered LIFO collection of items where items are added to & removed from the end ("top)”.
- The stack operations are given below.

"""
# from pythonds.basic.stack import Stack
# http://www.pythonworks.org/pythonds


# I. Implement the stack using a list where the top is at the end
# Performance: append and pop() operations are both O(1) ==>
# this implementation will perform push and pop in constant time no matter how many items are on the stack
class StackTopAtEnd:
    def __init__(self):
        self.items = []

    # tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    def is_empty(self):
        return self.items == []

    # returns the number of items on the stack. It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)

    # adds a new item to the top of the stack. It needs the item and returns nothing.
    def push(self, item):
        self.items.append(item)

    # removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
    def pop(self):
        return self.items.pop()

    # returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
    def peek(self):
        return self.items[len(self.items) - 1]


def main_top_at_end():
    # creates a new stack that is empty. It needs no parameters and returns an empty stack.
    s = StackTopAtEnd()
    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

# main_top_at_end()


# II. Implement the stack using a list where the top is at the beginning instead of at the end.
# In this case we have to index position 0 (the first item in the list) explicitly using pop and insert.
# Performance: insert(0) and pop(0) operations will both require O(n) for a stack of size n.

class StackTopAtBeginning:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]


def main_top_at_beginning():
    s = StackTopAtBeginning()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(8.4)
    print(s.pop())
    s.pop()
    print(s.size())


# main_top_at_beginning()