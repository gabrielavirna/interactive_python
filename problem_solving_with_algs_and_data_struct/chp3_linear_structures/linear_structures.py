"""

Linear data structures.
=======================
- Stacks, queues, deques, and lists are data collections whose items are ordered depending on how they're added/removed.
Once an item is added, it stays in that position relative to the other elements that came before and came after it.

Linear structures have 2 ends: the “left” & the “right”, the “front” & the “rear” , or the “top” & the “bottom.”
What distinguishes one linear structure from another is the way in which items are added and removed, in particular the
location where these additions and removals occur.
E.g. a structure might allow new items to be added at only one end, others allow items to be removed from either end.

Summary
--------
Linear data structures maintain their data in an ordered fashion.

Stacks: are simple data structures that maintain a LIFO, last-in first-out, ordering.
The fundamental operations for a stack are push, pop, and isEmpty.
Stacks are very useful for designing algorithms to evaluate and translate expressions.
Stacks can provide a reversal characteristic.

Queues: are simple data structures that maintain a FIFO, first-in first-out, ordering.
The fundamental operations for a queue are enqueue, dequeue, and isEmpty.
Queues can assist in the construction of timing simulations.
Simulations use random number generators to create a real-life situation and allow us to answer “what if” types of questions.

Prefix, infix, and postfix: are all ways to write expressions.

Deques are data structures that allow hybrid behavior like that of stacks and queues.
The fundamental operations for a deque are addFront, addRear, removeFront, removeRear, and isEmpty.

Lists are collections of items where each item holds a relative position.
A linked list implementation maintains logical order without requiring physical storage requirements.
Modification to the head of the linked list is a special case.
"""