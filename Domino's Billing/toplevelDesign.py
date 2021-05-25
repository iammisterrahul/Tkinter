from tkinter import *
import sqlite3
sec = Tk()
sec.geometry("500x500")
#Database-------------------------------------------------------------------------------------
con = sqlite3.connect("DomData.db")
cur = con.cursor()
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

qty = Label(sec, text = "Quantity:", font = "Courier 15 bold")
qty.grid(row = 8, column = 0, sticky = "NE", pady = 5)
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

sec.mainloop()