import tkinter.ttk as ttk
from tkinter import *
import time

# 프로그레스바는 진행 상태를 나타내준다.

root = Tk()
root.title("progress bar")
root.geometry("640x480+200+200")

progress_bar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate") # indeternimate : 그냥 진행중인 것만 알 수 있다. 진행도는 표시되지 않음.
progress_bar.start(10) # 10ms마다 움직임
progress_bar.pack()

progress_bar_2 = ttk.Progressbar(root, maximum = 100, mode = "determinate") # deternimate : 진행도 표시됨.
progress_bar_2.start(7) # 10ms마다 움직임
progress_bar_2.pack()


def btn_cmd() :
    progress_bar.stop()
    progress_bar_2.stop()
    


btn = Button(root, text = "중지", command = btn_cmd)
btn.pack()

root.mainloop()