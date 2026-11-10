# Ren Brown, 1, Turtle Race


import turtle as t
import random
import time

def go(race):
    race.forward(random.randint(0, 400))

def atom(vex):
    vex.shape("turtle")

def hover(float):
    float.penup()


t_one = t.Turtle()
t_two = t.Turtle()
t_three = t.Turtle()
t_four = t.Turtle()
t_five = t.Turtle()
t_six = t.Turtle()
t_seven = t.Turtle()
t_eight = t.Turtle()
t_nine = t.Turtle()
t_ten = t.Turtle()
t_eleven = t.Turtle()
goal = t.Turtle()

turtles = ["t_one", "t_two", "t_three", "t_four", "t_five", "t_six", "t_seven", "t_eight", "t_nine", "t_ten", "t_eleven"]

atom(t_one)
atom(t_two)
atom(t_three)
atom(t_four)
atom(t_five)
atom(t_six)
atom(t_seven)
atom(t_eight)
atom(t_nine)
atom(t_ten)
atom(t_eleven)

t_one.color("Red")
t_two.color("Orange")
t_three.color("Yellow")
t_four.color("Green")
t_five.color("Blue")
t_six.color("Purple")
t_seven.color("Magenta")
t_eight.color("Pink")
t_nine.color("Gray")
t_ten.color("Black")
t_eleven.color("Brown")

hover(t_one)
hover(t_two)
hover(t_three)
hover(t_four)
hover(t_five)
hover(t_six)
hover(t_seven)
hover(t_eight)
hover(t_nine)
hover(t_ten)
hover(t_eleven)

t_one.goto(-500, 500)
t_two.goto(-500, 400)
t_three.goto(-500, 300)
t_four.goto(-500, 200)
t_five.goto(-500, 100)
t_six.goto(-500, 0)
t_seven.goto(-500, -100)
t_eight.goto(-500, -200)
t_nine.goto(-500, -300)
t_ten.goto(-500, -400)
t_eleven.goto(-500, -500)

goal.penup()
goal.goto(500, 600)
goal.right(90)
goal.pendown()
goal.forward(1200)

while True:
    go(t_one)
    go(t_two)
    go(t_three)
    go(t_four)
    go(t_five)
    go(t_six)
    go(t_seven)
    go(t_eight)
    go(t_nine)
    go(t_ten)
    go(t_eleven)  

t.exitonclick()