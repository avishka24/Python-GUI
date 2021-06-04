import another_module
from prettytable import PrettyTable
from turtle import Screen

print(another_module.another_variable)
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
screen = Screen()
screen.exitonclick()