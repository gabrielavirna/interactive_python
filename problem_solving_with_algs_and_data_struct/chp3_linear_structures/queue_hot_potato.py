"""
Simulation: Hot Potato
=======================
- typical application for a queue - simulate a real situation that requires data to be managed in a FIFO manner.

E.g. the children’s game: Hot Potato (<=> Josephus problem: proceeding clockwise, one killed every seventh man).
Children line up in a circle & pass an item from neighbor to neighbor as fast as they can. At a certain point the
action is stopped & the child who has the item=potato is removed from the circle. Play continues until 1 child is left.

Implementation:
---------------
Input: a list of names and a constant “limit,” to be used for counting.
Returns: the name of the last person remaining after repetitive counting by num.

To simulate the circle: use a queue.
Assume that the child holding the potato will be at the front of the queue.
Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child, putting her at
the end of the line. She will then wait until all the others have been at the front before it will be her turn again.
After num dequeue/enqueue operations, the child at the front will be removed permanently and another cycle will begin.
This process will continue until only one name remains (the size of the queue is 1).

Note: the counting constant is greater than the number of names in the list =>
Not a problem since the queue acts like a circle & counting continues back at the beginning until the value is reached.
Notice: the list is loaded into the queue such that the first name on the list will be at the front of the queue.
"A" here is the first item in the list and therefore moves to the front of the queue (a variation: random counter).


"""

from projects.interactive_python.problem_solving_with_alg_and_data_struct import Queue


def hot_potato(name_list, limit):

    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:

        # simulate circle
        for i in range(limit):
            sim_queue.enqueue(sim_queue.dequeue())

            # for a in sim_queue.items:
                # print(a)

        sim_queue.dequeue()
    return sim_queue.dequeue()


def main():
    print(hot_potato(["A", "B", "C", "D", "E", "F"], 7))

# A call to the hotPotato function using 7 as the counting constant returns C.
main()
