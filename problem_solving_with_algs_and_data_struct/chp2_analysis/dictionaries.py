"""
Dictionaries
============
-  dictionaries differ from lists in that you can access items in a dictionary by a key rather than a position.
- Operations: the get item and set item operations on a dictionary are O(1).
- Another operation: the contains operation - Checking to see whether a key is in the dictionary or not is also O(1).

In some rare cases the contains, get item, and set item operations can degenerate into O(n)

operation	Big-O Efficiency
copy	        O(n)
get item	    O(1)
set item	    O(1)
delete item	    O(1)
contains (in)	O(1)
iteration	    O(n)

Dictionaries vs lists: compare the performance of the contains operation.
The time it takes for the contains operator on the list grows linearly with the size of the list O(n).
The contains operator on a dictionary is constant even as the dictionary size grows: O(1)


Implementation
-> List:
Make a list with a range of numbers in it. Then pick numbers at random and check to see if the numbers are in the list.
If our performance tables are correct the bigger the list the longer it should take to determine if any one number is
contained in the list.

-> Dictionary:
Repeat for a dictionary that contains numbers as the keys. Determining whether or not a number is in the dictionary is
not only much faster, but the time it takes to check should remain constant even as the dictionary grows larger.

"""
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")

    x = list(range(i))
    lst_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)

    print("%d, %10.3f, %10.3f" %(i, lst_time, dict_time))

