"""
Lists
------
- A list is a collection of items where each item holds a relative position with respect to the others (unordered list).
- We can consider the list as having a first item, a second item, a third item, and so on.
- We can also refer to the beginning of the list (the first item) or the end of the list (the last item).
- For simplicity, we assume that lists cannot contain duplicate items.

E.g.
----
The collection of integers: 54, 26, 93, 17, 77, and 31 represents a simple unordered list of exam scores.
The list structure: [54,26,93,17,77,31].

The list ADT - Operations:
--------------------------
- List() creates a new list that is empty.
- add(item) adds a new item to the list.
- remove(item) removes the item from the list.
- search(item) searches for the item in the list.
- isEmpty() tests to see whether the list is empty.
- size() returns the number of items in the list.
- append(item) adds a new item to the end of the list making it the last item in the collection.
- index(item) returns the position of item in the list.
- insert(pos,item) adds a new item to the list at position pos.
- pop() removes and returns the last item in the list.
- pop(pos) removes and returns the item at position pos.


Implementing an Unordered List: Linked Lists
----------------------------------------------
To implement an unordered list, construct a linked list.
Be sure to maintain the relative positioning of the items (not necessarily in contiguous memory).

E.g.
---
The collection of items 54, 26, 93, 17, 77, and 31. It appears that these values have been placed randomly.
If we can maintain some explicit information in each item (the location of the next item), then the relative position
of each item can be expressed by simply following the link from one item to the next.

Note: the location of the first item of the list must be explicitly specified.
Once we know where the first item is, the first item can tell us where the second is, and so on.
The external reference is the head of the list; the last item needs to know that there is no next item.

HEAD -> 54 -> 26 -> 93 -> 17 -> 77 -> 31(END)


The Node Class
--------------
The basic building block for the linked list implementation is the node.
Each node object must hold the list item itself (the data field of the node) and a reference to the next node.
The Node class also includes the usual methods to access and modify the data and the next reference.


The Unordered List Class
------------------------
The unordered list will be built from a collection of nodes, each linked to the next by explicit references.
As long as we know where to find the first node (containing the first item), each item after that can be found by
successively following the next links.
The UnorderedList class must maintain a reference to the first node.
Note: each list object will maintain a single reference to the head of the list.


"""


class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None  # a node is initially created with next set to None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None    # Initially there are no items in the list, the head does not refer to anything
        self.tail = None

    # Checks if there are no nodes in the linked list; None denotes the “end” of the linked structure
    # Method complexity: O(1) since it requires one step to check the head reference for None
    def is_empty(self):
        return self.head is None

    # the easiest place to add the new node is right at the head of the list
    # Method complexity: O(1), since we simply place the new node at the head of the linked list
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    # traverse the linked list and keep a count of the number of nodes that occurred
    # Method complexity: O(n), since n steps are required to traverse the n-nodes linked list from head to end
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.get_data())
            current = current.get_next()

    # traversal technique: visit each node in the linked list & check if the data stored there matches the searched item
    # Method complexity: O(n), since the method requires the traversal process
    # O(n) - worst case, process every node in the list; on average it may need to traverse only half of the nodes.
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    # traverse the list looking for the node containing the item to remove and use two external references to remove it
    # Method complexity: O(n), since the method requires the traversal process
    # O(n) - worst case, process every node in the list; on average it may need to traverse only half of the nodes.
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
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def prepend(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        if new_node.get_next() is None:
            self.tail = new_node

    # Time complexity of the method: O(n), it traverses the list until it finds the last node
    def append_complex(self, item):
        new_node = Node(item)
        current = self.head

        if current:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        else:
            self.head = new_node

    # Time complexity of the method: O(1), keep track of the last node
    # Searches till the end of the linked list so it can append the given value or item
    def append_easier(self, item):
        new_node = Node(item)
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_next() is None:
                current.set_next(new_node)
                found = True
            else:
                current = current.get_next()
        return found

    def append(self, item):
        new_node = Node(item)
        self.tail.set_next(new_node)
        self.tail = new_node

    def insert_at_beginning(self, item):
        new_node = Node(item)

        if self.size() == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def insert_at_end(self, item):
        new_node = Node(item)
        current = self.head

        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def insert_at_pos(self, pos, item):

        if pos > self.size() or pos < 0:
            return None
        if pos == 0:
            self.insert_at_beginning(item)
        else:
            if pos == self.size():
                self.insert_at_end(item)
            else:
                new_node = Node(item)
                current = self.head
                count = 0
                while count < pos - 1:
                    count += 1
                    current = current.get_next()
                new_node.set_next(current.get_next())
                current.set_next(new_node)

    def index(self, item):
        current = self.head
        current_pos = 0
        found = False

        if self.size() == 0:
            print("Linked list is empty!")
        else:
            while current is not None and not found:
                current_pos += 1
                if current.get_data() == item:
                    found = True
                else:
                    current = current.get_next()
            return current_pos

    def pop(self):
        current = self.head
        current_pos = 0
        done = False
        list_length = self.size()

        if list_length == 0:
            print("The linked list is empty!")
        else:
            while current is not None and not done:
                current_pos += 1
                if current_pos == list_length - 1:
                    # This method is slower than that below it
                    # self.remove(current.get_next().get_data())
                    current.set_next(None)
                    list_length -= 1
                    done = True
                else:
                    current = current.get_next()

            return done


def main():
    my_node = Node(93)
    print(my_node.get_data())

    my_list = UnorderedList()

    my_list.add(31)     # since 31 is the first item added, it will eventually be the last node on the linked list
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())

    print(my_list.search(17))   # Since 17 is in the list, the traversal process moves only to the node containing 17
    my_list.remove(17)
    print(my_list.search(17))

    print(my_list.size())

    my_list.append(66)
    print(my_list.search(66))
    my_list.insert_at_beginning(8)
    my_list.insert_at_end(82)

    print(my_list.size())

    print(my_list.index(54))

    print("\n")
    my_list.print_list()

    print("\n")
    my_list.pop()
    my_list.print_list()

if __name__ == "__main__":
    main()


