from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry("400x350")
e = Entry(root, width=45,bg='LavenderBlush2')#, borderwidth=4)
e.grid(row=0, ipady=20, column=0, columnspan=4, padx = 10, pady=10)

# Defining keys function
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def clear(): 
    e.delete(0,END)

def equal():
    second_number = e.get()
    e.delete(0,END)
    if math== "addition":
        e.insert(0,f_num + int(second_number) )
    if math== "subtraction":
        e.insert(0,f_num - int(second_number) )
    if math== "multiplication":
        e.insert(0,f_num * int(second_number) )
    if math== "division":
        e.insert(0,f_num / int(second_number) )

def add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

button_1 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='1', padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='2', padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='3', padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='4', padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='5', padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='6', padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='7', padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='8', padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='9', padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, bg='RosyBrown1', activebackground='IndianRed1', text='0', padx=40, pady=20, command= lambda: button_click(0))
button_equal = Button(root, bg='khaki',activebackground='dark khaki', text='=', padx=40, pady=20, command= equal)
button_clear = Button(root,bg='SkyBlue1', activebackground='DeepSkyBlue2', text='Clear', padx=30, pady=20, command=clear )
button_add = Button(root, bg='pale turquoise', activebackground='turquoise', text='+', padx=40, pady=20, command= add)
button_sub = Button(root, bg='pale turquoise', activebackground='turquoise', text='-', padx=40, pady=20, command= subtract)
button_mul = Button(root, bg='pale turquoise', activebackground='turquoise', text='X', padx=40, pady=20, command= multiply)
button_div = Button(root, bg='pale turquoise', activebackground='turquoise', text='/', padx=40, pady=20, command= divide)

#put button on screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_equal.grid(row=4,column=1)
button_mul.grid(row=4, column=2)
button_div.grid(row=4, column=3)

root.mainloop()
