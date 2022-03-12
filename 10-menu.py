from tkinter import *

# 툴바 만들기


root = Tk()
root.title("menu")
root.geometry("640x480+200+200")

def create_new_file() :
    print("새 파일을 만듭니다.")


menu_tk = Menu(root)


# File메뉴.
menu_file = Menu(menu_tk, tearoff = 0)
menu_file.add_command(label = "New file", command = create_new_file)
menu_file.add_command(label = "New window")
menu_file.add_separator()
menu_file.add_command(label = "Open File...")
menu_file.add_separator()
menu_file.add_command(label = "Save All", state = "disable")
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.quit)

menu_tk.add_cascade(label = "File", menu = menu_file)    # 완성된 menu_file을 최상위 메뉴인 menu_tk에 추가한다.

# Edit 메뉴 추가. Edit는 비어있다. 
menu_tk.add_cascade(label = "Edit")


# Language 메뉴 추가(radio button 통해서 하나만 선택하도록)

menu_lang = Menu(menu_tk, tearoff = 0)
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "JAVA")
menu_lang.add_radiobutton(label = "C++")

menu_tk.add_cascade(label = "Language", menu = menu_lang)


# View 메뉴 추가(체크박스를 통해서 체크/체크해제 할 수 있다)

menu_view = Menu(menu_tk, tearoff = 0)
menu_view.add_checkbutton(label = "Show minimap")
menu_view.add_checkbutton(label = "Open view")
menu_tk.add_cascade(label = "View", menu = menu_view)


root.config(menu = menu_tk)


root.mainloop()