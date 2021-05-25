from tkinter import *
import random
#Basic Configurations--------------------------------------------
root = Tk()
root.title("Rock Paper Scissor")
root.geometry("500x500+20+20")
#Variables-------------------------------------------------------
List = ["Rock","Paper","Scissor"]
Rock = StringVar(value = "Rock")
Paper = StringVar(value = "Paper")
Scissor = StringVar(value = "Scissor")
userWon = IntVar(value = 0)
compWon = IntVar(value = 0)
userChoice = StringVar(value = " ")
compChoice = StringVar(value = " ")
win = StringVar(value = " ")
#Functions-------------------------------------------------------

def WinCheck(obj):
    global userWon, compWon, userChoice, compChoice, win
    compChoice.set(random.choice(List))
    userChoice.set(obj.get())
    user = obj.get()
    comp = compChoice.get()
    if user == "Rock" and comp == "Rock" or user == "Paper" and comp == "Paper" or user == "Scissor" and comp == "Scissor":
        win.set(value = "Its a Tie!!!")
    elif user == "Rock" and comp == "Paper" or user == "Paper" and comp == "Scissor" or user == "Scissor" and comp == "Rock":
        win.set(value = "Computer Wins!!!")
        compWon.set(compWon.get()+1)
    else:
        win.set(value = "User Wins!!!")
        userWon.set(userWon.get()+1)
#Heading Lebel---------------------------------------------------
head = Label(root, name = "lbl", text = "Welcome to Rock Paper Scissor.", font = "corbel 22 bold")
head.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 5)
Partition1 = Label(root, text = "---------------------------------------------------------------------------------------")
Partition1.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 5)
#Buttons---------------------------------------------------------
Partition2 = Label(root, text = "----------     Click On Any Button To Start     ----------", font = "corbel 10 bold")
Partition2.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 5)

rock = Button(root, text = "Rock", textvariable = Rock, command = lambda : WinCheck(Rock), font = "corbel 18 bold", width = 10)
rock.grid(row = 3, column = 0)

paper = Button(root, text = "Paper", textvariable = Paper, command = lambda : WinCheck(Paper), font = "corbel 18 bold", width = 10)
paper.grid(row = 3, column = 1)

scissor = Button(root, text = "Scissor", textvariable = Scissor, command = lambda : WinCheck(Scissor), font = "corbel 18 bold", width = 10)
scissor.grid(row = 3, column = 2)

#User and Computer Profile---------------------------------------
Partition3 = Label(root, text = "---------------------------------------------------------------------------------------")
Partition3.grid(row = 4, column = 0, columnspan = 3, padx = 20, pady = 5)

UserChoice = Label(root, text = "User Choose:", font = "corbel 15 bold")
UserChoice.grid(row = 5, column = 0)
UserChoiceDisplay = Label(root,text = userChoice.get(), textvariable = userChoice, font = "corbel 10 bold")
UserChoiceDisplay.grid(row = 6, column = 0)

ComputerChoice = Label(root, text = "Computer Choose:", font = "corbel 15 bold")
ComputerChoice.grid(row = 5, column = 2)
ComputerChoiceDisplay = Label(root, text = compChoice.get(), textvariable = compChoice, font = "corbel 10 bold")
ComputerChoiceDisplay.grid(row = 6, column = 2)
#Score Board-----------------------------------------------------
Partition4 = Label(root, text = "----------     Score Board     ----------", font = "corbel 10 bold")
Partition4.grid(row = 7, column = 0, columnspan = 3, padx = 20, pady = 5)

UserWon = Label(root, text = "User Won::", font = "corbel 15 bold")
UserWon.grid(row = 8, column = 0)
UserWonDisplay = Label(root, text = userWon.get(), textvariable = userWon, font = "corbel 15 bold")
UserWonDisplay.grid(row = 8, column = 1)

CompWon = Label(root, text = "Computer Won:", font = "corbel 15 bold")
CompWon.grid(row = 9, column = 0)
CompWonDisplay = Label(root, text = compWon.get(), textvariable = compWon, font = "corbel 15 bold")
CompWonDisplay.grid(row = 9, column = 1)
#Display Winner--------------------------------------------------
Partition5 = Label(root, text = "------------------------------     Winner     ------------------------------", font = "corbel 12 bold")
Partition5.grid(row = 10, column = 0, columnspan = 3, padx = 20, pady = 5)
Winner = Label(root, text = win.get(), textvariable = win, font = "corbel 25 bold")
Winner.grid(row = 11, column = 0, columnspan = 3, padx = 20, pady = 5)

#MainLoop--------------------------------------------------------
root.mainloop()