from tkinter import *

# 계산기 만들기

root = Tk()
root.title("grid")
root.geometry("640x480+200+200")

btn_f16 = Button(root, text = "F16")
btn_f17 = Button(root, text = "F17")
btn_f18 = Button(root, text = "F18")
btn_f19 = Button(root, text = "F19")

btn_f16.grid(row = 0, column = 0)
btn_f17.grid(row = 0, column = 1)
btn_f18.grid(row = 0, column = 2)
btn_f19.grid(row = 0, column = 3)

btn_clear = Button(root, text = "clear")
btn_eql = Button(root, text = "=")
btn_slsh = Button(root, text = "/")
btn_aest = Button(root, text = "*")

btn_clear.grid(row = 1, column = 0)
btn_eql.grid(row = 1, column = 1)
btn_slsh.grid(row = 1, column = 2)
btn_aest.grid(row = 1, column = 3)

# 7 ~ 9

btn_7 = Button(root, text = "7")
btn_8 = Button(root, text = "8")
btn_9 = Button(root, text = "9")
btn_min = Button(root, text = "-")

btn_7.grid(row = 2, column = 0)
btn_8.grid(row = 2, column = 1)
btn_9.grid(row = 2, column = 2)
btn_min.grid(row = 2, column = 3)



# 4 ~ 6



btn_4 = Button(root, text = "4")
btn_5 = Button(root, text = "5")
btn_6 = Button(root, text = "6")
btn_plus = Button(root, text = "+")

btn_4.grid(row = 3, column = 0)
btn_5.grid(row = 3, column = 1)
btn_6.grid(row = 3, column = 2)
btn_plus.grid(row = 3, column = 3)



# 1 ~ 3

btn_1 = Button(root, text = "1")
btn_2 = Button(root, text = "2")
btn_3 = Button(root, text = "3")
btn_enter = Button(root, text = "enter")

btn_1.grid(row = 4, column = 0)
btn_2.grid(row = 4, column = 1)
btn_3.grid(row = 4, column = 2)
btn_enter.grid(row = 4, column = 3, rowspan = 2)  # 엔터는 아래로 길쭉하다.


# 0

btn_0 = Button(root, text = "0")
btn_dot = Button(root, text = ".")

btn_0.grid(row = 5, column = 0, columnspan = 2) # 0은 옆으로 길쭉하다.
btn_dot.grid(row = 5, column = 2)




root.mainloop()