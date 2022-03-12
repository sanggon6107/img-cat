from tkinter import *

root = Tk()
root.title("scroll bar")
root.geometry("640x480")

frame = LabelFrame(root, text = "프레임", padx = 10, pady = 10)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y")


listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set) # set을 하지 않으면 정상 동작 하지 않는다.
for i in range(1, 32) :
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")

scrollbar.config(command = listbox.yview) # listbox가 scrollbar를 보고 있듯, scrollbar도 listbox 보고있어야 한다.