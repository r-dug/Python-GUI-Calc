from tkinter import *

root = Tk()
root.title("Calculator.... I'm learning GUIS, gimme a break")

e = Entry(root, width= 35, borderwidth= 5)
e.grid(row=0, column=0, columnspan=4)

first_num = 0
opperator = ''

def button_num(number):
    e.insert('end', number)


def button_add():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    global opperator
    opperator = "add"

def button_subract():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    global opperator
    opperator = "subtract"

def button_multiply():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    global opperator
    opperator = "multiply"

def button_divide():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    global opperator
    opperator = "divide"

def button_square():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    e.insert(0, first_num ** 2)
    global opperator
    opperator = ""

def button_square_root():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    e.insert(0, first_num ** .5)
    global opperator
    opperator = ""

def button_power_of():
    global first_num
    first_num = float(e.get())
    e.delete(0, 'end')
    global opperator
    opperator = "power_of"

def button_equals():
    curr_num = float(e.get())
    e.delete(0, 'end')
    if opperator=='add':
        e.insert(0, first_num + curr_num)
    if opperator=='subtract':
        e.insert(0, first_num - curr_num)
    if opperator=='multiply':
        e.insert(0, first_num * curr_num)
    if opperator=='divide':
        e.insert(0, first_num / curr_num)
    if opperator=='power_of':
        e.insert(0, first_num ** curr_num)
    if opperator=='':
        e.insert(0, "you forgot an opperator, bitch!")


def button_clear():
    e.delete(0, 'end')

b_1 = Button(root, text='1', padx =40, pady=20, command= lambda:button_num(1))
b_2 = Button(root, text='2', padx =40, pady=20, command= lambda:button_num(2))
b_3 = Button(root, text='3', padx =40, pady=20, command= lambda:button_num(3))
b_4 = Button(root, text='4', padx =40, pady=20, command= lambda:button_num(4))
b_5 = Button(root, text='5', padx =40, pady=20, command= lambda:button_num(5))
b_6 = Button(root, text='6', padx =40, pady=20, command= lambda:button_num(6))
b_7 = Button(root, text='7', padx =40, pady=20, command= lambda:button_num(7))
b_8 = Button(root, text='8', padx =40, pady=20, command= lambda:button_num(8))
b_9 = Button(root, text='9', padx =40, pady=20, command= lambda:button_num(9))
b_0 = Button(root, text='0', padx =40, pady=20, command= lambda:button_num(0))

b_clear = Button(root, text='clr', padx =120, pady=20, command= button_clear)
b_equals = Button(root, text='=', padx =80, pady=20, command= button_equals)

b_add = Button(root, text='+', padx =20, pady=20, command=button_add)
b_subtract = Button(root, text='-', padx =20, pady=20, command=button_subract)
b_divide = Button(root, text='/', padx =20, pady=20, command=button_divide)
b_square = Button(root, text='^2', padx =20, pady=20, command=button_square)
b_square_root = Button(root, text='sqrt', padx =20, pady=20, command=button_square_root)
b_power_of = Button(root, text='^x', padx =20, pady=20, command=button_power_of)


b_1.grid(row= 3, column= 0)
b_2.grid(row= 3, column= 1)
b_3.grid(row= 3, column= 2)

b_4.grid(row= 2, column= 0)
b_5.grid(row= 2, column= 1)
b_6.grid(row= 2, column= 2)

b_7.grid(row= 1, column= 0)
b_8.grid(row= 1, column= 1)
b_9.grid(row= 1, column= 2)

b_0.grid(row= 4, column= 0)

b_clear.grid(row= 5, column = 0, columnspan = 3)

b_equals.grid(row= 4, column= 1, columnspan = 2)

b_add.grid(row= 1, column= 3)
b_subtract.grid(row= 2, column= 3)
b_divide.grid(row= 3, column= 3)
b_square.grid(row= 4, column= 3)
b_square_root.grid(row= 5, column= 3)
b_power_of.grid(row= 1, column= 4)

root.mainloop()
