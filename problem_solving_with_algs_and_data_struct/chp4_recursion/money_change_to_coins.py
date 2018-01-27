"""
Recursion
---------
- Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems
until you get to a small enough problem that it can be solved trivially. It involves a function calling itself.
- Recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.


The Three Laws of Recursion
----------------------------
1. A recursive algorithm must have a base case.
( A base case is the condition that allows the algorithm to stop recursing.
  A base case is typically a problem that is small enough to solve directly (e.g. a list of length 1)

2. A recursive algorithm must change its state and move toward the base case.
( A change of state means that some data that the algorithm is using is modified.
  Usually the data that represents our problem gets smaller in some way e.g.
  Since the base case is a list of length 1, a natural progression toward the base case is to shorten the list )

3. A recursive algorithm must call itself, recursively.



Recursion is an effective problem-solving technique.
The key points:
--------------

All recursive algorithms must have a base case.
A recursive algorithm must change its state and make progress toward the base case.
A recursive algorithm must call itself (recursively).
Recursion can take the place of iteration in some cases.
Recursive algorithms often map very naturally to a formal expression of the problem you are trying to solve.
Recursion isn't always the answer. A recursive sol. may be more computationally expensive than an alternative algorithm.


Glossary:
-------
-> base case
A branch of the conditional statement in a recursive function that does not give rise to further recursive calls.
-> data structure: An organization of data for the purpose of making it easier to use.
-> exception: An error that occurs at runtime.
-> handle an exception
To prevent an exception from terminating a program by wrapping the block of code in a try / except construct.
-> immutable data type
A data type which cannot be modified. Assignments to elements or slices of immutable types cause a runtime error.
-> infinite recursion: A function that calls itself recursively without ever reaching the base case. Eventually, an
infinite recursion causes a runtime error.
-> mutable data type
A data type which can be modified. All mutable types are compound types. Lists and dictionaries  are mutable data types;
strings and tuples are not.
-> raise: To cause an exception by using the raise statement.
-> recursion: The process of calling the function that is already executing.
-> recursive call: The statement that calls an already executing function.
Recursion can even be indirect — function f can call g which calls h, and h could make a call back to f.
-> recursive definition
A definition which defines something in terms of itself. To be useful it must include base cases which are not
recursive. In this way it differs from a circular definition. Recursive definitions often provide an elegant way to
express complex data structures.
-> tuple
A data type that contains a sequence of elements of any type, like a list, but is immutable. Tuples can be used wherever
an immutable type is required, such as a key in a dictionary.
-> tuple assignment
An assignment to all of the elements in a tuple using a single assignment statement.
Tuple assignment occurs in parallel rather than in sequence, making it useful for swapping values.

"""