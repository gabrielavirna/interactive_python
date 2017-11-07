"""
Lists
=====

Operations
-> indexing and assigning to an index position.
Both operations take the same amount of time no matter how large the list becomes.
When an operation like this is independent of the size of the list they are: O(1).

-> growing a list using: the append method or the concatenation operator.
The append method: O(1). The concatenation operator: O(k), where k is the size of the list that is being concatenated.

E.g. Generate a list of n numbers starting with 0 -> 4 ways -> see implementations os generate_list() below.

Big-O Efficiency
================

Operation	Big-O Efficiency
index []	        O(1)
index assignment	O(1)
append	            O(1)
pop()	            O(1)
pop(i)	            O(n)
insert(i,item)	    O(n)
del operator	    O(n)
iteration	        O(n)
contains (in)	    O(n)
get slice [x:y]	    O(k)
del slice	        O(n)
set slice	        O(n+k)
reverse         	O(n)
concatenate	        O(k)
sort	            O(n log n)
multiply	        O(nk)


Note:
When pop is called on the end of the list it takes O(1), but when pop is called on the first element in the list or
anywhere in the middle it is O(n) => The reason: When an item is taken from the front of the list, in Python’s
implementation, all the other elements in the list are shifted one position closer to the beginning.

e.g. Measure the difference between the two uses of pop - see popzero, popend
"""

import timeit


# Solution1: Using a for loop and creating the list by concatenation.
def generate_list1(n):
    l = []
    for i in range(n):
        l += [i]
    return l


# Solution 2. Using append rather than concatenation; The append operation is much faster than concatenation.
def generate_list2(n):
    l = []
    for i in range(n):
        l.append(i)
    return l


# Solution 3. Creating the list using list comprehension, which is twice as fast as a for loop with an append operation.
def generate_list3(n):
    l = [i for i in range(n)]
    return l


# Solution 4. Use the range function wrapped by a call to the list constructor.
def generate_list4(n):
    l = list(range(n))
    return l

# print(generate_list1(10), generate_list2(10), generate_list3(10), generate_list4(10))

time1 = timeit.Timer("generate_list1(1000)", "from __main__ import generate_list1")
print("concat", time1.timeit(number=1000), "milliseconds")

time2 = timeit.Timer("generate_list2(1000)", "from __main__ import generate_list2")
print("append", time2.timeit(number=1000), "milliseconds")

time3 = timeit.Timer("generate_list3(1000)", "from __main__ import generate_list3")
print("comprehension", time3.timeit(number=1000), "milliseconds")

time4 = timeit.Timer("generate_list4(1000)", "from __main__ import generate_list4")
print("list range", time4.timeit(number=1000), "milliseconds")

print("\n")

# To measure the difference between the two uses of pop
# As the list gets longer and longer the time it takes to pop(0) also increases while the time for pop stays very flat.
# This is exactly what we would expect to see for a O(n) and O(1) algorithm.
pop_zero = timeit.Timer("x.pop(0)", "from __main__ import x")
pop_end = timeit.Timer("x.pop()", "from __main__ import x")

for i in range(1000000,100000001,1000000):
    x = list(range((2000000)))
    pz = pop_zero.timeit(number=1000)

    x = list(range((2000000)))
    pd = pop_end.timeit(number=1000)

    print("%15.5f, %15.5f" % (pz,pd))