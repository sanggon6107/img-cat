import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # import * 이라도 __all__에 정의하지 않으면 한번에 모두 import 해주지 않는다.
from PIL import Image

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

# 저장 경로 설정 함수(폴더 선택)
def BrowseDestPath() :
    dir = filedialog.askdirectory()
    if dir == "" :
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, dir)

btn_dest_path = Button(path_frame, text = "찾아보기", width = 10, command = BrowseDestPath)
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

# 이미지 통합 함수
def MergeImage() :
    try :
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width == "원본유지" :
            img_width = -1 # -1일때는 원본 기준으로 이미지 통합.
        else :
            img_width = int(img_width)
            
        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게" :
            img_space = 30
        elif img_space == "보통" :
            img_space = 60
        elif img_space == "넓게" :
            img_space = 90
        else : # "없음" 선택
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # 확장자명 받아옴.


        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리한다.
        
        image_sizes = [] # [(넓이, 높이), (넓이, 높이) ...]
        if img_width > -1 :
            image_sizes = [(int(img_width), int(img_width * x.size[1]/x.size[0])) for x in images]
        else : # 이미지 원본 사이즈 사용할 경우
            image_sizes = [(x.size[0], x.size[0]) for x in images]



        width_list, height_list = zip(*(image_sizes)) # x의 멤버 size는 그 요소가 순서대로 width, height이다.

        max_width, total_height = max(width_list), sum(height_list) # 이미지를 합치기 위해, 전체 y값과 넓이 중 최대값을 구한다.
        
        total_height += (img_space * (len(images) - 1)) # 이미지 사이 공백만큼 total height 증가. 

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 통합 이미지 그리기 위한 스케치북
        y_offset = 0 # y 위치 오프셋

        for idx, img in enumerate(images) :

            if img_width > -1 :
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100 # 프로그레스바 연동을 위한 정보 계산.
            p_var.set(progress)
            progress_bar.update() # 프로그레스바 업데이트


        dest_path = os.path.join(txt_dest_path.get(), "result.{}".format(img_format))
        result_img.save(dest_path)
        msgbox.showinfo("Info", "Done")
    except Exception as err :
        msgbox.showerror("에러", err)


# 실행 함수

def Start() :
    # 각 옵션 값을 확인
    width = cmb_width.get()
    space = cmb_space.get()
    format = cmb_format.get()

    if list_file.size() == 0 :
        msgbox.showwarning("경고", "이미지 파일을 추가하세요.")
        return
    if len(txt_dest_path.get()) == 0 : 
        msgbox.showwarning("경고", "경로를 지정하세요.")
        return
    
    # 이미지 통합 작업
    MergeImage()

# 실행 버튼
btn_start = Button(frame_run, padx = 5, pady = 5, text = "시작", width = 12, command = Start)
btn_start.pack(side = "right", padx = 5, pady = 5)





root.mainloop()