from turtle import Turtle

ALIGN = "center"  # Alignment for text
FONT = ("Courier", 32, "normal")  # Font style for text


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("lightblue")
        self.hideturtle()
        self.goto(0, 260)  # Position the scoreboard at the top center of the screen
        self.level = 1  # Initial level is set to 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear any previous text on the scoreboard
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)  # Display the current level

    def increase_level(self):
        self.level += 1  # Increase the level by 1
        self.update_scoreboard()  # Update the scoreboard to display the new level

    def game_over(self):
        self.goto(0, 0)  # Position the text at the center of the screen
        self.write("GAME OVER", align=ALIGN, font=FONT)  # Display the "GAME OVER" message
