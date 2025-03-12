from customtkinter import *
from PIL import ImageTk, Image

class LoginPage:
    def __init__(self,main_frame):
        #prevening circular imports
        from GUI import signup
        #Removing old widgets
        for widget in main_frame.winfo_children():
            widget.destroy()
        self.main_frame = main_frame
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        #Setting app image
        self.img = Image.open('Images/logo.jfif')
        self.app_img = CTkImage(light_image=self.img, size=self.img.size)
        self.img_lbl = CTkLabel(self.main_frame,image=self.app_img,text='')
        self.img_lbl.grid(row=0,column=0,padx=5,pady=5, sticky="nsew")
        #Craeting right frame
        self.right_frame = CTkFrame(master=self.main_frame)
        self.right_frame.grid(row=0,column=1,padx=5,pady=5, sticky="nsew")
        self.right_frame.columnconfigure([0, 1],weight=1)
        self.right_frame.rowconfigure([0,1,2,3,4], weight=1)
        #Creating widgets
        self.usr_name_label = CTkLabel(self.right_frame,text='Username')
        self.usr_name_label.grid(row=0, column=0,padx=5,pady=5,sticky='w')

        self.usr_name_field = CTkEntry(self.right_frame)
        self.usr_name_field.grid(row=0, column=1,padx=5,pady=5,sticky='w')

        self.usr_pass_label = CTkLabel(self.right_frame,text='Password')
        self.usr_pass_label.grid(row=1, column=0,padx=5,pady=5,sticky='w')

        self.usr_pass_field = CTkEntry(self.right_frame,show="*")
        self.usr_pass_field.grid(row=1, column=1,padx=5,pady=5,sticky='w')

        self.login_btn = CTkButton(self.right_frame,text='Login',command=self.log_in)
        self.login_btn.grid(row=2,column=0,columnspan=2,padx=5,pady=5, sticky="ew")

        self.dnt_hv_acc_lbl = CTkLabel(self.right_frame,text="Don't have an account? Signup")
        self.dnt_hv_acc_lbl.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

        self.sign_up_btn = CTkButton(self.right_frame,text='Signup',command=lambda:signup.SignUpPage(self.main_frame))
        self.sign_up_btn.grid(row=4,column=0,columnspan=2,padx=5,pady=5, sticky="ew")


    def log_in(self):
        from GUI import appointments
        if True:
            appointments.AppointmentsPage(self.main_frame)






