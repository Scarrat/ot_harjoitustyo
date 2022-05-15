from ui.UI import UI
from tkinter import Tk, ttk

def main():
    window = Tk()
    window.title("Calculator")
    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ =='__main__':
    main()
