import tkinter.ttk as ttk # 콤보박스는 ttk에 있다.
from tkinter import *

root = Tk()
root.title("combo-box")
root.geometry("640x480+200+200")

combo_values = [str(i) + "일" for i in range(1, 32)]
combo_box = ttk.Combobox(root, height = 5, values = combo_values, state = "readonly" ) # readonly : 콤보박스에 타이핑 못하도록 한다.
combo_box.pack()
#combo_box.current(0)
combo_box.set("카드 결제일")

def btn_cmd() :
    print(combo_box.get())

btn = Button(root, text = "선택", command = btn_cmd)
btn.pack()

root.mainloop()