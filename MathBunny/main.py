
# Program Name : MathBunny
# Authors      : Sirena Salas, Aidin Tavassoli, Jared Schneider
# Description  : Educational game-based Math learning app for first graders

#=======================================================================================================================

#                                  Instructions
#                                ----------------
#       1) main function calls the following functions in order and saves
#       their values into the corresponding variables: problem, input and answer.
#       2) The input is then compared with the answer and the program responds
#       to the user (GUI) with true or false.
#       3) The program checks for exit condition to continue or exit gracefully.

import random
import tkinter as tk
from tkinter import messagebox

#=======================================================================================================================

#GLOBALS
USER_INPUT  = ""
USER_CHOICE = ""
root        = tk.Tk()
answer_var  = tk.StringVar()
problem_var = tk.StringVar()
global problem_label
root.resizable(False, False)
op1 = 1
op2 = 1
operation = 0

#=======================================================================================================================

# Function : problem_generator
# Purpose  : Produces a problem for the user using random number generation.
#            The problem would require 3 random numbers which are within the range
#            of 0-10 for the operands and 0-2 for the operations that correspond
#            to operations tuple with add, sub, mul for values.

def problem_generator():

    global op1
    global op2
    global operation

    op1 = random.randrange(0, 10, 1)
    op2 = random.randrange(0, 10, 1)

    operation = random.randrange(0, 3, 1)
    operator  = { 0: add, 1: sub, 2: mul }

    # handling the negativity: no negative results
    if operation == 1 and op1 < op2:
        temp = op1
        op1 = op2
        op2 = temp

    # handling multiplication over 4 x 4 and multiplication by 0
    if operation == 2 and (op1 > 4 or op2 > 4 or op1 == 0 or op2 == 0):
        op1 = (op1 % 4) + 1
        op2 = (op2 % 4) + 1

    func = operator.get(operation, "nothing")
    # global PROBLEM
    # PROBLEM = str(op1) + ' ' + operation_to_str(operation) + ' ' + str(op2) + ' '
    problem_var.set('What is ' + str(op1) + ' ' + operation_to_str(operation) + ' ' + str(op2) + ' ?')
    # print_problem(op1, op2, operation_to_str(operation))
    print(problem_var.get())
    return func(op1, op2)

#=======================================================================================================================

# Helper functions for problem_generator
def add(op1, op2):
    return op1 + op2


def sub(op1, op2):
    return op1 - op2


def mul(op1, op2):
    return op1 * op2


def operation_to_str(op_code):
    operation_list = {
        0: "+",
        1: '-',
        2: '*'
    }
    return operation_list[op_code]

#=======================================================================================================================

# Function : user_input_validation
# Purpose  : Validates the received value from user such as check if it is
#            numerical and within the maximum allowed number of digits.
#            If valid this function can return the user input to the program.


def user_input_validation():

    try:
        usr_input = int(input("Enter your answer: "))
        user_answr = usr_input

    except ValueError:
        print("Only integer values are accepted.")
    else:
        return user_answr

#=======================================================================================================================

# Function : checkAnswer
# Purpose  : Compares the user input with the global variable answer to be
#            in main and return the result as boolean value of correctness which
#            is used by the program to respond to user.

def check_answer(user_answr, correct_answr):
    if user_answr == correct_answr:
        return True
    else:
        return False

#=======================================================================================================================

# Function : quitApplication
# Purpose  : Exit the application returning 0

def quitApplication():
    exit(0)

#=======================================================================================================================

# Function : quitApplication
# Purpose  : Prompt user then exit the application from the game window
#            if user 'Yes' was chosen returning 0 otherwise return to the game.

def quitGame():
    USER_CHOICE = tk.messagebox.askyesno(title="Oh nooo ! ", message="Are you sure you want to quit the game ? ")
    if USER_CHOICE:
        exit(0)
    else:
        return



#=======================================================================================================================

# Function : startGame
# Purpose  : Removes the welcome page buttons from the GUI (root) and adds the game related
#            widgets and sets the program ready for game mode.


def startGame():

    start.pack_forget()  # Remove start button
    quit.pack_forget()   # Remove and replace quit button later with adjusted format
    label.pack_forget()  # Remove and replace the MathBunny logo
    label.pack(side='top', pady=10, padx=10)       # Place logo
    problem_label.pack(side='top', pady=0, padx=10)  # Solve prompt
    problem_label.place(x=180, y=175)                # Place solve prompt

    # problem_label.pack(side='top', pady=0, padx=10)  # Solve prompt
    # problem_label.place(x=180, y=175)  # Place solve prompt
   #Commented out input box image ===================================

   # answer_background = tk.Label(root, image=photo_input, borderwidth=0)
   # answer_background.place(x=125, y=575)
   # answer_background.lower()

   # ================================================================

    symbol_label.place(x=300, y=300)
    bunny_label_1.place(x=130, y=230)
    bunny_label_2.place(x=340, y=230)

    question_background = tk.Label(root, image=photo_background, borderwidth=0, pady=10)
    question_background.place(x=70, y=206)
    question_background.lower()

    answer_entry.pack(side='top', pady=100)  # Input box
    answer_entry.place(x=180, y=490)
    answer_entry.focus()
    answer_entry.bind('<Return>', (lambda event: takeInput()))  # on enter key

    # Button placements
    submit.pack(side='top', padx=0, pady=10) # Submit button
    submit.place(x=70, y=550)

    skip.pack(side='right', padx=0, pady=0)  # Skip button on the right
    skip.place(x=440, y=550)

    game_quit.pack(side='left', padx=0, pady=0)   # Quit button on the left
    game_quit.place(x=220, y=700)
    root.update_idletasks()

# NEED TO HANDLE THE INPUT AND CHECK IF CORRECT
def refreshProblem():

    global ANSWER
    ANSWER = problem_generator()

    print("inside refresh problem line 188")
    print(problem_var.get())
    # print("inside refresh problem line 188")
    # print(problem_var.get())
    problem_label.config(text=problem_var.get())
    root.update_idletasks()

    symbol_label = setSymbol(operation)

    symbol_label.place(x=300, y=300)

    bunny_label_1 = setBunny(op1)
    bunny_label_2 = setBunny(op2)

    bunny_label_1.place(x=130, y=230)
    bunny_label_2.place(x=340, y=230)


#=======================================================================================================================

# Function : takeInput
# Purpose  : When called by submit button it will set the answer_var the input from
#            answer_entry Entry widget.

def takeInput():
    global USER_INPUT
    global ANSWER
    global PROBLEM
    global problem_label
    # root.update()
    USER_INPUT = answer_entry.get()

    # Console debugging purposes
    print("User entered: ")
    print(USER_INPUT)
    print(ANSWER)
    # print("User entered: ")
    # print(USER_INPUT)
    # print(ANSWER)
    # Call check_answer
    if check_answer(int(USER_INPUT), int(ANSWER)):
        print("true")
        # print("true")
        USER_CHOICE = tk.messagebox.showinfo(title="Correct", message="Great Job! That's Correct.")
        print(USER_CHOICE)
        # print(USER_CHOICE)
        if USER_CHOICE == "ok":
            answer_entry.delete(0,'end')
            print("refresh problem line 218 ")
            # print("refresh problem line 218 ")
            refreshProblem()




    else:
        print("false")
        # print("false")
        USER_CHOICE = tk.messagebox.askyesno(title="Wrong", message="Not Quite! Do You Want To Try Again? ")
        print(USER_CHOICE)
        if USER_CHOICE:
            answer_entry.delete(0,'end')
        else:
            answer_entry.delete(0, 'end')
            refreshProblem()
    root.update()

#===== Initial problem generated========================================================================================
ANSWER = problem_generator() # Generate a problem to start the game with

#===== Configure and open the window =============================

root.title("Welcome to MathBunny")
root.geometry("600x765")
root.configure(bg="white")

#===== Images for Buttons ========================================


photo_bunny_0 = tk.PhotoImage(file="Resources/0.png")
photo_bunny_1 = tk.PhotoImage(file="Resources/1.png")
photo_bunny_2 = tk.PhotoImage(file="Resources/2.png")
photo_bunny_3 = tk.PhotoImage(file="Resources/3.png")
photo_bunny_4 = tk.PhotoImage(file="Resources/4.png")
photo_bunny_5 = tk.PhotoImage(file="Resources/5.png")
photo_bunny_6 = tk.PhotoImage(file="Resources/6.png")
photo_bunny_7 = tk.PhotoImage(file="Resources/7.png")
photo_bunny_8 = tk.PhotoImage(file="Resources/8.png")
photo_bunny_9 = tk.PhotoImage(file="Resources/9.png")

photo_start = tk.PhotoImage(file="Resources/start.png")
photo_quit = tk.PhotoImage(file="Resources/quit.png")
photo_title = tk.PhotoImage(file="Resources/title.png")
photo_background = tk.PhotoImage(file="Resources/background.png")
photo_submit = tk.PhotoImage(file="Resources/submit.png")
photo_skip = tk.PhotoImage(file="Resources/skip.png")

bunny_label_1 = tk.Label(root, image=photo_bunny_1, borderwidth = 0)
bunny_label_2 = tk.Label(root, image=photo_bunny_1, borderwidth = 0)

symbol_label = tk.Label(root, text="", font=('Arial Rounded MT Bold', 36, 'normal')) 

def setBunny(a):

    iamge = photo_bunny_0

    if a == 0:
        image = photo_bunny_0
    elif a == 1:
        image = photo_bunny_1
    elif a == 2:
        image = photo_bunny_2
    elif a == 3:
        image = photo_bunny_3
    elif a == 4:
        image = photo_bunny_4
    elif a == 5:
        image = photo_bunny_5
    elif a == 6:
        image = photo_bunny_6
    elif a == 7:
        image = photo_bunny_7
    elif a == 8:
        image = photo_bunny_8
    elif a == 9:
        image = photo_bunny_9

    bunny = tk.Label(root, image=image, borderwidth = 0, background="#e5e5e5")

    return bunny

def setSymbol(a):
    s = "+"

    if a == 0:
        s = "+"
    elif a == 1:
        s = "-"
    if a == 2:
        s = "*"

    sym = tk.Label(root, text=s, font=('Arial Rounded MT Bold', 36, 'normal'), background="#e5e5e5") 

    return sym


bunny_label_1 = setBunny(op1)
bunny_label_2 = setBunny(op2)
symbol_label = setSymbol(operation)

#===== MathBunny Logo at the top =================================

label = tk.Label(image=photo_title, borderwidth=0)
label.pack(side='top', pady=50, padx=10)   # Application logo center alignment

#===== Init Buttons ===============================================

# For the starting screen
start = tk.Button(root, text="Start", height=170, width=430, image=photo_start, command=startGame, borderwidth = 0)
start.pack(side='top', pady=50)            # Start button on the starting screen

quit = tk.Button(root, text="Quit", width=150, height=60, image=photo_quit, command=quitApplication, borderwidth = 0)
quit.pack(side='top', padx=10, pady=50)    # Quit button on starting screen

game_quit = tk.Button(root, text="Quit", width=150, height=60, image=photo_quit, command=quitGame, borderwidth = 0)
quit.pack(side='top', padx=10, pady=50)    # Quit button on the game screen screen


solve_label = tk.Label(text="Solve the problem: ", font=('Arial Rounded MT Bold', 16, 'normal'),
                       background="white")  # " Solve the problem: "
problem_label = tk.Label(text=problem_var.get(), font=('Arial Rounded MT Bold', 24, 'normal'),
                         background="white")  # Print and place the math problem on the canvas

answer_label = tk.Label(root, text="Answer: ")  # "Answer:"




# ============================Testing / Debuging entry field====================================

answer_entry = tk.Entry(root,  # Create input field
                        width=20,  # Max # of characters
                        # textvariable=answer_var,
                        font=('Arial Rounded MT Bold', 16, 'normal'), borderwidth=0, justify="center")





# Init Submit and Skip buttons the game screen
submit = tk.Button(root, text="Submit", height=100, width=348, image=photo_submit, borderwidth = 0, command=takeInput)
skip   = tk.Button(root, text="Skip", height=98, width=100, image=photo_skip, borderwidth = 0, command=refreshProblem)




# ===== CONSOLE TESTING ===========================================

print("before mainloop line 316")
print(problem_var.get())
# print(problem_var.get())
# print(ANSWER)

# =================================================================

root.mainloop()
