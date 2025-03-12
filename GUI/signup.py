from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class SignUpPage:

    def __init__(self,main_frame):
        #prevening circular imports
        from GUI import login
        for widget in main_frame.winfo_children():
            widget.destroy()
        self.main_frame = main_frame
        self.main_frame.columnconfigure([0, 1],weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        #Setting app image
        self.img=Image.open('Images/logo.jfif')
        self.app_img = CTkImage(light_image=self.img,size=self.img.size)
        self.img_lbl = CTkLabel(self.main_frame,image=self.app_img,text='')
        self.img_lbl.grid(row=0,column=0,padx=5,pady=5, sticky="nsew")
        #Craeting right frame
        self.right_frame = CTkFrame(master=self.main_frame)
        self.right_frame.grid(row=0,column=1,padx=5,pady=5, sticky="nsew")
        self.right_frame.columnconfigure([0, 1],weight=1)
        self.right_frame.rowconfigure([0,1,2,3,4], weight=1)
        #Creating widgets
        self.usr_name_label = CTkLabel(self.right_frame,text='Username')
        self.usr_name_label.grid(row=0, column=0,sticky='w',padx=5,pady=5)

        self.usr_name_field = CTkEntry(self.right_frame)
        self.usr_name_field.grid(row=0, column=1,sticky='w',padx=5,pady=5)

        self.usr_phone_label = CTkLabel(self.right_frame, text='Phone Number')
        self.usr_phone_label.grid(row=1, column=0,sticky='w',padx=5,pady=5)

        self.usr_phone_field = CTkEntry(self.right_frame)
        self.usr_phone_field.grid(row=1, column=1,sticky='w',padx=5,pady=5)

        self.usr_ID_label = CTkLabel(self.right_frame, text='National ID')
        self.usr_ID_label.grid(row=2, column=0,sticky='w',padx=5,pady=5)

        self.usr_ID_field = CTkEntry(self.right_frame)
        self.usr_ID_field.grid(row=2, column=1,sticky='w',padx=5,pady=5)

        self.usr_pass_label = CTkLabel(self.right_frame, text='Password')
        self.usr_pass_label.grid(row=3, column=0,sticky='w',padx=5,pady=5)

        self.usr_pass_field = CTkEntry(self.right_frame,show="*")
        self.usr_pass_field.grid(row=3, column=1,sticky='w',padx=5,pady=5)

        self.usr_cnfpass_label = CTkLabel(self.right_frame, text='Confirm Password')
        self.usr_cnfpass_label.grid(row=4, column=0,sticky='w',padx=5,pady=5)

        self.usr_cnfpass_field = CTkEntry(self.right_frame,show="*")
        self.usr_cnfpass_field.grid(row=4, column=1,sticky='w',padx=5,pady=5)

        self.sbmt_btn = CTkButton(self.right_frame,text='Submit',command=self.sign_up)
        self.sbmt_btn.grid(row=5,column=0,columnspan=2,padx=5,pady=5, sticky="ew")

        self.bck_to_lgn_btn = CTkButton(master=self.right_frame,text='Back to login',command=lambda:login.LoginPage(self.main_frame))
        self.bck_to_lgn_btn.grid(row=6,column=0,columnspan=2,padx=5,pady=5, sticky="ew")

    def sign_up(self):
        from GUI import login
        if True:
            messagebox.showinfo("Welcome on board", "Credentials submitted correctly")
            login.LoginPage(self.main_frame)

