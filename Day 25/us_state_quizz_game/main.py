import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Quizz Game")

image = "C:\\100-days-of-python-learning\\Day 25\\us_state_quizz_game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
        
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Countries",
                                    prompt="What's the another state's name?")
    if answer_state:
        answer_state = answer_state.title()
   
    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)        
        break
    # print(converting_to_string)
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # print(state_data.x)
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state, font=("Verdana",8, "normal"))
           


# print(isPresent)
# # if :
#     turtle.setposition(x,y)
#     turtle.write(answer_state.capitalize(), font=("Verdana",10, "normal"))


# turtle.mainloop()


