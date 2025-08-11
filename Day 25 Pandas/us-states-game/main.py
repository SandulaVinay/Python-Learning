import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
state_list = states_data.state.to_list()
x_co_ordinate = states_data.x
y_co_ordinate = states_data.y

gussed_state = []
while len(gussed_state) < 50:

    answer_state = screen.textinput(
        title=f"{len(gussed_state)}/50 States Correct",
        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in gussed_state:
                missing_states.append(state)
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("States to learn.csv")
        break

    if answer_state in state_list and answer_state not in gussed_state:
        gussed_state.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = states_data[states_data.state == answer_state]
        new_turtle.goto(state_data.x.item(), state_data.y.item())
        new_turtle.write(answer_state)

# screen.exitonclick()