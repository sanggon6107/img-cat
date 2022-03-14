import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog # import * 이라도 __all__에 정의하지 않으면 한번에 모두 import 해주지 않는다.

root = Tk()

root.title("GUI programming")
root.geometry("640x510+300+100")
root.resizable(False, False)

# 파일 프레임(파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 10, pady = 10)

# 파일 추가 함수
def AddFile() :
    files = filedialog.askopenfilenames(title = "이미지 파일을 선택하세요", \
        filetypes = (("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir="C:/") # 파일 추가 클릭 시 최초 경로를 C드라이브로 설정
    
    # 사용자가 선택한 파일을 목록에 추가
    for file in files :
        list_file.insert(END, file)

# 파일 삭제 버튼
def DeleteFile() :
    for file in reversed(list_file.curselection()) :
        list_file.delete(file)

# 파일 추가 버튼
btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "Add file", command = AddFile)
btn_add_file.pack(side = "left")

# 파일 삭제 버튼
btn_delete_file = Button(file_frame,padx = 5, pady = 5, width = 12, text = "Delete file", command = DeleteFile)
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
path_frame.pack(fill = "x", padx = 10, ipady = 5, ipadx = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True, padx = 5, ipady = 4) # ipad : inner-pad

def BrowseDestpath() :
    pass

btn_dest_path = Button(path_frame, text = "찾아보기", width = 10, comman = BrowseDestPath)
btn_dest_path.pack(side = "right", padx = 5)

# 옵션 프레임
frame_option = LabelFrame(root, text = "option")
frame_option.pack(ipadx = 5, ipady = 5, fill = "x", padx = 10)

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


# 진행상황 프로그레스바

frame_progress = LabelFrame(root, text = "진행 상황")
frame_progress.pack(fill = "x", ipadx = 5, ipady = 5, padx = 10)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill = "x", padx = 10)

# 실행 프레임

frame_run = Frame(root)
frame_run.pack(fill = "x")

btn_quit = Button(frame_run, padx = 5, pady = 5, text = "끝내기", width = 12, command = root.quit)
btn_quit.pack(side = "right", padx = 10, pady = 5)

btn_start = Button(frame_run, padx = 5, pady = 5, text = "시작", width = 12)
btn_start.pack(side = "right", padx = 5, pady = 5)





root.mainloop()