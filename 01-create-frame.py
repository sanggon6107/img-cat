from tkinter import *

root = Tk()

root.title("GUI programming")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+100") # 가로 * 세로 + 창의 x위치 + 창의 y위치

root.resizable(False, False) # 너비, 높이 변경 불가하도록 설정.

root.mainloop()  # 메인루프를 통해서 창이 닫히지 않도록 한다.