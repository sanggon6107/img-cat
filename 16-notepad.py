import os
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480+200+200")

# 메뉴
menu_base = Menu(root)

# 파일 Open, Save 함수

filename = "notepad.txt"

def Open() :
    if os.path.isfile(filename) :
        with open(filename, "r", encoding = "utf8") as file :
            text.delete("1.0", END)  # 현재 텍스트 쓰인부분 삭제
            text.insert(END, file.read()) # 메모장에 파일의 내용을 작성

def Save() :
    with open(filename, "w", encoding = "utf8") as file :
        file.write(text.get("1.0", END)) # 파일의 모든 내용을 저장



#파일
menu_file = Menu(menu_base, tearoff = 0)
menu_file.add_command(label = "열기", command = Open)
menu_file.add_command(label = "저장", command = Save)
menu_file.add_separator()
menu_file.add_command(label = "끝내기", command = root.quit)

menu_base.add_cascade(label = "파일", menu = menu_file)

# 편집
menu_edit = Menu(menu_base, tearoff = 0)
menu_base.add_cascade(label = "편집", menu = menu_edit)


# 서식
menu_form = Menu(menu_base, tearoff = 0)
menu_base.add_cascade(label = "서식", menu = menu_form)

# 보기
menu_view = Menu(menu_base, tearoff = 0)
menu_base.add_cascade(label = "보기", menu = menu_view)

# 도움말
menu_help = Menu(menu_base, tearoff = 0)
menu_base.add_cascade(label = "도움말", menu = menu_help)

root.config(menu = menu_base)


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")


# 텍스트 입력기
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side = "left", fill = "both", expand = True)

scrollbar.config(command = text.yview)



root.mainloop()