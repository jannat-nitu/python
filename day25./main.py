import csv
import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    user_choice = screen.textinput(f"{len(guess_state)}/50 guess state",
                                   "What's your guess name?").title()

    if user_choice == "Exit":
        missing_state = [state for state in all_states if state not in guess_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if user_choice in all_states:
        guess_state.append(user_choice)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_choice]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_choice)


