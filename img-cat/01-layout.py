import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("GUI programming")
root.geometry("640x480+300+100")
root.resizable(False, False)

# 파일 프레임(파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill = "x")

btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "Add file")
btn_add_file.pack(side = "left")


btn_delete_file = Button(file_frame,padx = 5, pady = 5, width = 12, text = "Delete file")
btn_delete_file.pack(side = "right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill = "both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill = "y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand=scrollbar.set)
list_file.pack(side = "left", fill = "both", expand = True)
scrollbar.config(command = list_file.yview)

#저장경로 프레임
path_frame = LabelFrame(root, text = "저장경로")
path_frame.pack(fill = "x")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True, padx = 5, ipady = 4) # ipad : inner-pad

btn_dest_path = Button(path_frame, text = "찾아보기", width = 10)
btn_dest_path.pack(side = "right")

# 옵션 프레임
frame_option = LabelFrame(root, text = "option")
frame_option.pack(ipadx = 5, ipady = 5)

# 옵션1 -가로 넓이 옵션
## 가로 넓이 레이블

lbl_width = Label(frame_option, text = "가로 넓이", width = 8)
lbl_width.pack(side = "left")

## 가로 넓이콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 10)
cmb_width.current(0) # 디폴트는 원본 유지
cmb_width.pack(side = "left")

# 옵션2 - 간격 옵션

## 간격 옵션 레이블
lbl_space = Label(frame_option, text = "간격", width = 8)
lbl_space.pack(side = "left")

## 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state = "readonly", values = opt_space, width = 10)
cmb_space.current(0) # 디폴트는 없음
cmb_space.pack(side = "left")



# 옵션3 - 파일 포맷 옵션

## 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text = "파일 포맷", width = 10)
lbl_format.pack(side = "left")
## 파일 포맷 옵션 콤보

opt_format = ["jpg", "png", "bmp"]
cmb_format = ttk.Combobox(frame_option, state = "readonly", values = opt_format, width = 10)
cmb_format.current(0) # 디폴트는 jpg
cmb_format.pack(side = "left")




root.mainloop()