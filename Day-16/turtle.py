from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# from turtle import *
# color('red', 'yellow')
# shape('turtle')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()