import tkinter.messagebox as msgbox
from tkinter import *

root =Tk()
root.title("messagebox")
root.geometry("640x480+200+200")

def info() :
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # 첫번째 인자 : 제목, 두번째 인자 : 메세지박스 내용


def warn() :
    msgbox.showwarning("경고", "좌석이 매진되었습니다.")


def error() :
    msgbox.showerror("에러", "결제 오류")



def enter_cancel() :
    msgbox.askokcancel("확인 / 취소", "확인/취소입니다.")



def retry_cancel() :
    msgbox.askretrycancel("확인 / 취소", "예매 실패하였습니다. 재시도 하시겠습니까?")



def yes_no() :
    msgbox.askyesno("네/아니오", "왕복으로 예매하시겠습니까?")



def yes_no_cancel() :
    response = msgbox.askyesnocancel(title = None, message = "저장 후 프로그램을 종료하시겠습니까?") # 타이틀을 없앨 수 있다.
    print("응답 : ", response)
    # 응답은 순서대로 True, False, None이다.
    # 참고 : 재시도/취소처럼 대답이 두개인 경우, 각각 1, 0으로 반환한다.


Button(root, command = info, text = "알림").pack()
Button(root, command = warn, text = "경고").pack()
Button(root, command = error, text = "에러").pack()
Button(root, command = enter_cancel, text = "확인/취소").pack()
Button(root, command = retry_cancel, text = "재시도/취소").pack()
Button(root, command = yes_no, text = "네/아니오").pack()
Button(root, command = yes_no_cancel, text = "네/아니오/취소").pack()


root.mainloop()