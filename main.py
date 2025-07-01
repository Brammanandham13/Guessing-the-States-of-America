import turtle
import pandas


screen=turtle.Screen()

image="blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_state=[]

while len(guess_state)<=50:
    answer=screen.textinput(title = f"{len(guess_state)}/50 states",prompt = "guess the state names!").title()
    print(answer)

    if answer=="Exit":
        missing=[]
        for state in all_state:
            if state not in guess_state:
                missing.append(state)
        new_data=pandas.DataFrame(missing)
        new_data.to_csv("missing states")
        break



    if answer in all_state:
        guess_state.append(answer)
        tim=turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data=data[data.state==answer]
        tim.goto(state_data.x.item(),state_data.y.item())
        tim.write(answer)

screen.exitonclick()



