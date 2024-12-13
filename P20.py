import turtle

t = turtle.Turtle()

t.circle(50)

t.up()
t.goto(-20, 25)
t.setheading(-30)
t.width(2)
t.down()
t.circle(40, 65)

for i in range(-20, 40, 45):
    t.up()
    t.goto(i, 50)
    t.down()
    t.begin_fill()
    t.circle(8)
    t.end_fill()

    t.hideturtle()
    t.clone()
