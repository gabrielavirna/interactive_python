"""
1.3. What Is Computer Science?

* Computer science: the study of problems, problem-solving & the solutions that come out of the problem-solving process.
* Algorithm: Given a problem, a computer scientist’s goal is to develop an algorithm, a step-by-step list of instructions
for solving any instance of the problem that might arise. Algorithms are solutions.
* Computable: a problem is computable if an algorithm exists for solving it (CS studies both computable & not problems).
* Abstraction: viewing the problem and solution in such a way as to separate the logical & physical perspectives.
The user of the abstraction (the client) doesn't need to know the details as long as he's aware of the way the interface
works. * This interface is the way users communicate with the underlying complexities of the implementation.

E.g.1. Consider the automobile that you may have driven to work today.
-> logical perspective: As a driver(user), to utilize the car for its intended purpose, you use the functions:
   You get in, insert the key, start the car, shift, brake, accelerate, and steer in order to drive - interface
-> physical perspective:  the mechanic who must repair your automobile must bot only knows how to drive, but also
   understand all details necessary to carry out all the functions: how the engine works, how transmission shifts gears.

E.g.2. Consider the computers.
-> logical perspective: User perspective - Most people use computers to write documents, send and receive email, surf
   the web, play music, store images, and play games without any knowledge of the details of how applications work.
-> physical perspective: Computer scientists, programmers, technology support staff, and system administrators must know
   the details of how OS work, how network protocols are configured & how to code various scripts that control function.
   They must be able to control the low-level details that a user simply assumes.

E.g.3. procedural abstraction: the Python math module: >>> import math   >>> math.sqrt(16)    4.0 <<<
-> logical perspective: User doesn't necessarily know how the square root is being calculated, but knows what the
   function is called & how to use it. If he imports correctly, the function will provide him the correct results.
-> physical perspective: someone implemented a solution to the square root problem
   * black box view of a process: the details are hidden inside

* Algorithms describe the solution to a problem in terms of the data needed to represent the problem instance and the
  set of steps necessary to produce the intended result.
* Programming languages must provide a notational way to represent both the process and the data. Languages provide
  control constructs(to represent algorithm steps) and data types.
  -> Control constructs: sequential processing, selection for decision-making, iteration for repetitive control.
  -> Data types: provide an interpretation for binary data-> all data items are represented as strings of binary digits.

* Data abstraction.
* An abstract data type: (ADT), is a logical description of how we view the data and the operations that are allowed
  without regard to how they will be implemented i.e.we are concerned only with what the data is representing and not
  with how it will eventually be constructed. By providing this level of abstraction => encapsulation around the data.
* Encapsulation: by encapsulating the details of the implementation, we do information hiding from the user’s view.

E.g. Abstarct data type
-> logical perspective: The user interacts with the interface, using the operations specified by the abstract data type.
-> physical perspective: Concerned with the implementation of an ADT a.k.a. data structure.
   * implementation-independent: allows programmer to switch the details of the implementation without changing the way
   the user of the data interacts with it. The user can remain focused on the problem-solving process.


* OOP: a class is a description of what the data look like (the state) and what the data can do (the behavior).
Classes are analogous to ADTs: a user of a class only sees the state and behavior of a data item.
Objects: the data items; an object is an instance of a class.

* Python:
- 2 main built-in numeric classes that implement the integer and floating point data types: int and float.
The standard arithmetic operations: +, -, *, /, ** exponentiation, % remainder (modulo) operator, // integer division.

- Other built-in classes: boolean; collections - ordered: Lists, strings, tuples, unordered: sets and dictionaries.
"""