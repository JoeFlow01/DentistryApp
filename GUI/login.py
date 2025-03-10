from tkinter import *

class LoginPage:
    def __init__(self,main_frame):
        #prevening circular imports
        from GUI import signup
        self.main_frame = main_frame
        self.main_frame.forget()
        self.main_frame = Frame()
        self.main_frame.pack(expand=True)

        self.usr_name_label = Label(self.main_frame,text='Username')
        self.usr_name_label.grid(row=0, column=0)

        self.usr_name_field = Entry(self.main_frame)
        self.usr_name_field.grid(row=0, column=1)

        self.usr_pass_label = Label(self.main_frame,text='Password')
        self.usr_pass_label.grid(row=1, column=0)

        self.usr_pass_field = Entry(self.main_frame)
        self.usr_pass_field.grid(row=1, column=1)

        self.login_btn = Button(self.main_frame,text='Login')
        self.login_btn.grid(row=2,column=0,columnspan=2)

        self.dnt_hv_acc_lbl = Label(self.main_frame,text="Don't have an account? Signup")
        self.dnt_hv_acc_lbl.grid(row=3,column=0,columnspan=2)

        self.sign_up_btn = Button(self.main_frame,text='Signup',command=lambda:signup.SignUpPage(self.main_frame))
        self.sign_up_btn.grid(row=4,column=0,columnspan=2)




