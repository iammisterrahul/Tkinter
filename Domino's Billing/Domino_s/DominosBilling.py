from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pyglet
import re
import sqlite3

screen = Tk()
screen.title("Dominos Billing System")
screen.geometry("1300x700+0+0")
screen.resizable(height = False, width = False)
screen.config(background = "#4066a3")
pyglet.font.add_file("Chango-Regular.ttf")
#Database-------------------------------------------------------------------------------------
con = sqlite3.connect("DomData.db")
cur = con.cursor()
try:
    cur.execute("create table DomTable (c_id INTEGER PRIMARY KEY AUTOINCREMENT, c_name TEXT, c_mobile INTEGER, pizza_name TEXT, pizza_price INTEGER, topping_name TEXT, topping_price INTEGER, qty INTEGER, gst REAL, total REAL); ")
except:
    pass
#Adding Photo Directory-----------------------------------------------------------------------
thin = ImageTk.PhotoImage(file = r"C:\Users\Rahul\Desktop\Tkinter\Pizza\thin1.png")
thick = ImageTk.PhotoImage(file = r"C:\Users\Rahul\Desktop\Tkinter\Pizza\thick1.png")
cheese = ImageTk.PhotoImage(file = r"C:\Users\Rahul\Desktop\Tkinter\Pizza\cheese1.png")
pan = ImageTk.PhotoImage(file = r"C:\Users\Rahul\Desktop\Tkinter\Pizza\pan1.png")
#Variables------------------------------------------------------------------------------------
name = StringVar()
mobile = StringVar(value = None)
qty = IntVar(value = 1)
pizzaprice = IntVar(value = 0)
toppingprice = IntVar(value = 0)
GST = IntVar(value = 0)
TOTAL = IntVar(value = 0)
#Functions------------------------------------------------------------------------------------
def removeQty():
    global qty
    if qty.get() > 0:
        qty.set(qty.get()-1)
    TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())

def addQty():
    global qty
    qty.set(qty.get()+1)
    TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())


def choosePizza(pzname,price):
    global qty,pz1,pz2,pz3,pz4
    pz1 = False
    pz2 = False
    pz3 = False
    pz4 = False

    if pzname == "Thin Crust":
        pz1 = True
        pizza1lbl.config(background = "#de2828")
        pizzaprice.set(price)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
    else:
        pz1 = False
        pizza1lbl.config(background = "#1f3f82")

    if pzname == "Thick Crust":
        pz2 = True
        pizza2lbl.config(background = "#de2828")
        pizzaprice.set(price)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100)
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
    else:
        pz2 = False
        pizza2lbl.config(background = "#1f3f82")
    
    if pzname == "Cheese Burst":
        pz3 = True
        pizza3lbl.config(background = "#de2828")
        pizzaprice.set(price)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
    else:
        pz3 = False
        pizza3lbl.config(background = "#1f3f82")

    if pzname == "Pan Pizza":
        pz4 = True
        pizza4lbl.config(background = "#de2828")
        pizzaprice.set(price)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
    else:
        pz4 = False
        pizza4lbl.config(background = "#1f3f82")

def pizzaCheck():
    if pz1 == True:
        return "Thin Crust"
    elif pz2 == True:
        return "Thick Crust"
    elif pz3 == True:
        return "Cheese Burst"
    elif pz4 == True:
        return "Pan Pizza"
    else:
        return ""

def toppings(tname,prices):
    t1 = False
    t2 = False
    t3 = False
    t4 = False
    t5 = False
    global qty
    if tname == "Pepperoni":
        t1 = True
        toppingtype1.config(background = "#de2828")
        toppingprice.set(prices)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
        global PizzaName, toppingName
        PizzaName = pizzaCheck()
        toppingName = tname
    else:
        t1 = False
        toppingtype1.config(background = "#1f3f82")
    
    if tname == "Mushrooms":
        t2 = True
        toppingtype2.config(background = "#de2828")
        toppingprice.set(prices)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
        PizzaName = pizzaCheck()
        toppingName = tname
    else:
        t2 = False
        toppingtype2.config(background = "#1f3f82")
    
    if tname == "Onions":
        t3 = True
        toppingtype3.config(background = "#de2828")
        toppingprice.set(prices)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
        PizzaName = pizzaCheck()
        toppingName = tname
    else:
        t3 = False
        toppingtype3.config(background = "#1f3f82")
    
    if tname == "Extra Cheese":
        t4 = True
        toppingtype4.config(background = "#de2828")
        toppingprice.set(prices)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
        PizzaName = pizzaCheck()
        toppingName = tname
    else:
        t4 = False
        toppingtype4.config(background = "#1f3f82")
    
    if tname == "Black Olives":
        t5 = True
        toppingtype5.config(background = "#de2828")
        toppingprice.set(prices)
        GST.set((pizzaprice.get() + toppingprice.get())*18/100 )
        TOTAL.set((pizzaprice.get() + toppingprice.get() + GST.get()) * qty.get())
        PizzaName = pizzaCheck()
        toppingName = tname
    else:
        t5 = False
        toppingtype5.config(background = "#1f3f82")

def checkpay():
    try:
        mob = mobile.get()
        a = re.compile("(0/91)?[7-9][0-9]{9}")
        print(a.match(mob))
        if name.get() == "" or mobile.get() == None:
            messagebox.showerror("Improper Entry.","Enter Your Name and Mobile Number")
        elif not a.match(mob):
            messagebox.showerror("Invalid Entry","Invalid Mobile Number")
        else:
            cur.execute(f"INSERT INTO DomTable(c_name,c_mobile,pizza_name,pizza_price,topping_name,topping_price,qty,gst,total) VALUES('{name.get()}', {mobile.get()}, '{PizzaName}', {pizzaprice.get()}, '{toppingName}', {toppingprice.get()}, {qty.get()}, {GST.get()}, {TOTAL.get()});")
            con.commit()
            sec = Toplevel()
            sec.title("Payee Details.")
            sec.resizable(height = False, width = False)
            sec.geometry("500x500")
            #Database-------------------------------------------------------------------------------------
            try:
                cur.execute("SELECT * FROM DomTable")
                a = cur.fetchall()[-1]
            except:
                pass

            #Variables------------------------------------------------------------------------------------
            c_name = StringVar(value = a[1])
            c_mobile = IntVar(value = a[2])
            pzname = StringVar(value = a[3])
            pzprice = IntVar(value = a[4])
            topname = StringVar(value = a[5])
            topprice = IntVar(value = a[6])
            quantity = IntVar(value = a[7])
            pzgst = IntVar(value = a[8])
            pztotal = IntVar(value = a[9])
            con.close()
            #sec.option_add("*font","Courier 20 bold")
            #Heading--------------------------------------------------------------------------------------
            heading = Label(sec, text = "Thanks For Purchasing from Domino's", font = "Courier 18 bold")
            heading.grid(row = 0, column = 0, columnspan = 3, padx = 5)

            div = Label(sec, text = "--------------------------------------------------------------------------------")
            div.grid(row = 1, column = 0, columnspan = 3)
            #Rows and Cols--------------------------------------------------------------------------------
            cname = Label(sec, text = "Name:", font = "Courier 15 bold")
            cname.grid(row = 2, column = 0, sticky = "NE", pady = 5)
            cnameDisp = Label(sec, textvariable = c_name,  font = "Courier 15 bold italic")
            cnameDisp.grid(row = 2, column = 1)

            cmobile = Label(sec, text = "Mobile:", font = "Courier 15 bold")
            cmobile.grid(row = 3, column = 0, sticky = "NE", pady = 5)
            cmobileDisp = Label(sec, textvariable = c_mobile, font = "Courier 15 bold italic")
            cmobileDisp.grid(row = 3, column = 1)

            pizza = Label(sec, text = "Pizza Name:", font = "Courier 15 bold")
            pizza.grid(row = 4, column = 0, sticky = "NE", pady = 5)
            pizzaDisp = Label(sec, textvariable = pzname, font = "Courier 15 bold italic")
            pizzaDisp.grid(row = 4, column = 1)

            pizza_price = Label(sec, text = "Pizza Price:", font = "Courier 15 bold")
            pizza_price.grid(row = 5, column = 0, sticky = "NE", pady = 5)
            pizza_priceDisp = Label(sec, textvariable = pzprice, font = "Courier 15 bold italic")
            pizza_priceDisp.grid(row = 5, column = 1)

            topping = Label(sec, text = "Topping Type:", font = "Courier 15 bold")
            topping.grid(row = 6, column = 0, sticky = "NE", pady = 5)
            toppingDisp = Label(sec, textvariable = topname, font = "Courier 15 bold italic")
            toppingDisp.grid(row = 6, column = 1)

            topping_price = Label(sec, text = "Topping Price:", font = "Courier 15 bold")
            topping_price.grid(row = 7, column = 0, sticky = "NE", pady = 5)
            topping_priceDisp = Label(sec, textvariable = topprice, font = "Courier 15 bold italic")
            topping_priceDisp.grid(row = 7, column = 1)

            qty1 = Label(sec, text = "Quantity:", font = "Courier 15 bold")
            qty1.grid(row = 8, column = 0, sticky = "NE", pady = 5)
            qtyDisp = Label(sec, textvariable = quantity, font = "Courier 15 bold italic")
            qtyDisp.grid(row = 8, column = 1)

            gst = Label(sec, text = "GST @18%:", font = "Courier 15 bold")
            gst.grid(row = 9, column = 0, sticky = "NE")
            gstDisp = Label(sec, textvariable = pzgst, font = "Courier 15 bold italic")
            gstDisp.grid(row = 9, column = 1)

            tot = Label(sec, text = "Total:", font = "Courier 15 bold")
            tot.grid(row = 10, column = 0, sticky = "NE")
            totDisp = Label(sec, textvariable = pztotal, font = "Courier 15 bold italic")
            totDisp.grid(row = 10, column = 1)
    except Exception as e:
        messagebox.showerror("Invalid Entry",e)
#Design---------------------------------------------------------------------------------------
head = Label(screen, text = "Welcome to Domino's Pizza.", font = "courier 25 bold", background = "#4066a3", foreground = "white")
head.place(x = 400, y = 5)
head.config(font = "Chango 20 bold")
#Pizza Frame----------------------------------------------------------------------------------
pizzaFrame = Frame(screen, width = "850", height = "650", background = "#1f3f82")
pizzaFrame.place(x = 10, y = 45)

pizzaHead = Label(pizzaFrame,  text = "Choose Your Pizza!!", font = "courier 14 bold", background = "#1f3f82", foreground = "white")
pizzaHead.place(x = 300, y = 2)

pizzatype1 = Button(pizzaFrame, width = 400, height = 300, image = thin, compound = "top", background = "#d1dbeb", foreground = "white", command = lambda : choosePizza("Thin Crust",350))
pizzatype1.place(x = 10, y = 30)
pizza1lbl = Label(pizzaFrame, text = "Thin Crust Pizza      350Rs.", width = 35, font = "courier 12 bold", background = "#1f3f82", foreground = "white")
pizza1lbl.place(x = 30, y = 300)

pizzatype2 = Button(pizzaFrame, width = 400, height = 300, image = thick, background = "#d1dbeb", foreground = "white", command = lambda : choosePizza("Thick Crust",250))
pizzatype2.place(x = 430, y = 30)
pizza2lbl = Label(pizzaFrame, text = "Thick Crust Pizza     250Rs.", width = 35, font = "courier 12 bold", background = "#1f3f82", foreground = "white")
pizza2lbl.place(x = 450, y = 300)

pizzatype3 = Button(pizzaFrame, width = 400, height = 300, image = cheese, background = "#d1dbeb", foreground = "white", command = lambda : choosePizza("Cheese Burst",420))
pizzatype3.place(x = 10, y = 350)
pizza3lbl = Label(pizzaFrame, text = "Cheese Brust Pizza    420Rs.", width = 35, font = "courier 12 bold", background = "#1f3f82", foreground = "white")
pizza3lbl.place(x = 30, y = 600)

pizzatype4 = Button(pizzaFrame, width = 400, height = 300, image = pan, background = "#d1dbeb", foreground = "white", command = lambda : choosePizza("Pan Pizza",380))
pizzatype4.place(x = 430, y = 350)
pizza4lbl = Label(pizzaFrame, text = "Pan Pizza             380Rs.", width = 35, font = "courier 12 bold", background = "#1f3f82", foreground = "white")
pizza4lbl.place(x = 450, y = 600)

#Topping Frame--------------------------------------------------------------------------------
toppingFrame = Frame(screen, width = "400", height = "280", background = "#1f3f82")
toppingFrame.place(x = 880, y = 45)

toppingHead = Label(toppingFrame, text = "Choose Your Topping!!!", font = "courier 14 bold", background = "#1f3f82", foreground = "white")
toppingHead.place(x = 60, y = 2)

toppingtype1 = Button(toppingFrame, text = "Pepperoni        50Rs.", height = 1, width = 30, background = "#1f3f82", foreground = "white", font = "courier 15 bold", command = lambda : toppings("Pepperoni",50))
toppingtype1.place(x = 12, y = 40)

toppingtype2 = Button(toppingFrame, text = "Mushrooms        80Rs.", height = 1, width = 30, background = "#1f3f82", foreground = "white", font = "courier 15 bold", command = lambda : toppings("Mushrooms",80))
toppingtype2.place(x = 12, y = 85)

toppingtype3 = Button(toppingFrame, text = "Onions           70Rs.", height = 1, width = 30, background = "#1f3f82", foreground = "white", font = "courier 15 bold", command = lambda : toppings("Onions",70))
toppingtype3.place(x = 12, y = 130)

toppingtype4 = Button(toppingFrame, text = "Extra Cheese    120Rs.", height = 1, width = 30, background = "#1f3f82", foreground = "white", font = "courier 15 bold", command = lambda : toppings("Extra Cheese",120))
toppingtype4.place(x = 12, y = 175)

toppingtype5 = Button(toppingFrame, text = "Black Olives    100Rs.", height = 1, width = 30, background = "#1f3f82", foreground = "white", font = "courier 15 bold", command = lambda : toppings("Black Olives",100))
toppingtype5.place(x = 12, y = 220)

#Bill Frame-----------------------------------------------------------------------------------
billFrame = Frame(screen, width = 400, height = 364, background = "#de2828")
billFrame.place(x = 880, y = 330)

nameDisp = Label(billFrame, text = "Name", font ='courier 15 bold', background = "#de2828", foreground = "white")
nameDisp.place(x = 10, y = 20)

Name = Entry(billFrame, width = 15, font = "courier 14 bold", textvariable = name)
Name.place(x = 180, y = 20)

mobileDisp = Label(billFrame, text = "Mobile", font ='courier 15 bold', background = "#de2828", foreground = "white")
mobileDisp.place(x = 10, y = 55)

Mobile = Entry(billFrame, width = 15, font = "courier 14 bold", textvariable = mobile)
Mobile.place(x = 180, y = 55)

qtyDisp = Label(billFrame, text = "Quantity", font ='courier 15 bold', background = "#de2828", foreground = "white")
qtyDisp.place(x = 10, y = 88)

qtyMinusBtn = Button(billFrame, text = "-", width = 2, height = 1, font = "courier 10 bold", command = lambda : removeQty() ) 
qtyMinusBtn.place(x = 180, y = 88)
Qty = Entry(billFrame, width = 3, font = "courier 14 bold", textvariable = qty)
Qty.place(x = 220, y = 88)
Qty['state'] = DISABLED
qtyPlusBtn = Button(billFrame, text = "+", width = 2, height = 1, font = "courier 10 bold", command = lambda : addQty() ) 
qtyPlusBtn.place(x = 280, y = 88)

pizzaPriceDisp = Label(billFrame, text = "Pizza Price", font ='courier 15 bold', background = "#de2828", foreground = "white")
pizzaPriceDisp.place(x = 10, y = 120)
pizzaPrice = Label(billFrame, text = pizzaprice.get(), textvariable = pizzaprice, font ='courier 15 bold', background = "#de2828", foreground = "white")
pizzaPrice.place(x = 180, y = 120)

toppingPriceDisp = Label(billFrame, text = "Topping Price", font ='courier 15 bold', background = "#de2828", foreground = "white")
toppingPriceDisp.place(x = 10, y = 150)
toppingPrice = Label(billFrame, text = toppingprice.get(), textvariable = toppingprice, font ='courier 15 bold', background = "#de2828", foreground = "white")
toppingPrice.place(x = 180, y = 150)

gstDisp = Label(billFrame, text = "G.S.T 18%", font ='courier 15 bold', background = "#de2828", foreground = "white")
gstDisp.place(x = 10, y = 180)
gst = Label(billFrame, text = GST.get(), textvariable = GST, font ='courier 15 bold', background = "#de2828", foreground = "white")
gst.place(x = 180, y = 180)

totalDisp = Label(billFrame, text = "TOTAL", font ='Chango 22 bold', background = "#de2828", foreground = "white")
totalDisp.place(x = 10, y = 220)
total = Label(billFrame, text = TOTAL.get(), textvariable = TOTAL, font ='Courier 22 bold', background = "#de2828", foreground = "white")
total.place(x = 180, y = 222)

#Bill Payment Button--------------------------------------------------------------------------
payBill = Button(billFrame, text = "PAY BILL", width = "10", height = "1", font ='Courier 22 bold', background = "#1f3f82", foreground = "white", command = lambda : checkpay())
payBill.place(x = 80, y = 280)
#Mainloop-------------------------------------------------------------------------------------
screen.mainloop()