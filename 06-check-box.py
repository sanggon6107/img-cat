from tkinter import *

root = Tk()
root.title("check-box")
root.geometry("640x480+200+200")

check_information = {0 : "체크 해제", 1 : "체크"}

def btncmd() :
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크 
    print(chkvar_2.get()) # 0 : 체크 해제, 1 : 체크 
    lbl.config(text = "체크박스1 : {0}   체크박스2 : {1}".format(check_information[ chkvar.get() ],
                                                             check_information[ chkvar_2.get() ]))



chkvar = IntVar() # 체크 상태를 int형으로 반환하여 그 값을 chkvar에 저장한다.
chkbox = Checkbutton(root, text = " check button", variable = chkvar, command = btncmd)
chkbox.select() # 체크바에 체크한다.
chkbox.deselect() # 체크바 체크 해제한다.
chkbox.pack()

chkvar_2 = IntVar()
chkbox_2 = Checkbutton(root, text = "check_button_2", variable = chkvar_2, command = btncmd)
chkbox_2.pack()




btn = Button(root, text = "Button", command = btncmd)
btn.pack()



lbl = Label(root, text = "체크박스1 : {0}   체크박스2 : {1}".format(check_information[ chkvar.get() ],
                                                                   check_information[ chkvar_2.get() ]))
lbl.pack()


root.mainloop()