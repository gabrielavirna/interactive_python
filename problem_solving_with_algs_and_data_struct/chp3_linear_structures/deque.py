"""
Deque (double-ended queue)
--------------------------

-> A deque is a hybrid linear structure, that provides all the capabilities of stacks and queues in a single data
structure, but it does not require the LIFO and FIFO orderings that are enforced by those data structures.
-> A deque is structured as an ordered collection of items where items are added & removed from either end: front/rear.

Deque vs. Queue
----------------
- adding & removing items: New items can be added at the front/the rear; Existing items can be removed from either end.



          rear                       front
---------------------------------------------------
add    ->                                <- add
             "dog"   4   "cat"   True
remove <-                                -> remove
---------------------------------------------------
                    items



Implementing a Deque
---------------------
- Create a new class for the implementation of the ADT deque.
- Use the Python list set of methods to build the details of the deque.
- Assume that the rear of the deque is at position 0 in the list.

Complexity
----------
- Adding and removing items from the front: O(1)
- Adding and removing from the rear: O(n)
"""


class Deque:
    # creates a new empty deque
    def __init__(self):
        self.items = []

    # tests to see whether the deque is empty
    def is_empty(self):
        return self.items == []

    # returns the number of items in the deque
    def size(self):
        return len(self.items)

    # adds a new item to the front of the deque
    def add_front(self, item):
        self.items.append(item)

    # adds a new item to the rear of the deque.
    def add_rear(self, item):
        self.items.insert(0, item)

    # removes the front item from the deque.
    def remove_front(self):
        return self.items.pop()

    # removes the rear item from the deque.
    def remove_rear(self):
        return self.items.pop(0)


def main():
    d = Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear("dog")
    d.add_front("cat")
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    d.remove_rear()
    d.remove_front()
    print(d.items)

if __name__ == "__main__":
    main()






