"""
Sierpinski Triangle
--------------------
The Sierpinski triangle is a fractal with the property of self-similarity. It illustrates a 3-way recursive algorithm.

Drawing a Sierpinski triangle (by hand procedure):
------------------------------------------------------
Start with a single large triangle. Divide this large triangle into 4 new triangles by connecting the midpoint of each
side. Ignoring the middle triangle that you just created, apply the same procedure to each of the 3 corner triangles.
Each time you create a new set of triangles, you recursively apply this procedure to the 3 smaller corner triangles.
You can continue to apply this procedure indefinitely if you have a sharp enough pencil.

The base case:
--------------
Since we can continue to apply the algorithm indefinitely, the base case is set arbitrarily as the number of times we
want to divide the triangle into pieces. This number is a.k.a the “degree” of the fractal. Each time we make a recursive
call, we subtract 1 from the degree until we reach 0. When we reach a degree of 0, we stop making recursive calls.


Implementation:
---------------
The first thing sierpinski does is draw the outer triangle. Next, there are three recursive calls, one for each of the
new corner triangles we get when we connect the midpoints (use of the standard turtle module).

Think about the order in which the triangles will be drawn. While the exact order of the corners depends upon how the
initial set is specified, let’s assume that the corners are ordered lower left, top, lower right.
Because of the way the sierpinski function calls itself, sierpinski works its way to the smallest allowed triangle in
the lower-left corner, and then begins to fill out the rest of the triangles working back.
Then it fills in the triangles in the top corner by working toward the smallest, topmost triangle.
Finally, it fills in the lower-right corner, working its way toward the smallest triangle in the lower right.

"""

import turtle


def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_middle_point(p1, p2):
    return (p1[0] + p2[0])/2, (p1[1] + p2[1])/2


def sierpinski(points, degree, my_turtle):
    color_map = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(points, color_map[degree], my_turtle)

    if degree > 0:
        sierpinski([points[0], get_middle_point(points[0], points[1]), get_middle_point(points[0], points[2])],
                   degree - 1, my_turtle)

        sierpinski([points[1], get_middle_point(points[0], points[1]), get_middle_point(points[1], points[2])],
                   degree - 1, my_turtle)

        sierpinski([points[2], get_middle_point(points[2], points[1]), get_middle_point(points[0], points[2])],
                   degree - 1, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(my_points, 3, my_turtle)
    my_window.exitonclick()

main()