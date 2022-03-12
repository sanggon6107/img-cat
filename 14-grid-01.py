from tkinter import *


root = Tk()
root.title("grid")
root.geometry("640x480+200+200")

btn_1 = Button(text = "button1")
btn_2 = Button(text = "button2")

btn_1.grid(row = 0, column = 0)
btn_2.grid(row = 1, column = 1)

root.mainloop()