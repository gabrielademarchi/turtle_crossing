from turtle import Turtle

FONT = ('Courier', 24, 'normal')
FONT_SUB = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-220, 250)
        self.level = 0
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align='center',
                   font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.home()
        self.write("Game Over",
                   align='center', font=FONT)
        # self.goto(0, -40)
        # self.write("Press 'Enter' to play again",
        #            align='center', font=FONT_SUB)
