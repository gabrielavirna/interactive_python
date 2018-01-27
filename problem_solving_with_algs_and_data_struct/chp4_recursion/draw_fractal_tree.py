"""
Fractals
--------
Fractals have much in common with recursion.
When you look at it the fractal has the same basic shape no matter how much you magnify it.
E.g. from nature: the coastlines of continents, snowflakes, mountains, trees or shrubs.

The fractal nature of many of these natural phenomenon makes it possible for programmers to generate very realistic
looking scenery for computer generated movies.


Draw (generate) a fractal tree - use Turtle
------------------------------

Describe a tree using a fractal vocabulary (= something that looks the same at all different levels of magnification)
=> Even a small twig has the same shape & characteristics as a whole tree.
=> A tree is a trunk, with a smaller tree going off to the right and another smaller tree going off to the left.

Using this definition recursively => apply the recursive definition of a tree to both of the smaller left & right trees.


After runnig the code, notice how each branch point on the tree corresponds to a recursive call, and notice how the tree
is drawn to the right all the way down to its shortest twig.
After that, notice how the program works its way back up the trunk until the entire right side of the tree is drawn.
Then the left side of the tree is drawn, but not by going as far out to the left as possible. Rather, once again the
entire right side of the left tree is drawn until we finally make our way out to the smallest twig on the left.

../_images/tree1.png
../_images/tree2.png


Exercise
--------
Modify the recursive tree program using one or all of the following ideas:

Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range.
For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in
some range.



"""
import turtle


def draw_fractal_tree(branch_length, my_turtle):
    # check for the base case of branch_length getting too small.
    if branch_length > 5:
        my_turtle.forward(branch_length)
        my_turtle.right(20)
        # turtle makes a recursive call after the turtle turns to the right by 20 degrees (the right tree)
        # for each recursive call to tree, subtract some amount from the length
        # to make sure that the recursive trees get smaller and smaller.
        draw_fractal_tree(branch_length - 15, my_turtle)
        my_turtle.left(40)
        # turtle makes another recursive call after turning left by 40 degrees.
        # 40 dregrees because it needs to undo the original 20 degree right turn  & then do an 20 degree left turn
        draw_fractal_tree(branch_length - 10, my_turtle)
        my_turtle.right(20)
        my_turtle.backward(branch_length)


def main():
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_fractal_tree(75, t)
    my_window.exitonclick()

if __name__ == "__main__":
    main()