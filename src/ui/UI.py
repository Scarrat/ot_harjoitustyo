from tkinter import scrolledtext, ttk, StringVar, constants
from tkinter import *

from numpy import empty
from calculator import Calculator
from services.history_service import history_service
from note import Note
from datetime import datetime


calculator = Calculator()
class UI:
    """Class that manages the UI of the program.   
    """
    def __init__(self,root):
        """Creates new calculator UI.

        Args: 
            root: the default window.
        """
        self._root = root
        self.input = None
        self.expression = ""
        self.input = StringVar()
        self.last_exp = ""
        self.notes = []
        self.num1 = ""
        self.num2 = ""
        self.operand = ""

    def start(self):
        """Starts the calculator UI window.
        """
        self.initialize()

    def click_num(self,item):
        """Manages what happens after clicking a number.

        Args:
            item: The button pressed     
        """
        self.expression = self.expression + str(item)
        self.input.set(self.expression)

        if self.operand:
            self.num2 = self.num2 + str(item)
        else:
            self.num1 = self.num1 + str(item)

    def click_oper(self,item):
        """Manages what happens after clicking a symbol.

        Args:
            item: The button pressed     
        """
        self.expression = self.expression + str(item)
        self.input.set(self.expression)

        if self.operand:
            self.num2 = self.num2 + str(item)
        if self.num1 == "":
            self.num1 = self.num1 + str(item)
        else:
            self.operand = item

    

    def equals(self):
        """Manages what happens after self.clicking the equals button.    
        """
        if not self.operand or not self.num1 or not self.num2:
            self.input.set("Please use correct form for expressions")
        else:   
            result = str(calculator.calc_test(self.num1, self.operand,self.num2))
            self.last_exp = self.expression + "=" + str(result)
            self.input.set(result)
            self.expression = result
            self.num1 = result
            self.num2 = ""
            self.operand = ""

        

    def clear_field(self):
        """Clears the entry field. 
        """
        self.expression = ""
        self.input.set("")
        self.num1 = ""
        self.num2 = ""
        self.operand = ""


    def show_notes(self,txt):
        """Loads the history list from database.

            Args:
                txt: Textbox where history is displayed.
        """
        notelist = history_service.get_notes()
        for note in notelist:
            self.notes.append(note)
        for note in self.notes:
            txt.insert(constants.INSERT, note.time + " | " + note.expression + "\n")

    def save_note(self,txt):
        """Saves an history entry into textbox and database.

            Args:
                txt: Textbox where history is displayed.
        """
        if self.last_exp:
            temp_note = Note(self.last_exp, datetime.now().strftime("%d/%m %H:%M"))
            history_service.save_note(temp_note)
            txt.insert(constants.INSERT, temp_note.time + " | " + temp_note.expression + "\n")

    def clear_history(self):
        """Clears history from database."""
        history_service.delete_all()

    def initialize(self):
        """Initializes the window of the calculator."""
        text_frame = ttk.Frame(master= self._root, width=320, height=50)
        text_frame.pack(side=TOP)
        text_field = Entry(text_frame, textvariable=self.input, width=50, justify=CENTER)
        text_field.grid(row=0, column=0)
        text_field.pack(ipady=15)
        button_frame = Frame(master= self._root, width=320, height=440)
        button_frame.pack()
        note_frame = Frame(master= self._root, width=100, height=100)
        note_frame.pack(side=RIGHT)
        txt = scrolledtext.ScrolledText(note_frame,width=55,height=10)
        txt.grid(row=0,column=0)
        self.show_notes(txt)
    
        zero = Button(button_frame, text="0", width=10, height=3, bg = "white", command = lambda: self.click_num(0)).grid(row = 3, column = 1)
        one = Button(button_frame, text="1", width=10, height=3, bg = "white", command = lambda: self.click_num(1)).grid(row = 2, column = 0)
        two = Button(button_frame, text="2", width=10, height=3, bg = "white", command = lambda: self.click_num(2)).grid(row = 2, column = 1)
        three = Button(button_frame, text="3", width=10, height=3, bg = "white", command = lambda: self.click_num(3)).grid(row = 2, column = 2)
        four = Button(button_frame, text="4", width=10, height=3, bg = "white", command = lambda: self.click_num(4)).grid(row = 1, column = 0)
        five = Button(button_frame, text="5", width=10, height=3, bg = "white", command = lambda: self.click_num(5)).grid(row = 1, column = 1)
        six = Button(button_frame, text="6", width=10, height=3, bg = "white", command = lambda: self.click_num(6)).grid(row = 1, column = 2)
        seven = Button(button_frame, text="7", width=10, height=3, bg = "white", command = lambda: self.click_num(7)).grid(row = 0, column = 0)
        eight = Button(button_frame, text="8", width=10, height=3, bg = "white", command = lambda: self.click_num(8)).grid(row = 0, column = 1)
        nine = Button(button_frame, text="9", width=10, height=3, bg = "white", command = lambda: self.click_num(9)).grid(row = 0, column = 2)
        add = Button(button_frame, text="+", width=10, height=3, bg = "white", command = lambda: self.click_oper("+")).grid(row = 0, column = 3)
        subtract = Button(button_frame, text="-", width=10, height=3, bg = "white", command = lambda: self.click_oper("-")).grid(row = 1, column = 3)
        multiply = Button(button_frame, text="*", width=10, height=3, bg = "white", command = lambda: self.click_oper("*")).grid(row = 2, column = 3)
        divide = Button(button_frame, text="/", width=10, height=3, bg = "white", command = lambda: self.click_oper("/")).grid(row = 3, column = 3)
        equal = Button(button_frame, text="=", width=10, height=3, bg = "white", command = lambda: self.equals()).grid(row = 3, column = 2)
        point = Button(button_frame, text=".", width=10, height=3, bg = "white", command = lambda: self.click_num(".")).grid(row = 3, column = 0)
        clear = Button(button_frame, text="C", width=10, height=3, bg = "white", command = lambda: self.clear_field()).grid(row = 4, column = 0)
        note_button = Button(button_frame, text="S", width=10, height=3, bg = "white", command = lambda: self.save_note(txt)).grid(row = 4, column = 1)
        clearn_note_button = Button(button_frame, text="CH", width=10, height=3, bg = "white", command = lambda: self.clear_history()).grid(row = 4, column = 2)

        
        


