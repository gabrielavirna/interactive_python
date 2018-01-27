"""
Exploring a Maze
-----------------
- a problem that has relevance to the expanding world of robotics: How do you find your way out of a maze?
(If you have a Roomba vacuum cleaner for your dorm room, you could reprogram it)

The problem: help our turtle find its way out of a virtual maze.
Assume that our turtle is dropped down somewhere into the middle of the maze and must find its way out.

The maze problem: Theseus who was sent into a maze to kill the minotaur.
Theseus used a ball of thread to help him find his way back out again once he had finished off the beast.


To make it easier: our maze is divided up into “squares.” Each square of the maze is either open or occupied by a
section of wall. The turtle can only pass through the open squares of the maze. If the turtle bumps into a wall it must
try a different direction. The turtle will require a systematic procedure to find its way out of the maze.

The procedure:
---------------
From our starting position we will first try going North one square and then recursively try our procedure from there.
If we are not successful by trying a Northern path as the first step then we will take a step to the South and
recursively repeat our procedure.
If South does not work then we will try a step to the West as our first step and recursively apply our procedure.
If North, South, West haven't been successful then apply the procedure recursively from a position one step to our East.
If none of these directions works then there is no way to get out of the maze and we fail.
To avoid an infinite loop we must have a strategy to remember where we have been.

Base cases:
-----------
The turtle has run into a wall. Since the square is occupied by a wall no further exploration can take place.
The turtle has found a square that has already been explored. We do not want to continue exploring from this position or
we will get into a loop.
We have found an outside edge, not occupied by a wall. In other words we have found an exit from the maze.
We have explored a square unsuccessfully in all four directions.


"""


import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self,mazeFileName):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(mazeFileName,'r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.startRow = rows_in_maze
                    self.startCol = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.xTranslate = -columns_in_maze/2
        self.yTranslate = rows_in_maze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columns_in_maze-1)/2-.5,-(rows_in_maze-1)/2-.5,(columns_in_maze-1)/2+.5,(rows_in_maze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.maze_list[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)

    def __getitem__(self,idx):
        return self.maze_list[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze_data_file')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
