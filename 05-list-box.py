from tkinter import *


root = Tk()

root.title("GUI programming")
root.geometry("640x480+300+100") # 가로 * 세로 + 창의 x위치 + 창의 y위치

list_box = Listbox(root, selectmode = "extended", height = 0)
# selectmode를 single : 여러개 선택 불가능하고 하나만 선택 가능.
# height를 0으로 하면 리스트박스 안에 있는 것만큼 height 자동 지정.


list_box.insert(0, "첫번째")
list_box.insert(1, "두번째")
list_box.insert(2, "세번째")
list_box.insert(END, "네번째")
list_box.insert(END, "다섯번째") # END : 제일 마지막.

lbl = Label(root, text = "리스트박스에는 {}개가 들어있어요.".format(list_box.size()))
lbl.pack()

def cmd() :
    list_box.delete(END) # 제일 마지막 요소 삭제
    
    print(list_box.get(0, 2)) # 0, 1, 2 get한다.

    lbl.config(text = "리스트박스에는 {}개가 들어있어요.".format(list_box.size()))


list_box.pack()

btn = Button(root, text = "button", command = cmd)
btn.pack()




root.mainloop()  # 메인루프를 통해서 창이 닫히지 않도록 한다.