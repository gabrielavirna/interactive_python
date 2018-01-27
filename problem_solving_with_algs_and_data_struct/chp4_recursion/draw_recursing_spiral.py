"""
Turtle - Python’s graphics module
---------------------------------
The turtle metaphor:
You can create a turtle and the turtle can move forward, backward, turn left, turn right, etc. The turtle
can have its tail up or down. When the turtle’s tail is down and the turtle moves it draws a line as it moves.

E.g. Draw a spiral recursively.

"""

import turtle

# when the turtle is created
my_turtle = turtle.Turtle()
# it also creates a window for itself to draw in
my_window = turtle.Screen()


def draw_spiral(my_turtle, line_length):
    if line_length > 0:
        # forward() tells the turtle to move forward by the given distance.
        my_turtle.forward(line_length)
        # right() takes a number of degrees which you want to rotate to the right
        # right angle 90 needed for a square
        my_turtle.right(90)
        draw_spiral(my_turtle, line_length - 5)


def main():
    draw_spiral(my_turtle, 100)
    #  to keep the window open until you click on it:
    my_window.exitonclick()

if __name__ == "__main__":
    main()