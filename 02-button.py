from tkinter import *

# 위젯이란, 버튼, 텍스트박스 등등 윈도우 GUI위에 올릴 수 있는 특정 기능을 의미함.
# 아래는 버튼 위젯.

root = Tk()
root.title("GUI programming")
root.geometry("500x1000+300+300")


btn_1 = Button(root, text = "버튼1") # 버튼 객체를 생성하는 것만으로 버튼이 창에 생기지 않는다.
btn_1.pack()                         # pack()을 해야 비로소 버튼이 창에 생긴다.

btn_2 = Button(root, padx = 5, pady = 10, text = "버튼2222222222222") # pad는 여백이다.
btn_2.pack()


btn_3 = Button(root, padx = 10, pady = 5, text = "버튼3")
btn_3.pack()

btn_4 = Button(root, width = 10, height = 3, text = "버튼44444444444") # width는 고정 크기이다.
btn_4.pack()


btn_5 = Button(root, fg = "red", bg = "yellow", text = "버튼5") #  버튼에 색 넣기. foreground, background
btn_5.pack()

button_image = PhotoImage(file = "button.png") # 이미지 파일을 인스턴스화.
btn_6 = Button(root, image = button_image)     # 이미지를 버튼으로 쓴다.
btn_6.pack()

def btncmd() :
    return print("동작")

btn_7 = Button(root, text = "누르면 동작", command = btncmd)
btn_7.pack()



root.mainloop()  # 메인루프를 통해서 창이 닫히지 않도록 한다.