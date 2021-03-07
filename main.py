import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    guess_state = screen.textinput(title=f'{len(guessed_states)}/50 States guessed',
                                   prompt="Name Another state: ").title()
    guess_state.lower()
    print(guess_state)
    if guess_state == "Exit":
        break
    if guess_state in all_states:
        guessed_states.append(guess_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess_state)


missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)


missed_states = pd.DataFrame(missed_states)
missed_states.to_csv("States to learn.csv")
