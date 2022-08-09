from turtle import Screen, Turtle, position, colormode
from random import choice, randint



tim = Turtle()
colormode(255)
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.right(angle)
#         tim.forward(100)

# for i in range(3,11):
#     tim.color(choice(colors))
#     draw_shape(i)

# directions = ['left','right']



# def random_walk(direction):

#     if direction == 'right':
#         tim.right(90)
#     elif direction == 'left':
#         tim.left(90)
#     tim.forward(50)

# random_range = randint(10,100)
# for _ in range(random_range):
#     tim.color(random_color())
#     tim.pensize(5)
#     tim.speed(10)
#     random_walk(choice(directions))

tim.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color






def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(1)


screen = Screen()
screen.exitonclick()
