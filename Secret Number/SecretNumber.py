from tkinter import *
import random
#Main Files---------------------------------------------------------------------
screen = Tk()
screen.title("Secret Number Guessing Game")
screen.geometry("600x650+100+100")
screen.resizable(width = False, height = False)
#Variables----------------------------------------------------------------------
guessvalue = IntVar()
trial = IntVar(value = 15)
hints = StringVar(value = "Hints Will Be Shown Here.")
secretnumberDisp = IntVar(value = 00)
secretnumber = IntVar()
secretnumber.set(random.randint(1,100))
win = StringVar(value = "Who Wins!!")
#Functions----------------------------------------------------------------------
def BtnClk(value):
    global secretnumber
    if value == "begin":
        gameframe.config(background = "yellow")
        secretnumber.set(random.randint(1,100))
        secretnumberDisp.set(value = 00)
        trial.set(value = 15)
        guessvalue.set(value = 0)
    
    elif value == "inter":
        gameframe.config(background = "yellow")
        secretnumber.set(random.randint(1,100))
        secretnumberDisp.set(value = 00)
        trial.set(value = 10)
        guessvalue.set(value = 0)
    
    elif value == "pro":
        gameframe.config(background = "yellow")
        secretnumber.set(random.randint(1,100))
        secretnumberDisp.set(value = 00)
        trial.set(value = 5)
        guessvalue.set(value = 0)

def check():
    global secretnumber, win, hints
    trl = trial.get()
    gv = guessvalue.get()
    sn = secretnumber.get()
    if trl > 1:
        if secretnumber.get()== gv:
            gameframe.config(background = "green")
            secretnumberDisp.set(secretnumber.get())
            win.set(value = "User Wins!!!")
        else:
            if gv in range(sn,sn+5) or gv in range(sn-5,sn):
                hints.set("Too Close!")
            elif gv in range(sn+5,sn+15) or gv in range(sn-15, sn-5):
                hints.set("A Little Closer!")
            else:
                hints.set("Too Far")
            trl -= 1
            trial.set(trl)
    else:
        trial.set(value = 0)
        gameframe.config(background = "red")
        secretnumberDisp.set(secretnumber.get())
        win.set(value = "Computer Wins!!!")
    #print(trl,sn)
    

#Design-------------------------------------------------------------------------
#Heading------------------------------------------------------------------------
head = Label(screen, width = "50", height = "2", text = "Welcome to Secret Number", font = "courier 15 bold")
head.grid(row = 0, column = 0, columnspan = 3)
#Partition----------------------------------------------------------------------
part1 = Label(screen, width = "50", height = "2", text = "------------------------------------------------------------------------", font = "courier 12 bold")
part1.grid(row = 1, column = 0, columnspan = 3)
#Introduction-------------------------------------------------------------------
intro = Label(screen, text = "Introduction: \nHere the player will guess a number ranging from 1 to 100. \nThe Player will get chance according to complexity.", font = "courier 8 bold")
intro.grid(row = 2, column = 0, columnspan = 3)
#Complexity---------------------------------------------------------------------
part2 = Label(screen, width = "50", height = "2", text = "------------------------------------------------------------------------", font = "courier 12 bold")
part2.grid(row = 3, column = 0, columnspan = 3)
begin = Button(screen, width = "15", text = "Beginner", command = lambda : BtnClk("begin"), font = "courier 12 bold")
begin.grid(row = 4, column = 0)
inter = Button(screen, width = "15", text = "Intermediate", command = lambda : BtnClk("inter"), font = "courier 12 bold")
inter.grid(row = 4, column = 1)
pro = Button(screen, width = "15", text = "Professional", command = lambda : BtnClk("pro"), font = "courier 12 bold")
pro.grid(row = 4, column = 2)
chance1 = Label(screen, text = "15 Trials", font = "courier 8 bold")
chance1.grid(row = 5, column = 0)
chance2 = Label(screen, text = "10 Trials", font = "courier 8 bold")
chance2.grid(row = 5, column = 1)
chance3 = Label(screen, text = "5 Trials", font = "courier 8 bold")
chance3.grid(row = 5, column = 2)
gameframe = Frame(screen, height = "400", width = "550", background = "Yellow")
gameframe.grid(row = 6, column = 0, columnspan = 3, padx = 1, pady = 5)

frameHead = Label(gameframe, text = "Enter The Guessed Number:", font = "courier 12 bold")
frameHead.grid(row = 0, column = 0, columnspan = 3)

frameenter = Entry(gameframe, textvariable = guessvalue, font = "courier 12 bold", width = 4)
frameenter.grid(row = 1, column = 0, pady = 12)

Check = Button(gameframe, text = "Check", font = "courier 12 bold", command = lambda : check())
Check.grid(row = 1, column = 1, pady = 12)

trials = Label(gameframe, text = "Trials Left", font = "courier 12 bold")
trials.grid(row = 2, column = 0, columnspan = 3, pady = 20)

trialinfo = Label(gameframe, text = trial, textvariable = trial, font = "courier 12 bold")
trialinfo.grid(row = 3, column = 0, columnspan = 3, pady = 10)

part3 = Label(screen, width = "50", height = "2", text = "------------------------------------------------------------------------", font = "courier 12 bold")
part3.grid(row = 7, column = 0, columnspan = 3)

hint = Label(screen, text = "Hint:", font = "courier 12 bold")
hint.grid(row = 8, column = 0, columnspan = 2, padx = 0)
hintInfo = Label(screen, text = hints, textvariable = hints, font = "courier 12 bold")
hintInfo.grid(row = 9, column = 0, columnspan = 2, padx = 0)

SecretNumber = Label(screen, text = "Secret Number is:", font = "courier 12 bold")
SecretNumber.grid(row = 8, column = 2, columnspan = 2, padx = 0)
SecretNumberDisplay = Label(screen, text = secretnumberDisp, textvariable = secretnumberDisp, font = "courier 12 bold")
SecretNumberDisplay.grid(row = 9, column = 2, padx = 0)

part4 = Label(screen, width = "50", height = "2", text = "--------------------------------Winner---------------------------------", font = "courier 12 bold")
part4.grid(row = 10, column = 0, columnspan = 3)

winnerDisplay = Label(screen, text = win.get(), textvariable = win, font = "courier 24 bold")
winnerDisplay.grid(row = 11, column = 0, columnspan = 3)
screen.mainloop()