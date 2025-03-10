from tkinter import *

class SignUpPage:
    def __init__(self,main_frame):
        #prevening circular imports
        from GUI import login
        self.main_frame = main_frame
        self.main_frame.forget()
        self.main_frame = Frame()
        self.main_frame.pack(expand=True)

        self.usr_name_label = Label(self.main_frame,text='Username')
        self.usr_name_label.grid(row=0, column=0,sticky='w')

        self.usr_name_field = Entry(self.main_frame)
        self.usr_name_field.grid(row=0, column=1,sticky='w')

        self.usr_phone_label = Label(self.main_frame, text='Phone Number')
        self.usr_phone_label.grid(row=1, column=0,sticky='w')

        self.usr_phone_field = Entry(self.main_frame)
        self.usr_phone_field.grid(row=1, column=1,sticky='w')

        self.usr_ID_label = Label(self.main_frame, text='National ID')
        self.usr_ID_label.grid(row=2, column=0,sticky='w')

        self.usr_ID_field = Entry(self.main_frame)
        self.usr_ID_field.grid(row=2, column=1,sticky='w')

        self.usr_pass_label = Label(self.main_frame, text='Password')
        self.usr_pass_label.grid(row=3, column=0,sticky='w')

        self.usr_pass_field = Entry(self.main_frame)
        self.usr_pass_field.grid(row=3, column=1,sticky='w')

        self.usr_cnfpass_label = Label(self.main_frame, text='Confirm Password')
        self.usr_cnfpass_label.grid(row=4, column=0,sticky='w')

        self.usr_cnfpass_field = Entry(self.main_frame)
        self.usr_cnfpass_field.grid(row=4, column=1,sticky='w')

        self.sbmt_btn = Button(self.main_frame,text='Submit')
        self.sbmt_btn.grid(row=5,column=0,columnspan=2)

        self.bck_to_lgn_btn = Button(master=self.main_frame,text='Back to login',command=lambda:login.LoginPage(self.main_frame))
        self.bck_to_lgn_btn.grid(row=6,column=0,columnspan=2)

