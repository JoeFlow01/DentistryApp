from customtkinter import *
class AppointmentsPage:

    def __init__(self, main_frame):
        # Removing old widgets
        for widget in main_frame.winfo_children():
            widget.destroy()
        self.main_frame = main_frame
        self.main_frame.columnconfigure([0,1],weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        #Creating left frame
        self.left_frame = CTkFrame(master= self.main_frame)
        self.left_frame.grid(row=0,column=0,padx=5,pady=5, sticky="nsew")
        #Creating right frame
        self.right_frame = CTkFrame(master=self.main_frame)
        self.right_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.right_frame.columnconfigure(0,weight=1)
        self.right_frame.rowconfigure([0, 1, 2, 3, 4, 5],weight=1)
        #Creating buttons
        self.list_of_btn = [('Profile', 0),('New appointment',1),('View rooms',2),('View doctors',3)]
        for btn,row in self.list_of_btn:
            new_btn = CTkButton(self.right_frame, text=btn)
            new_btn.grid(row=row,column=0,padx=5,pady=5, sticky="ew")