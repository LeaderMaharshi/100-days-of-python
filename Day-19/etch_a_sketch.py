from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backword():
    tim.backward(10)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backword, 's')
screen.onkey(move_right, 'd')
screen.onkey(move_left, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()