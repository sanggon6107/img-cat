from tkinter import *

root = Tk()
root.title("title")
root.geometry("640x480+200+200")

lbl_1 = Label(root, text = "메뉴를 고르세요")
lbl_1.pack()

bgr_var = IntVar()
burger_1 = Radiobutton(root, text = "치즈버거", value = 1, variable = bgr_var)
burger_1.select() # 기본값으로 지정
burger_2 = Radiobutton(root, text = "콰트로치즈버거", value = 2, variable = bgr_var)
burger_3 = Radiobutton(root, text = "치킨버거", value = 3, variable = bgr_var)
burger_1.pack()
burger_2.pack()
burger_3.pack()

Label(root, text = "드링크를 선택하세요.").pack()

drk_var = StringVar()
drink_1 = Radiobutton(root, text = "콜라", value = "콜라", variable = drk_var)
drink_1.select() # 기본값으로 지정
drink_2 = Radiobutton(root, text = "제로콜라", value = "제로콜라", variable = drk_var)
drink_3 = Radiobutton(root, text = "사이다", value = "사이다", variable = drk_var)
drink_1.pack()
drink_2.pack()
drink_3.pack()


def btn_cmd() :
    print(bgr_var.get()) # 선택된 값을 출력.
    print(drk_var.get())

btn_1 = Button(root, text = "선택", command = btn_cmd)
btn_1.pack()

root.mainloop()