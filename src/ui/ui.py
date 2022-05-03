from tkinter import ttk, Tk, StringVar
from tkinter import *
from calculator import Calculator

calculator = Calculator()
class UI:
    """Class that manages the UI of the program.   
    """
    def __init__(self, root):
        """Creates new calculator UI.
        """
        self._root = root
        self.input = None

    def start(self):
        """Starts the calculator UI window.
        """
        self.input = StringVar()
        self._label_var.set("0")

gui = Tk()
gui.geometry("450x400")
gui.title("Calculator")

expression = ""
input = StringVar()

def click(item):
    """Manages what happens after clicking a number or a symbol.

    Args:
        item: The button pressed     
    """
    global expression
    expression = expression + str(item)
    input.set(expression)

def equals():
    """Manages what happens after clicking the equals button.    
    """
    global expression
    result = str(calculator.calc_basic(expression))
    input.set(result)
    expression = result

def clear_field():
    """Manages what happens after clicking clear button   
    """
    global expression
    expression = ""
    input.set("")

text_frame = Frame(gui, width=320, height=50)
text_frame.pack(side=TOP)
text_field = Entry(text_frame, textvariable=input, width=50, justify=CENTER)
text_field.grid(row=0, column=0)
text_field.pack(ipady=15)
button_frame = Frame(gui, width=320, height=440)
button_frame.pack()

zero = Button(button_frame, text="0", width=10, height=3, bg = "white", command = lambda: click(0)).grid(row = 3, column = 1)
one = Button(button_frame, text="1", width=10, height=3, bg = "white", command = lambda: click(1)).grid(row = 2, column = 0)
two = Button(button_frame, text="2", width=10, height=3, bg = "white", command = lambda: click(2)).grid(row = 2, column = 1)
three = Button(button_frame, text="3", width=10, height=3, bg = "white", command = lambda: click(3)).grid(row = 2, column = 2)
four = Button(button_frame, text="4", width=10, height=3, bg = "white", command = lambda: click(4)).grid(row = 1, column = 0)
five = Button(button_frame, text="5", width=10, height=3, bg = "white", command = lambda: click(5)).grid(row = 1, column = 1)
six = Button(button_frame, text="6", width=10, height=3, bg = "white", command = lambda: click(6)).grid(row = 1, column = 2)
seven = Button(button_frame, text="7", width=10, height=3, bg = "white", command = lambda: click(7)).grid(row = 0, column = 0)
eight = Button(button_frame, text="8", width=10, height=3, bg = "white", command = lambda: click(8)).grid(row = 0, column = 1)
nine = Button(button_frame, text="9", width=10, height=3, bg = "white", command = lambda: click(9)).grid(row = 0, column = 2)
add = Button(button_frame, text="+", width=10, height=3, bg = "white", command = lambda: click("+")).grid(row = 0, column = 3)
subtract = Button(button_frame, text="-", width=10, height=3, bg = "white", command = lambda: click("-")).grid(row = 1, column = 3)
multiply = Button(button_frame, text="*", width=10, height=3, bg = "white", command = lambda: click("*")).grid(row = 2, column = 3)
divide = Button(button_frame, text="/", width=10, height=3, bg = "white", command = lambda: click("/")).grid(row = 3, column = 3)
equal = Button(button_frame, text="=", width=10, height=3, bg = "white", command = lambda: equals()).grid(row = 3, column = 2)
point = Button(button_frame, text=".", width=10, height=3, bg = "white", command = lambda: click(".")).grid(row = 3, column = 0)
clear = Button(button_frame, text="C", width=10, height=3, bg = "white", command = lambda: clear_field()).grid(row = 4, column = 0)

gui.mainloop()
