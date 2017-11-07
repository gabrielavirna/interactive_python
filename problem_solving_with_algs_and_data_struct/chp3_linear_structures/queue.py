"""
What Is a Queue?
=================
A queue is an ordered collection of items, where the addition of new items happens at one end (the “rear”)
and the removal of existing items occurs at the other end (the “front”).

Ordering principle: FIFO, first-in first-out. It is also known as “first-come first-served.”

As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when
it is the next element to be removed. The most recently added item in the queue must wait at the end of the collection.
The item that has been in the collection the longest is at the front.

E.g. Queue of Python data objects:

rear  -> 8.4     True    "dog"   4   -> front
        [........items.......]

E.g. Queue: the typical line that we all participate in from time to time. We wait in a line for a movie, we wait
in the check-out line at a grocery store, and we wait in the cafeteria line (so that we can pop the tray stack).
Well-behaved lines, or queues, are very restrictive in that they have only one way in and only one way out.
There is no jumping in the middle & no leaving before you have waited the necessary amount of time to get to the front.

E.g. Queues: Our computer laboratory has 30 computers networked with a single printer.
When students want to print, their print tasks “get in line” with all the other printing tasks that are waiting.
The 1st task in is the next to be completed. If you're last in line, you wait for all other tasks to print ahead of you.

E.g. Queues: operating systems use a number of different queues to control processes within a computer.
The scheduling of what gets done next is typically based on a queuing algorithm that tries to execute programs as
quickly as possible and serve as many users as it can.

E.g. As we type, sometimes keystrokes get ahead of the characters that appear on the screen.
This is due to the computer doing other work at that moment.
The keystrokes are placed in a queue-like buffer to eventually be displayed on the screen in the proper order.
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def main():
    q = Queue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    q.enqueue(8.4)
    print(q.size())

# main()