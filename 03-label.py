from tkinter import *

# 레이블은 이미지나 글자를 띄우기 위한 공간. 기본적으로는 별도의 인터랙션은 제공하지 않는다.

root = Tk()
root.title("GUI programming")
root.geometry("500x500+300+300")

apple_image = PhotoImage(file = "apple.png")
question_image = PhotoImage(file = "question_mark.png")


label_1 = Label(root, text = "레이블 1")
label_1.pack()


label_2 = Label(root, image = question_image) # 레이블 위에 이미지 올릴 수도 있다.
label_2.pack()

label_3 = Label(root, text = "이것은..")
label_3.pack()



def change() :
    label_3.config(text = "사과입니다.")
    label_2.config(image = apple_image)
    # 주의 : 이미지를 이 함수의 지역변수로 지정하면, 이 함수가 끝나는 시점에 이미지가 날아간다.
    # 따라서 함수 내에서 이미지를 전역변수로 선언하거나, 전역에 있는 이미지를 쓰도록 한다.


btn_1 = Button(root, text = "이것은..?", command = change)
btn_1.pack()

root.mainloop()  # 메인루프를 통해서 창이 닫히지 않도록 한다.