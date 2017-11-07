"""
Anagram detection problem for strings
-------------------------------------
 - One string is an anagram of another if the second is simply a rearrangement of the first.
   E.g. 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well.

 - A good example problem for showing algorithms with different orders of magnitude

* Solution 1: Checking Off
Solution checks to see that each character in the first string actually occurs in the second.
If it is possible to “checkoff” each character, then the two strings must be anagrams.
Checking off a character will be accomplished by replacing it with the special Python value None.

To analyze this algorithm:
- each of the n characters in s1 will cause an iteration through up to n characters in the list from s2.
Each of the n positions in the list will be visited once to match a character from s1.
- The number of visits: the sum of the integers from 1 to n = n(n+1)/2 = 1/2* n^2 + 1/2*n.
As n gets large, the n^2 term will dominate the n term and the 1/2can be ignored => this solution is O(n2^2).

* Solution 2: Sort and Compare
Even though s1 and s2 are different, they are anagrams only if they consist of exactly the same characters.
So, if we begin by sorting each string alphabetically, from a to z, we will end up with the same string if the original
two strings are anagrams.

To analyze this algorithm:
At first glance you may be tempted to think that this algorithm is O(n), since there is one simple iteration to compare
the n characters after the sorting process. However, the two calls to the Python sort method have their cost: sorting is
typically either O(n^2) or O(nlogn), so the sorting operations dominate the iteration.
=> This algorithm will have the same order of magnitude as that of the sorting process.

* Solution 3: Brute Force
A brute force technique for solving a problem typically tries to exhaust all possibilities.
We can simply generate a list of all possible strings using the characters from s1 and then see if s2 occurs.
However, when generating all possible strings from s1, there are n possible first characters, n−1 possible characters
for the second position, n−2for the third, and so on.
=> The total number of candidate strings is n∗(n−1)∗(n−2)∗...∗3∗2∗1, which is n!. Although some of the strings may be
duplicates, the program cannot know this ahead of time and so it will still generate n! different strings.

It turns out that n! grows even faster than 2^n as n gets large. In fact, if s1 were 20 characters long, there would be
20!=2,432,902,008,176,640,000 possible candidate strings. If we processed one possibility every second, it would still
take us 77,146,816,596 years to go through the entire list. This is probably not going to be a good solution.

* Solution 4: Count and Compare
Any two anagrams will have the same number of a’s, the same number of b’s, the same number of c’s, and so on.
In order to decide whether two strings are anagrams, we will first count the number of times each character occurs.
Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character.
Each time we see a particular character, we will increment the counter at that position.
In the end, if the two lists of counters are identical, the strings must be anagrams.

To analyze this algorithm:
Again, the solution has a number of iterations. However, unlike the first solution, none of them are nested.
The first two iterations used to count the characters are both based on n.
The 3rd iteration, comparing the 2 lists of counts, takes 26 steps since there're 26 possible characters in the strings.
=> T(n) = 2n+26 steps => O(n). We have found a linear order of magnitude algorithm for solving this problem.

Note: make decisions between time and space trade-offs:
there are space requirements:although the last solution was able to run in linear time, it could only do so by using
additional storage to keep the two lists of character counts e.g. this algorithm sacrificed space in order to gain time.

"""


# Solution 1: Checking Off
def anagram_detection(s1, s2):
    # since strings in Python are immutable, convert the second string to a list:
    a_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        # Each character from the 1st string can be checked against the characters in the list
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1

        # and if found, checked off by replacement (with value None)
        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok


print(anagram_detection('abcde', 'ecdba'))


def anagram_detection2(s1, s2):
    # we can use the built-in sort method on lists by simply converting each string to a list at the start.
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(a_list1) and matches:
        if a_list1[pos] == a_list2[pos]:
            matches = True
            pos += 1
        else:
            matches = False

    return matches

print(anagram_detection2('abcde', 'ecdba'))


def anagram_detection4(s1, s2):
    # Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character
    count1 = [0]*26
    count2 = [0]*26

    for i in range(len(s1)):
        #  Each time we see a particular character, we will increment the counter at that position
        pos = ord(s1[i]) - ord('a')
        count1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        count2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        # if the two arrays of counters are identical, the strings must be anagrams.
        if count1[j] == count2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok

print(anagram_detection4('abcde', 'cdeba'))


#  Q.Given the following code fragment, what is its Big-O running time?

# A. A singly nested loop is O(n^2)
def q1(n):
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j


# A. Even though there are two loops they are not nested.  O(2n) but we can ignore the constant 2 => O(n).
def q2(n):
    test = 0
    for i in range(n):
        test = test + 1

    for j in range(n):
        test = test - 1


# The value of i is cut in half each time through the loop so it will only take log n iterations => O(log n).
def q3(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2