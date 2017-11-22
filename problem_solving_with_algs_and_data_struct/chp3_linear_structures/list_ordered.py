"""
The Ordered List Abstract Data Type
===================================

E.g.
The collection of integers: 54, 26, 93, 17, 77, and 31 represented as an ordered list (ascending order) is written as:
17, 26, 31, 54, 77, 93. The smallest item occupies the first position in the list, the largest occupies the last one.

The list ADT - Operations:
--------------------------
- OrderedList() creates a new list that is empty.
- add(item) adds a new item to the list making sure that the order is preserved.
- remove(item) removes the item from the list.
- search(item) searches for the item in the list.
- isEmpty() tests to see whether the list is empty.
- size() returns the number of items in the list.
- append(item) adds a new item to the end of the list making it the last item in the collection.
- index(item) returns the position of item in the list.
- insert(pos,item) adds a new item to the list at position pos.
- pop() removes and returns the last item in the list.
- pop(pos) removes and returns the item at position pos.


Implementing an Ordered List: Linked Lists
--------------------------------------------

To implement an unordered list, construct a linked list. Be sure to maintain the relative positioning of the items.\\

HEAD -> 17 -> 26 -> 31 -> 54 -> 77 -> 93 -> ||


"""


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderedList:
    def __init__(self):
        self.head = None    # an empty list will be denoted by a head reference to None

    # Method complexity: O(1), since it requires one step to check the head reference for None
    # same implementation as for UnorderedList
    def is_empty(self):
        return self.head is None

    # Method complexity: O(n), since n steps are required to traverse the n-nodes linked list from head to end
    # same implementation as for UnorderedList
    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()
        return count

    # same as for UnorderedList
    def print_list(self):
        current = self.head

        while current is not None:
            print(current.get_data())
            current = current.get_next()

    # Method complexity: O(n), since the method requires the traversal process
    # O(n) - worst case, process every node in the list; on average it may need to traverse only half of the nodes.
    # same implementation as for UnorderedList
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.set_next(None)
        else:
            previous.set_next(current.get_next())

    # similar to UnorderedList: traverse the nodes one at a time,
    # but stop once the value in the node becomes greater than the item we are searching for

    # Method complexity: O(n), since the method requires the traversal process
    # O(n) - worst case, process every node in the list; on average it may need to traverse only half of the nodes.
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    # traverse the linked list looking for the place where to add the new node
    # the place is either where we run out of nodes (current becomes None)
    # or the value of the current node becomes > the item we wish to add

    # Method complexity: O(n), since the method requires the traversal process
    # O(n) - worst case, process every node in the list; on average it may need to traverse only half of the nodes.
    def add(self, item):
        new_node = Node(item)
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)

