from wsgiref.util import guess_scheme
import pandas
import turtle

screen = turtle.Screen()
screen.title("US States")

screen.setup(725,491)
image = "day-25-start/us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("day-25-start/us-states-game-start/50_states.csv")

game_is_on = True
guess_count = 0
while game_is_on:

    answer_state = screen.textinput(f"{guess_count}/50 Enter a State", "Please Guess a State").title()

    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    if data[data.state == answer_state].empty == False:
        state_info =data[data.state == answer_state]
        x = int(state_info.x)
        y = int(state_info.y)
        state = state_info.state.item()
        guess_count += 1
        new_turtle.setx(x)
        new_turtle.sety(y)
        new_turtle.write(f"{state}")


screen.exitonclick()