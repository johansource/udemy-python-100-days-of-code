import turtle as t
import random

bob_ross = t.Turtle()
t.colormode(255)
bob_ross.shape("turtle")
bob_ross.color("mediumpurple")
bob_ross.pensize(1)

# colours = ["RosyBrown3", "LightSalmon3", "DarkKhaki", "OliveDrab3", "MediumSeaGreen", "CadetBlue3", "SteelBlue3", "SlateBlue4"]
directions = [0, 90, 180, 270]

# def setup_shapes():
#     terry.pensize(5)
#     terry.up()
#     terry.left(180)
#     terry.forward(100)
#     terry.right(90)
#     terry.forward(200)
#     terry.right(90)
#     terry.down()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         terry.forward(200)
#         terry.right(angle)

# def draw_shapes():
#     setup_shapes()
#     for shape_side_n in range(3, 11):
#         terry.pencolor(colours[shape_side_n - 3])
#         draw_shape(shape_side_n)

# draw_shapes()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# def random_walk(num_walks):
#     terry.speed("fastest")
#     for _ in range(num_walks):
#         terry.pencolor(random_color())
#         terry.setheading(random.choice(directions))
#         terry.forward(30)

# random_walk(100)

def draw_spirograph(size_of_gap):
    bob_ross.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        bob_ross.pencolor(random_color())
        bob_ross.circle(100)
        bob_ross.setheading(bob_ross.heading() + size_of_gap)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
