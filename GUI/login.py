from tkinter import *
from PIL import ImageTk, Image

class LoginPage:
    def __init__(self,main_frame):
        #prevening circular imports
        from GUI import signup
        #Removing old widgets
        for widget in main_frame.winfo_children():
            widget.destroy()
        self.main_frame = main_frame
        #Setting app image
        self.app_img = ImageTk.PhotoImage(Image.open('Images/logo.jfif'))
        self.img_lbl = Label(self.main_frame,image=self.app_img)
        self.img_lbl.grid(row=0,column=0,sticky='W')
        #Creting right frame
        self.right_frame = Frame(master=self.main_frame)
        self.right_frame.grid(row=0,column=1)
        #Creating widgets
        self.usr_name_label = Label(self.right_frame,text='Username')
        self.usr_name_label.grid(row=0, column=0)

        self.usr_name_field = Entry(self.right_frame)
        self.usr_name_field.grid(row=0, column=1)

        self.usr_pass_label = Label(self.right_frame,text='Password')
        self.usr_pass_label.grid(row=1, column=0)

        self.usr_pass_field = Entry(self.right_frame)
        self.usr_pass_field.grid(row=1, column=1)

        self.login_btn = Button(self.right_frame,text='Login')
        self.login_btn.grid(row=2,column=0,columnspan=2)

        self.dnt_hv_acc_lbl = Label(self.right_frame,text="Don't have an account? Signup")
        self.dnt_hv_acc_lbl.grid(row=3,column=0,columnspan=2)

        self.sign_up_btn = Button(self.right_frame,text='Signup',command=lambda:signup.SignUpPage(self.main_frame))
        self.sign_up_btn.grid(row=4,column=0,columnspan=2)




