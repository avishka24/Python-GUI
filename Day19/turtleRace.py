from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color:  ")
print(user_bet)

tim = Turtle()
tim.goto(x=-230, y=-100)

screen.exitonclick()