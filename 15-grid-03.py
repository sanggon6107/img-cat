from tkinter import *

# 계산기 만들기 2 - 버튼 크기 등 조절

root = Tk()
root.title("grid")
root.geometry("640x480+200+200")

# 첫째줄

btn_f16 = Button(root, text = "F16",width = 5, height = 2)
btn_f17 = Button(root, text = "F17",width = 5, height = 2)
btn_f18 = Button(root, text = "F18",width = 5, height = 2)
btn_f19 = Button(root, text = "F19",width = 5, height = 2)

# sticky : 동, 서, 남, 북에 있는 다른 그리드(혹은 창의 끝)에 붙을 때까지 확장한다.
btn_f16.grid(row = 0, column = 0, sticky = W + E + S + N, padx =3, pady = 3)
btn_f17.grid(row = 0, column = 1, sticky = W + E + S + N, padx =3, pady = 3)
btn_f18.grid(row = 0, column = 2, sticky = W + E + S + N, padx =3, pady = 3)
btn_f19.grid(row = 0, column = 3, sticky = W + E + S + N, padx =3, pady = 3)

# 둘째줄

btn_clear = Button(root, text = "clear",width = 5, height = 2)
btn_eql = Button(root, text = "=",width = 5, height = 2)
btn_slsh = Button(root, text = "/",width = 5, height = 2)
btn_aest = Button(root, text = "*",width = 5, height = 2)

btn_clear.grid(row = 1, column = 0, sticky = W + E + S + N, padx = 3, pady = 3)
btn_eql.grid(row = 1, column = 1, sticky = W + E + S + N, padx = 3, pady = 3)
btn_slsh.grid(row = 1, column = 2, sticky = W + E + S + N, padx = 3, pady = 3)
btn_aest.grid(row = 1, column = 3, sticky = W + E + S + N, padx = 3, pady = 3)

# 7 ~ 9

btn_7 = Button(root, text = "7",width = 5, height = 2)
btn_8 = Button(root, text = "8",width = 5, height = 2)
btn_9 = Button(root, text = "9",width = 5, height = 2)
btn_min = Button(root, text = "-",width = 5, height = 2)

btn_7.grid(row = 2, column = 0, sticky = W + E + S + N, padx = 3, pady = 3)
btn_8.grid(row = 2, column = 1, sticky = W + E + S + N, padx = 3, pady = 3)
btn_9.grid(row = 2, column = 2, sticky = W + E + S + N, padx = 3, pady = 3)
btn_min.grid(row = 2, column = 3, sticky = W + E + S + N, padx = 3, pady = 3)

# 4 ~ 6

btn_4 = Button(root, text = "4",width = 5, height = 2)
btn_5 = Button(root, text = "5",width = 5, height = 2)
btn_6 = Button(root, text = "6",width = 5, height = 2)
btn_plus = Button(root, text = "+",width = 5, height = 2)

btn_4.grid(row = 3, column = 0, sticky = W + E + S + N, padx = 3, pady = 3)
btn_5.grid(row = 3, column = 1, sticky = W + E + S + N, padx = 3, pady = 3)
btn_6.grid(row = 3, column = 2, sticky = W + E + S + N, padx = 3, pady = 3)
btn_plus.grid(row = 3, column = 3, sticky = W + E + S + N, padx = 3, pady = 3)


# 1 ~ 3

btn_1 = Button(root, text = "1",width = 5, height = 2)
btn_2 = Button(root, text = "2",width = 5, height = 2)
btn_3 = Button(root, text = "3",width = 5, height = 2)
btn_enter = Button(root, text = "enter",width = 5, height = 2)

btn_1.grid(row = 4, column = 0, sticky = W + E + S + N, padx = 3, pady = 3)
btn_2.grid(row = 4, column = 1, sticky = W + E + S + N, padx = 3, pady = 3)
btn_3.grid(row = 4, column = 2, sticky = W + E + S + N, padx = 3, pady = 3)
btn_enter.grid(row = 4, column = 3, rowspan = 2, sticky = W + E + S + N, padx = 3, pady = 3)  # 엔터는 아래로 길쭉하다.

# 0

btn_0 = Button(root, text = "0",width = 5, height = 2)
btn_dot = Button(root, text = ".",width = 5, height = 2)

btn_0.grid(row = 5, column = 0, columnspan = 2, sticky = W + E + S + N, padx = 3, pady = 3) # 0은 옆으로 길쭉하다.
btn_dot.grid(row = 5, column = 2, sticky = W + E + S + N, padx = 3, pady = 3)



root.mainloop()