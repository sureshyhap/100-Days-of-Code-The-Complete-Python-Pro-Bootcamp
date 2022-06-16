"""import another_module

print(another_module.another_variable)

import turtle

timmy = turtle.Turtle()
print(timmy)
my_screen = turtle.Screen()
print(my_screen.canvheight)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
my_screen.exitonclick()
"""
import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Bulbasaur", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Grass", "Water"])
table.align = "l"
print(table)