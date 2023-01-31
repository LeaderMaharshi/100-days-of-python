from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


#paddle movements
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while scoreboard.game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect the collision with wall toop and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect r_paddle missing
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.winner()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.winner()
        


screen.exitonclick()