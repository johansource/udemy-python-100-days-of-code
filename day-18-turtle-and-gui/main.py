import random
import turtle as t
import colorgram as cg

t.colormode(255)
bob_ross = t.Turtle()
bob_ross.up()
bob_ross.speed(0)
bob_ross.hideturtle()

def get_rgb_colors():
    colours = []
    extracted_colours = cg.extract('day-18-turtle-and-gui/image.jpg', 15)
    for colour in extracted_colours:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        colours.append((r, g, b))
    return colours

def draw_hirst_dots(size_of_grid, dot_size, spacing):
    rgb_colours = get_rgb_colors()
    center_offset = (size_of_grid / 2 * spacing)
    bob_ross.teleport(-center_offset, center_offset)
    for _ in range(size_of_grid):
        for _ in range(size_of_grid):
            bob_ross.dot(dot_size, random.choice(rgb_colours))
            bob_ross.teleport(bob_ross.xcor() + spacing, bob_ross.ycor())
        bob_ross.teleport(-center_offset, bob_ross.ycor() - spacing)

draw_hirst_dots(10, 50, 75)

screen = t.Screen()
screen.exitonclick()
