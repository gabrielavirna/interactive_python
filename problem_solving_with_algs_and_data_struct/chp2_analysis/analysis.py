"""

* Comparing algorithms: based upon the amount of computing resources that each algorithm requires to solve the problem.
Resources:
-> space/ memory
-> time

Running time:
sum_of_n() vs sum_of_n2() vs sum_of_n3()

Notice:
==> (first 2 methods) iterative solutions: program steps repeated =>  it takes longer time; increases as we increase n
==> the 3rd method: 1)the times are shorter 2)they are very consistent no matter what the value of n.
It appears that sumOfN3 is hardly impacted by the number of integers being added.


* Execution time for an algorithm: the number of steps required to solve the problem.
  T(n) is the time it takes to solve a problem of size n, namely 1+n steps.”


Order of magnitude (Big-O notation): sum_of_n() vs sum_of_n2() vs sum_of_n3()

sum_of_n(): T(n) = 1+n ~ T(n) (1 assignment statements (theSum=0) +  n (the number of times we perform theSum=theSum+i).

* Sometimes the performance of an algorithm depends on the exact values of the data rather than simply the size of the
problem => characterize the performance of these algorithms using: best case, worst case, average case performance.


f(n)	Name
1	    Constant
log 	Logarithmic
n   	Linear
nlogn	Log Linear
n^2  	Quadratic
n^3	    Cubic
2^n  	Exponential


Check performance_example():
The number of assignment operations is the sum of four terms.
The first term is the constant 3, representing the three assignment statements at the start of the fragment.
The second term is 3n^2, since there are three statements that are performed n^2 times due to the nested iteration.
The third term is 2n, two statements iterated n times.
The fourth term is the constant 1, representing the final assignment statement.
This gives us T(n)=3+3n^2+2n+1=3n^2+2n+4 => code is O(n^2) because by looking at the exponents, we can see that the n^2
term will be dominant ; all of the other terms & the coefficient on the dominant term can be ignored as n grows larger.
"""


import time


def sum_of_n(n):

    start = time.time()

    the_sum = 0
    for i in range(1, n+1):
        the_sum += i

    end = time.time()

    return the_sum, end - start


# print(sum_of_n(10))
for i in range(5):
    print("Sum is: %d required: %10.7f seconds" % sum_of_n(1000000))

print("\n")


def sum_of_n2(tom):

    start = time.time()

    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred += barney

    end = time.time()

    return fred, end - start

# print(foo(10))
for j in range(5):
    print("Sum is: %d required: %10.7f seconds" % sum_of_n2(1000000))

print("\n")


def sum_of_n3(n):
    start = time.time()

    the_sum = n*(n+1)/2

    end = time.time()
    return the_sum, end - start


print("Sum is: %d required: %10.7f seconds" % sum_of_n3(10000))
print("Sum is: %d required: %10.7f seconds" % sum_of_n3(100000))
print("Sum is: %d required: %10.7f seconds" % sum_of_n3(1000000))
print("Sum is: %d required: %10.7f seconds" % sum_of_n3(10000000))
print("Sum is: %d required: %10.7f seconds" % sum_of_n3(100000000))


def performance_example(n):
    a = 5
    b = 6
    c = 10
    for i in range(n):
        for j in range(n):
            x = i * i
            y = j * j
            z = i * j
    for k in range(n):
        w = a * k + 45
        v = b * b
    d = 33
