from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.game_is_on = True
        
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font =("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font =("courier", 80, "normal"))    
        
    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        self.r_score += 1
        self.update_score()
        
    def winner(self):
        self.goto(0,0)
        self.game_is_on = False
        if self.l_score == 10:
            self.write("Game Over! Left side person wins", align="center", font =("courier", 20, "normal"))
        elif self.r_score == 10:
            self.write("Game Over!Rignt side person wins", align="center", font =("courier", 20, "normal"))