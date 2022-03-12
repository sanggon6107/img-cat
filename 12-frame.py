from tkinter import *

root = Tk()
root.title("frame")
root.geometry("640x480+200+200")

Label(root, text = "메뉴를 선택해 주세요").pack(side = "top")

Button(root, text = "주문하기").pack(side = "bottom")


frame_burger = Frame(root, relief = "solid", bd = 1) # relief : 외곽선.
frame_burger.pack(side = "left", fill = "both", expand = True) # fill : 위아래 채움. expand : 좌우 채움 

Button(frame_burger, text = "햄버거").pack()
Button(frame_burger, text = "치즈버거").pack()
Button(frame_burger, text = "치킨버거").pack()


frame_drink = LabelFrame(root, text = "음료", padx = 10, pady = 10)
frame_drink.pack(side = "right")
Button(frame_drink, text = "콜라").pack()
Button(frame_drink, text = "제로콜라").pack()
Button(frame_drink, text = "사이다").pack()


root.mainloop()