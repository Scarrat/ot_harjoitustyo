from tkinter import Tk
from ui.UI import UI


def main():
    window = Tk()
    window.title("Calculator")
    interface = UI(window)
    interface.start()

    window.mainloop()

if __name__ =='__main__':
    main()
