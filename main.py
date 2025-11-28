from tkinter import Tk

if  "__main__" == __name__ :
    master_screen = Tk()
    master_screen.geometry("800x900")
    master_screen.title("Calculator")
    master_screen.resizable(False, False)
    master_screen.configure(bg="black")
    master_screen.mainloop()
