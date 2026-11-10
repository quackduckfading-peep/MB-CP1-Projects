# Ren Brown, 1, Turtle Race


import turtle as t
import random
import time

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


turtles = ["t_one", "t_two", "t_three", "t_four", ]

t_one.color("Red")
t_one.shape("turtle")
t_two.color("Orange")
t_two.shape("turtle")
t_three.color("Yellow")
t_three.shape("turtle")
t_four.color("Green")
t_four.shape("turtle")
t_five.color("Blue")
t_five.shape("turtle")
t_six.color("Purple")
t_six.shape("turtle")
t_seven.color("Magenta")
t_seven.shape("turtle")
t_eight.color("Pink")
t_eight.shape("turtle")
t_nine.color("Gray")
t_nine.shape("turtle")
t_ten.color("Black")
t_ten.shape("turtle")
t_eleven.shape("turtle")
t_eleven.color("Brown")

t_one.penup()
t_one.goto(-500, 500)
t_two.penup()
t_two.goto(-500, 400)
t_three.penup()
t_three.goto(-500, 300)
t_four.penup()
t_four.goto(-500, 200)
t_five.penup()
t_five.goto(-500, 100)
t_six.penup()
t_six.goto(-500, 0)
t_seven.penup()
t_seven.goto(-500, -100)
t_eight.penup()
t_eight.goto(-500, -200)
t_nine.penup()
t_nine.goto(-500, -300)
t_ten.penup()
t_ten.goto(-500, -400)
t_eleven.penup()
t_eleven.goto(-500, -500)



t.exitonclick()