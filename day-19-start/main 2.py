from turtle import Turtle, Screen, screensize
import random

is_race_on = False
screen = Screen()
screen.setup(width=700, height=400)



user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = -70
all_turtles = []
x_coordinates  = -(screensize()[0] / 2 - 20)

#Create 6 turtles
for turtle_index in range(0, len(colors)):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-x_coordinates, y=y_positions)
    all_turtles.append(new_turtle)
    y_positions += 30


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > x_coordinates:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()