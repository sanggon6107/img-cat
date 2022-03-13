from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480+200+200")

# 메뉴
menu_base = Menu(root)

# 파일 Open, Save 함수

def Open() :
    pass

def Save() :
    pass



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