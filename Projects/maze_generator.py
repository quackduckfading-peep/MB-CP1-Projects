# Ren Brown, 1, Maze Generator

import turtle as t

def row(walls, space):
    space = 0
    walls = 1
    while walls == 1:
        t.penup()
        t.left(45)
        t.forward(25)
        t.right(45)
        t.pendown()
        t.forward(25)
    while space == 0:
        t.penup()

t.showturtle()

row(1, 0)
t.exitonclick()
"""rows = [[1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1], ]"""
