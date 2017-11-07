""""
Simulation: Printing Tasks
==========================
The behavior of the printing queue:
As students send printing tasks to the shared printer, the tasks are placed in a queue to be processed in a FIFO manner.
Question: is the printer is capable of handling a certain amount of work?
If it cannot, students will be waiting too long for printing and may miss their next class.

E.g. Situation in a CS laboratory: On any average day about 10 students are working in the lab at any given hour.
These students typically print up to twice during that time, and the length of these tasks ranges from 1 to 20 pages.
The printer in the lab is older, capable of processing 10 pages per minute of draft quality.
The printer could be switched to give better quality, but then it would produce only five pages per minute.
The slower printing speed could make students wait too long.
- What page rate should be used?

Simulation: simulate the real situation as closely as possible given that you know general parameters.
----------
Build a simulation that models the laboratory. Construct representations for students, printing tasks, and the printer.
As students submit printing tasks, we will add them to a waiting list, a queue of print tasks attached to the printer.
When the printer completes a task, it will look at the queue to see if there are any remaining tasks to process.
Of interest for us is the average amount of time students will wait for their papers to be printed.
This is equal to the average amount of time a task waits in the queue.

Probabilities: to model this situation -> E.g. students may print a paper from 1 to 20 pages in length.
If each length from 1 to 20 is equally likely, the actual length for a print task can be simulated by using a random
number between 1 and 20 inclusive <=>  there is equal chance of any length from 1 to 20 appearing.

If there are 10 students in the lab and each prints twice, then there are 20 print tasks per hour on average.
What's the chance that at any given second, a print task is going to be created? => consider the ratio of tasks to time.
Twenty tasks per hour means that on average there will be one task every 180 seconds:

20 tasks/1 hour x 1 hour/60 minutes × 1 minute/60 seconds = 1 task/180 seconds

For every second we can simulate the chance that a print task occurs: generate a random number between 1 and 180 incl.
If the number is 180, we say a task has been created.
Note: it is possible that many tasks could be created in a row or we may wait quite a while for a task to appear.

Main Simulation Steps
----------------------

1. Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
2. For each second (currentSecond):
    Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
    If the printer is not busy and if a task is waiting,
        Remove the next task from the print queue and assign it to the printer.
        Subtract the timestamp from the currentSecond to compute the waiting time for that task.
        Append the waiting time for that task to a list for later processing.
        Based on the number of pages in the print task, figure out how much time will be required.
    The printer now does 1 second of printing if necessary and subtracts 1 second from the time required for that task.
    If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
3. After the simulation is complete, compute the average waiting time from the list of waiting times generated.


Python Implementation
--------------------
To design this simulation: create classes for the real-world objects: Printer, Task, and PrintQueue.

* The Printer class:
- Track whether it has a current_task.
    If yes, then it is busy and the amount of time needed can be computed from the number of pages in the task.
- The constructor will also allow the pages-per-minute setting to be initialized.
- The tick method decrements the internal timer and sets the printer to idle if the task is completed.

* The Task class
- Represent a single printing task.
    When the task is created, a random number generator will provide a length from 1 to 20 pages -> use randrange()
- Each task will also need to keep a timestamp to be used for computing waiting time.
    This timestamp will represent the time that the task was created and placed in the printer queue.
- The waitTime method can then be used to retrieve the amount of time spent in the queue before printing begins.

* The main simulation implements the algorithm described above.
The printQueue object is an instance of our existing queue ADT.
A boolean helper function, newPrintTask, decides whether a new printing task has been created.
Use randrange() to return a random integer between 1 and 180. Print tasks arrive once every 180 seconds.
By arbitrarily choosing 180 from the range of random integers, we can simulate this random event.
The simulation function allows us to set the total time and the pages per minute for the printer.

When we run the simulation, the results are different each time - due to the probabilistic nature of the random numbers.
We are interested in the trends that may be occurring as the parameters to the simulation are adjusted. Some results:

- First, run the simulation for a period of 60 minutes (3,600 seconds) using a page rate of five pages per minute.
    In addition, run 10 independent trials -> because of random numbers, each run will return different results.
    After running our 10 trials we can see that the mean average wait time is 122.09 seconds.
    You can also see that there is a large variation in the average weight time with a minimum average of 17.27 seconds
    and a maximum of 376.05 seconds. You may also notice that in only two of the cases were all the tasks completed.

- Now, adjust the page rate to 10 pages per minute, and run the 10 trials again, with a faster page rate our hope would
  be that more tasks would be completed in the one hour time frame.
"""

import random

from projects.interactive_python.problem_solving_with_alg_and_data_struct import Queue


class Printer:
    def __init__(self, pages_per_minute):
        self.page_rate = pages_per_minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def simulation(num_seconds, pages_per_min):
    lab_printer = Printer(pages_per_min)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


print("Simulation for 5 tasks per minute", "\n")
for i in range(10):
    simulation(3600, 5)

print("Simulation for 10 tasks per minute", "\n")
for j in range(10):
    simulation(3600, 10)


