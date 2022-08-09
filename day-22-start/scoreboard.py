from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.WINNING_SCORE = 5
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner = ''
        self.y_move = 10
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.winner = ''
        if self.r_score == self.WINNING_SCORE:
            self.winner = "Player 2"
        elif self.l_score == self.WINNING_SCORE:
            self.winner = "Player 1"
        self.goto(0, 0)
        self.write(f"GAME OVER {self.winner} wins", align="center", font=("Courier", 30, "normal"))

