# RB, Libraries and Built-In Funtions

import turtle as t



colors = ["red", "orange", "yellow", "green", "blue", "green", "blue", "purple", "pink"]
loop_helper = 0

for num in range(360):
    t.color(loop_helper[colors])
    t.fd(5)
    t.left(5)
t.exitonclick() # creates a dotted rainbow line


t.color('pink')
t.forward(250)
t.left(120)
t.forward(250)
t.left(120)
t.forward(250)
t.left(120)
t.forward(250)
t.left(60)
t.color('purple')
t.circle(150)


t.showturtle()
t.forward(250)
t.shape("square")
t.shapesize(10)
t.hideturtle()
t.forward(100)
t.showturtle()
for x in range(0,100):
    t.tilt(x)
    t.fd(5)
    t.left(1)


    

t.exitonclick()