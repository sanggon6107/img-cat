from tkinter import *

# 한줄만 입력받고싶을 때는 Entry, (처리가 간단하고 엔터를 입력할 수 없다.)
# 여러줄 입력받고싶을 때는 Text.

root = Tk()

root.title("text-entry")
root.geometry("640x480+300+100") # 가로 * 세로 + 창의 x위치 + 창의 y위치

txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # 첫 번째 요소인 index에는 END를 쓴다.

ent = Entry(root, width = 30)
ent.pack()
ent.insert(0, "한 줄만 입력하세요") # 첫 번째 요소인 index에는 0을 입력한다.

def enter() :
    # 입력 사항 로깅
    print(txt.get("1.0", END))  # "1.0", END의 의미 : 첫 번째 줄의, 인덱스0(첫글자) 글자부터. END까지 전부 get해라.
    print(ent.get())

    # 입력 내용 삭제
    txt.delete("1.0", END)
    ent.delete(0, END)

btn_1 = Button(root, text =  "입력 완료", command = enter)
btn_1.pack()


root.mainloop()  # 메인루프를 통해서 창이 닫히지 않도록 한다.