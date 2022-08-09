from turtle import Turtle, Screen

tim = Turtle()
tina = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    tina.backward(10)

def move_backwards():
    tim.backward(10)
    tina.forward(10)
def rotate_left():
    tim.left(10)
    tina.right(10)

def rotate_right():
    tim.right(10)
    tina.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=screen.reset)



screen = Screen()
screen.exitonclick()

