"""
Questions:
==========
Q1: Which of the list operations shown below is not O(1)? A. (A)
(A) list.pop(0) -> When you remove the 1st element of a list, all the other elements of the list must be shifted forward
(B) list.pop()
(C) list.append()
(D) list[10]
(E) all of the above are O(1)

Q2: Which of the dictionary operations shown below is O(1)? A. (E)
(A) 'x' in mydict
(B) del mydict['x']
(C) mydict['x'] == 10
(D) mydict['x'] = mydict['x'] + 1
(E) all of the above are O(1) -> The only dictionary operations that are not O(1) are those that require iteration.



Q3: Give the Big-O performance of the following code fragment: A. T(n) = n^2 + 1 => T(n) = n^2

for i in range(n):
   for j in range(n):
      k = 2 + 2

Q4: Give the Big-O performance of the following code fragment: A. T(n) = n + 1 => T(n) = n

for i in range(n):
     k = 2 + 2

Q5: Give the Big-O performance of the following code fragment: A. T(n) = 1 + 2*log n => T(n) = log n

i = n
while i > 0:
   k = 2 + 2
   i = i // 2

Q6: Give the Big-O performance of the following code fragment: A. T(n) = n^3

for i in range(n):
   for j in range(n):
      for k in range(n):
         k = 2 + 2

Q7: Give the Big-O performance of the following code fragment: A. T(n) = 1 + 2 log n = log n

i = n
while i > 0:
   k = 2 + 2
   i = i // 2

Q8: Give the Big-O performance of the following code fragment: A. T(n) = 3*n = n

for i in range(n):
   k = 2 + 2
for j in range(n):
   k = 2 + 2
for k in range(n):
   k = 2 + 2

Programming Exercises:
======================
P1: Devise an experiment to verify that the list index operator is O(1).
P2: Devise an experiment to verify that get item and set item are O(1) for dictionaries.
P3: Devise an experiment that compares the performance of the del operator on lists and dictionaries.
P4: Given a list of numbers in random order, write an algorithm that works in O(n log(n)) to find the kth
smallest number in the list.
P5: Can you improve the algorithm from the previous problem to be linear? Explain.
"""
import timeit
import random

# P1: Devise an experiment to verify that the list index operator is O(1).
lst = list(range(10))
for i in lst:
    t1 = timeit.Timer("lst.index(6)", "from __main__ import lst")
    time_taken1 = t1.timeit(number=1000)
    print("list index operator: %10.7f" % time_taken1, "milliseconds")

print("\n")
# P2: Devise an experiment to verify that get item and set item are O(1) for dictionaries.


dct = {"Name": "Harry", "Age": 12, "Job": "Student"}
t2 = timeit.Timer("dct.__getitem__('Name')", "from __main__ import dct")
time_taken2 = t2.timeit(number=10000)

t3 = timeit.Timer("dct.__setitem__('Height', 169)", "from __main__ import dct")
time_taken3 = t3.timeit(number=10000)

print("get item for dictionary: %10.5f" % time_taken2, "milliseconds")
print("set item for dictionary: %10.5f" % time_taken3, "milliseconds")

for item in dct:
    print(item, dct[item])

print("\n")

# # P3: Devise an experiment that compares the performance of the del operator on lists and dictionaries.
#
# lst = list(range(15))
# t4 = timeit.Timer("del(lst[4])", "from __main__ import lst")
# time_taken4 = t4.timeit(number=10000)
#
# dct = {"Name": "Prune", "Age": 23, "Learning": "Python", "Topic": "Big O Notation"}
# t5 = timeit.Timer("del(dict['Learning'])", "from __main__ import dct")
# time_taken5 = t5.timeit(number=10000)

# print("del operator on list: %10.3f" % time_taken4, "milliseconds")
# print("del operator on dictionary: %10.3f" % time_taken5, "milliseconds")


# P4: Given a list of no. in random order, write an algorithm O(n log(n)) to find the kth smallest number in the list.

# works fine when the array is small
def kth_smallest_number(n, k):
    my_list = list(random.randint(1, 100) for elem in range(n))
    random.shuffle(my_list)
    random.shuffle(my_list)
    my_list.sort()
    return my_list[k]

t6 = timeit.Timer("kth_smallest_number(1000, 5)", "from __main__ import kth_smallest_number")
time_taken6 = t6.timeit(number=10000)
print("time taken to find kth smallest number in a list: %10.5f" % time_taken6, "milliseconds")

# P5: Can you improve the algorithm from the previous problem to be linear? Explain.

# The first algorithm: select_random_pivot -> uses a random number to select the pivot point;
# The average run time is O(N) and the worst case run time is O(N^2) with a vanishingly smal probability of occurring.

# The second algorithm: select_median_of_medians_pivot -> uses a more deterministic approach to find a better
# approximation of the median; the algorithm has an average and worst case run time of O(N).

# Application: get the top n ordered items from an unordered array in O(N) time using the select_random_pivot function.

# Select random pivot
# Although this algorithm has worse worst case performance than select_median_of_medians (O(n^2) instead of O(n)),
# algorithm is preferred because it is much faster in practice.


def main_select_random():
    # Create a list of N pseudo random numbers; Duplicates can occur.
    num = 10000
    my_list = list(random.randint(1, 100) for elem in range(num))
    random.shuffle(my_list)
    random.shuffle(my_list)

    # Get the value of the kth item.
    k = 7
    k_value = select_random_pivot(my_list, k)

    # Test it
    sorted_list = sorted(my_list)
    assert sorted_list[k] == k_value


def select_random_pivot(the_list, k):
    # If the array is short, terminate the recursion and return the value without partitioning.
    if len(the_list) <= 10:
        the_list.sort()
        return the_list[k]
    else:
        # Randomly choose a pivot point; In vanishingly rare cases this can result in O(N^2).
        pivot_idx = random.randint(0, len(the_list) -1)
        pivot = the_list[pivot_idx] # pivot point value (not index)

        # Now select recursively using the pivot. Use the pivot to partition the input array into 3 categories:
        # items < pivot value (array_lt), items > pivot value (array_gt) and items = pivot value (equals_array).
        list_lt = []
        list_eq = []
        list_gt = []

        for item in the_list:
            if item < pivot:
                list_lt.append(item)
            elif item > pivot:
                list_gt.append(item)
            else:
                list_eq.append(item)
        # Now, the array values have been partitioned according to their relation to the pivot value.

        # the desired value is in list_lt => we need to recurse.
        if k < len(list_lt):
            return select_random_pivot(list_lt, k)
        # the desired value is in list_eq
        elif k < len(list_lt) + len(list_eq):
            return list_eq[0]
        # we need to recurse but we also have to make sure that k is normalized with
        # respect to array_gt so that it has the proper offset in the recursion.
        else:
            normalized_k = k - (len(list_lt) + len(list_eq))
            return select_random_pivot(list_gt, normalized_k)


t7 = timeit.Timer("main_select_random", "from __main__ import main_select_random")
time_taken7 = t7.timeit(number=1000)
print("time taken by the select random pivot method: %10.5f " % time_taken7, "milliseconds")


def main_select_median():
    # Create a list of N pseudo random numbers; Duplicates can occur.
    num = 10000
    my_list = list(random.randint(1, 100) for elem in range(num))
    random.shuffle(my_list)
    random.shuffle(my_list)

    # Get the value of the kth item.
    k = 7
    k_value = select_median_of_medians_pivot(my_list, k)

    # Test it
    sorted_list = sorted(my_list)
    assert sorted_list[k] == k_value


def select_median_of_medians_pivot(the_list, k):
    # If the array is short, terminate the recursion and return the value without partitioning.
    if len(the_list) <= 10:
        the_list.sort()
        return the_list[k]
    else:
        # Partition the array into subsets with a maximum of 5 elements each.
        subset_size = 5
        subsets = []  # list of subset
        num_medians = int(len(the_list) / subset_size)
        if len(the_list) % subset_size > 0: # not divisible by 5
            num_medians += 1

        for i in range(num_medians):
            beg = i * subset_size
            end = min(len(the_list), beg + subset_size)
            subset = the_list[beg:end]
            subsets.append(subset)

        # Find the medians in each subset.
        # Note that it calls select_median_of_medians_pivot() recursively taking advantage of the fact that for
        # len(array) <= 10, the select operation simply sorts the array and returns the k-th item. This could be done
        # here but since the termination condition is required to get an infinite loop we may as well use it.

        medians = []  # list of medians
        for subset in subsets:
            median = select_median_of_medians_pivot(subset, int(len(subset)/2))
            medians.append(median)

        # Now get the median of the medians recursively.
        # Assign it to the local pivot variable because the pivot handling code is the same regardless of how
        # it was generated. See select_random_pivot() for a different approach for generating the pivot.

        median_of_medians = select_median_of_medians_pivot(medians, int(len(medians)/2))
        pivot = median_of_medians  # pivot point value (not index)

        # Now select recursively using the pivot.
        # At this point we have the pivot. Use it to partition the input array into 3 categories:
        # items < the pivot value (array_lt), items > pivot value (array_gt) and items = the pivot value (equals_array).

        list_lt = []
        list_gt = []
        list_eq = []

        for item in the_list:
            if item < pivot:
                list_lt.append(item)
            elif item > pivot:
                list_gt.append(item)
            else:
                list_eq.append(item)
        # Now the array values have been partitioned according to their relation to the pivot value

        if k < len(list_lt):
            return select_median_of_medians_pivot(list_lt, k)
        elif k < len(list_lt) + len(list_eq):
            return list_eq[0]
        else:
            normalized_k = k - (len(list_lt) + len(list_eq))
            return select_median_of_medians_pivot(list_gt, normalized_k)


t8 = timeit.Timer("main_select_median()", "from __main__ import main_select_median")
time_taken8 = t8.timeit(number=1000)
print("time taken by the select median of medians pivot method: %10.5f" % time_taken8, "milliseconds")


def main_get_top_n_items():
    # Create a list of N pseudo random numbers; Duplicates can occur.
    num = 10000
    my_list = list(random.randint(1, 100) for elem in range(num))
    random.shuffle(my_list)
    random.shuffle(my_list)

    # Get the value of the kth item.
    k = 7
    k_value = get_top_n_items(my_list, k)

    # Test it
    sorted_list = sorted(my_list)
    assert sorted_list[k] == k_value


def get_top_n_items(my_list, n):
    nth = select_random_pivot(my_list, n)   # avg case: O(N), WC: O(N^2)
    top_items = []

    # Start by getting all of the values less than the top value (O(N)).
    # This guarantees that we don't miss some because there are duplicate nth values.
    for value in my_list:
        if value < nth:
            top_items.append(value)
            if len(top_items) == n:
                return top_items  # all done

    # Now get the remaining values. This is where duplicates are handled.
    for value in my_list:
        if value == nth:
            top_items.append(value)
            if len(top_items) == n:
                return top_items

        # # We should never reach this point.
        assert len(top_items) == n


t9 = timeit.Timer("main_get_top_n_items()", "from __main__ get_top_n_items")
time_taken9 = t9.timeit(number=1000)
print("time taken to get top n items: %10.5f" % time_taken9, "milliseconds")