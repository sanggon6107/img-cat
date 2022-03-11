import tkinter.ttk as ttk
from tkinter import *
import time

# 실제로 진행되는 프로그레스바를 만들어본다.

root = Tk()
root.title("progress bar")
root.geometry("640x480+200+200")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var)
progress_bar.pack()

lbl = Label(root, text = "시작을 누르세요.")
lbl.pack()

def btn_cmd() :
    for i in range(1, 101) : # [1,101)
        p_var.set(i) # variable의 값을 바꾼다.
        time.sleep(0.1)
        progress_bar.update() # 프로그레스바 업데이트
        lbl.config(text = p_var.get())



btn = Button(root, text = "시작", command = btn_cmd)
btn.pack()

root.mainloop()