"""
Programming Exercises
-----------------------

1. Write a recursive function to compute the factorial of a number.

2. Write a recursive function to reverse a list.

3. Modify the recursive tree program using one or all of the following ideas:

Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.
If you implement all of the above ideas you will have a very realistic looking tree.

4. Find or invent an algorithm for drawing a fractal mountain. Hint: One approach to this uses triangles again.

5. Write a recursive function to compute the Fibonacci sequence.
How does the performance of the recursive function compare to that of an iterative version?

6. Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.

7. Using the turtle graphics module, write a recursive program to display a Hilbert curve.

8. Using the turtle graphics module, write a recursive program to display a Koch snowflake.

9. Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug.
Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water.
How can you get exactly two gallons of water in the 4-gallon jug?

Solution:
Fill up the 3-gallon jug. Empty the 3-gallon jug into the 4-gallon jug. (4-g jug: 3 g water, 3-g jug: 0 g water)
Fill up the 3-gallon jug again and empty it in the 4-gallon-jug. (4-g jug: 4 g water, 3-g jug: 2 g water)
Empty the 4-gallon jug and fill it up with the 2-gallons of water reimained in the 3-gallon jug.

10. Generalize the problem above so that the parameters to your solution include the sizes of each jug and the final
amount of water to be left in the larger jug.

11. Write a program that solves the following problem: Three missionaries and three cannibals come to a river and find
a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the cannibals
ever outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of crossings that will get
everyone safely to the other side of the river.

Solution:
Two cannibals go across (leaving one cannibal and three missionaries on home side)
One cannibal stays and one returns (leaving one cannibal on other side)
Cannibal and Missionary go across.
Missionary stays and cannibal returns (leaving one missionary and one cannibal on other side)
Both two remaining Missionaries go across (leaving two cannibals at home)
The one cannibal on other side returns to home (leaving three missionaries on other side)
Two cannibals go across to other side. One stays.
One returns. (leaving three missionaries and one cannibal on other side)
The remaining two cannibals go across to other side.

12. Modify the Tower of Hanoi program using turtle graphics to animate the movement of the disks. Hint: You can make
multiple turtles and have them shaped like rectangles.

13. Pascal’s triangle is a number triangle with numbers arranged in staggered rows such that: a_nr=n!/r!(n−r)!
This equation is the equation for a binomial coefficient. You can build Pascal’s triangle by adding the two numbers that
are diagonally above a number in the triangle. An example of Pascal’s triangle is shown below.

        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1

14. Write a program that prints out Pascal’s triangle. Your program should accept a parameter that tells how many rows of
the triangle to print.

Suppose you are a computer scientist/art thief who has broken into a major art gallery. All you have with you to haul
out your stolen art is your knapsack which only holds WW pounds of art, but for every piece of art you know its value
and its weight. Write a dynamic programming function to help you maximize your profit. Here is a sample problem for you
to use to get started: Suppose your knapsack can hold a total weight of 20. You have 5 items as follows:

item     weight      value
  1        2           3
  2        3           4
  3        4           8
  4        5           8
  5        9          10

15. This problem is called the string edit distance problem, and is quite useful in many areas of research.
Suppose that you want to transform the word “algorithm” into the word “alligator.” For each letter you can either copy
the letter from one word to another at a cost of 5, you can delete a letter at cost of 20, or insert a letter at a cost
of 20. The total cost to transform one word into another is used by spell check programs to provide suggestions for
words that are close to one another. Use dynamic programming techniques to develop an algorithm that gives you the
smallest edit distance between any two words.


"""

from projects.interactive_python.problem_solving_with_algs_and_data_struct.chp3_linear_structures.stack import StackTopAtEnd
import timeit, random
import math


# 1. Factorial of a number
def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result


# 2. Reverse a list - affects the original list
def reverse_list(l):
    i = len(l)
    for i in range(int(len(l)/2)):
        l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
    return l


# 2. Reverse a list using a stack - doesn't affect the original list
def reverse_list_using_stack(l):
    s = StackTopAtEnd()
    for elem in l:
        s.push(elem)

    reversed_list = []*len(l)
    while not s.is_empty():
        reversed_list.append(s.pop())
    return reversed_list


# 5. Fibonacci sequence: iterative vs. recursive
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        return result


def fibonacci_iterators(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# 6. Tower of Hanoi using 3 stacks
def move_tower(height, initial_stack, buffer_stack, final_stack):
    if height == 0:
        return
    elif height > 0:
        # move tower of size n - 1 to helper:
        move_tower(height - 1, initial_stack, final_stack, buffer_stack)
        # move disk from source peg to target peg
        move_disk(initial_stack, final_stack)
        # move tower of size n-1 from helper to target
        move_tower(height - 1, buffer_stack, initial_stack, final_stack)


def move_disk(initial_s, final_s):
    if initial_s:
        final_s.push(initial_s.pop())


# 10. Jugs with water
class WaterJug:
    def __init__(self, capacity=0, amount=0): # 0 <= amount <= capacity
        if capacity < 0 or amount < 0 or capacity < amount:
            raise NameError("Invalid parameters for Water Jug")
        self.capacity = capacity
        self.amount = amount

    # to print the capacity and content of the Water Jug
    def __str__(self):
        return "(" + str(self.capacity) + "," + str(self.amount) + ")"

    def get_amount(self):
        return self.amount

    # take a variable amount of water, changing the contents inside
    # of the WaterJug, and return the added amount
    def fill_up_jug(self, amount):
        room = self.capacity - self.amount
        amount_added = amount
        if room < amount:
            amount_added = room
        self.amount += amount_added
        return amount_added

    # use swap method to empty the contents from a WaterJug and return the amount removed
    def remove(self, amount):
        room = self.amount
        amount_removed = amount
        if room < amount:
            amount_removed = room
        self.amount -= amount_removed
        return amount_removed

    # spill the content of this into another
    def spill_into(self, other):
        self.remove(other.add(self.amount))

#
# class WaterJugPuzzle:
#     def __init__(self):
#         self.jugs = {4: WaterJug(4, 0), 3: WaterJug(3, 0)}
#         self.moves = 0
#
#     def move(self, from_jug, to_jug):
#         self.jugs[from_jug].spill_into(self.jugs[to_jug])
#         self.moves += 1
#
#     def is_solved(self):
#         return self.jugs[4].get_amount() == 2 and self.jugs[3] == 0
#
#     def __str__(self):
#         return str(self.jugs[4]) + " " + str(self.jugs[3]) + " " + str(self.moves) + str(self.is_solved())


# Ex.11. 3 missionaries and 3 cannibals crossing the river
def cross_river(missionaries, cannibals, p1, p2):
    left = ["x"]*6
    right = []*6
    while cannibals <= missionaries:
        right.append("x")
    return right


# Ex.14. Pascal's triangle
def combinations(n, r):  # combinations, n choose k
    return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))


def pascal_triangle(n_rows):
    result = []  # a container to collect the rows
    for count in range(n_rows):
        row = []
        for element in range(count+1):
            row.append(combinations(count, element))
        result.append(row)
    return result


def main():
    number = 6
    print("Ex.1. Factorial of {} is: {}".format(number, factorial(number)))
    print("\n")

    the_list = [1, 3, 5, 7, 9]
    print("Ex.2. The reverse of the list is:  {}".format(reverse_list(the_list)))
    print("\n")

    the_2nd_list = [1, 3, 5, 7, 9]
    print("The reverse of the list {}, using a stack is the list: {}".format(the_2nd_list, reverse_list_using_stack(the_2nd_list)))
    print("\n")

    n = 7
    print("Ex.5. The {}th number of the fibonacci sequence is: {}".format(n, fibonacci_recursive(n)))

    t1 = timeit.Timer("fibonacci_recursive(7)", "from __main__ import fibonacci_recursive")
    time_taken1 = t1.timeit(number=100)
    print("Time taken using recursive fibonacci sequence is: %10.7f" % time_taken1, "milliseconds")

    print("The fibonacci sequence using iterators is:")
    for i in fibonacci_iterators(13):
        print(i)

    t2 = timeit.Timer("fibonacci_iterators(13)", "from __main__ import fibonacci_iterators")
    time_taken2 = t2.timeit(number=100)
    print("Time taken using iterators fibonacci is: %10.7f" % time_taken2, "milliseconds")
    print("\n")

    initial_stack = StackTopAtEnd()
    initial_stack.items = [4, 3, 2, 1]
    buffer_stack = StackTopAtEnd()
    final_stack = StackTopAtEnd()
    move_tower(initial_stack.size(), initial_stack, buffer_stack, final_stack)
    print("Ex.6. The final stack is: {}".format(final_stack.items))
    print("\n")
    #
    # content1 = int(input("Enter the capacity for the 1st water jug: "))
    # jug1 = WaterJug(content1, 0)
    # content2 = int(input("Enter the capacity for the 2nd water jug: "))
    # jug2 = WaterJug(content2, 0)
    # goal = int(input("Enter the goal quantity of water in the 1st jug: "))
    #

    # cannibals = 3
    # missionaries = 3
    # result = cross_river(missionaries, cannibals)
    # print("Ex.11. The right side after crossing the river: ".format(result))
    # print("\n")

    print("Ex.13. Pascal's triangle: ")
    for row in pascal_triangle(5):
        print(row)

if __name__ == "__main__":
    main()



