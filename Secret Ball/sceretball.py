from tkinter import *
from PIL import ImageTk, Image
import random
#Screen elemenst---------------------------------------------------------------
screen = Tk()
screen.title("Secret Ball!!")
screen.geometry("690x690+10+1")
#Variables---------------------------------------------------------------------
predictions = ["You will have a great \nday KID!","Awesome!! \nNever Miss your Breakfast!","Today you should play \n BasketBall","Complete your HomeWork \nelse Sir will Punish you."]
show = StringVar()
#Functions---------------------------------------------------------------------
def mypredictions():
    show.set(random.choice(predictions))

#Adding Image------------------------------------------------------------------
witch = ImageTk.PhotoImage(file = r"C:\Users\faculty\Desktop\Tkinter\SecretBall\witch.jpg")
img = Label(screen, image = witch, width = 700, height = 700)
img.place(x = 3, y = 5)

question = Label(screen, text = "Let me predict something for you!\nPress the predict button below. \n", background = "#010101", foreground = "white", font = "Courier 13 bold")
question.place(x = 180, y = 10)

showPredictions = Label(screen, textvariable = show, background = "#010101", foreground = "white", font = "Courier 15 bold")
showPredictions.place(x = 210, y = 230)

predict = Button(screen, text = "PREDICT", background = "#010101", foreground = "white", command = lambda : mypredictions(), font = "Courier 20 bold")
predict.place(x = 270, y = 600)
screen.mainloop()