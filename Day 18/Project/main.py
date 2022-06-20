"""
import colorgram

colors = colorgram.extract("image.jpeg", 25)
colors_list = []
for color in colors:
    colors_list.append(tuple(color.rgb))

print(colors_list)
"""
import turtle as t
import random

t.colormode(255)
colors_list = [(236, 236, 242), (240, 229, 236), (241, 231, 220), (224, 162, 69), (228, 240, 235), (19, 44, 82), (133, 62, 85), (171, 65, 45), (125, 39, 60), (23, 85, 61), (22, 114, 140), (58, 46, 35), (244, 197, 53), (194, 138, 160), (60, 136, 75), (225, 83, 45), (230, 174, 191), (28, 61, 53), (58, 71, 38), (155, 188, 179), (194, 101, 133), (165, 204, 199), (55, 29, 44), (153, 170, 183), (32, 40, 102)]
cursor = t.Turtle()
cursor.penup()
cursor.setposition(-150, -150)
cursor.pendown()
cursor.hideturtle()
for i in range(10):
    for j in range(10):
        cursor.dot(20, random.choice(colors_list))
        cursor.penup()
        cursor.forward(50)
        cursor.pendown()
    cursor.penup()
    cursor.left(90)
    cursor.forward(50)
    cursor.setx(-150)
    cursor.right(90)
    cursor.pendown()


screen = t.Screen()
screen.exitonclick()
