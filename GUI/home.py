from customtkinter import *
from tkcalendar import DateEntry


class HomePage:

    def __init__(self, main_frame):
        # Removing old widgets from main frame
        for widget in main_frame.winfo_children():
            widget.destroy()
        self.main_frame = main_frame
        self.main_frame.columnconfigure([0,1],weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        #Creating left frame
        self.left_frame = CTkFrame(master= self.main_frame)
        self.left_frame.grid(row=0,column=0,padx=5,pady=5, sticky="nsew")
        self.left_frame.columnconfigure([0,1],weight=1)
        self.left_frame.rowconfigure(0,weight=0)
        self.left_frame.rowconfigure(1, weight=1)
        #Adding date entry widget
        self.date_entry = DateEntry(self.left_frame,
                               background='darkblue',
                               foreground='white',
                               borderwidth=2,
                               date_pattern="dd/mm/yyyy",
                               state="readonly",
                                showweeknumbers=False,
                                )
        self.date_entry.grid(row=0,column=0,sticky='nsew',padx=5,pady=5)
        self.date_entry.bind("<<DateEntrySelected>>", self.on_date_selected)
        #View appointments button
        self.view_app_btn = CTkButton(self.left_frame, text="View appointments",command=self.list_appointments)
        self.view_app_btn.grid(row=0,column=1,sticky='ew',padx=5,pady=5)
        #Creating right frame
        self.right_frame = CTkFrame(master=self.main_frame)
        self.right_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.right_frame.columnconfigure(0,weight=1)
        self.right_frame.rowconfigure([0, 1, 2, 3, 4, 5],weight=1)
        #Creating buttons in right frame
        self.list_of_btn = [('Profile', 0),('New appointment',1),('View rooms',2),('View doctors',3)]
        for btn,row in self.list_of_btn:
            new_btn = CTkButton(self.right_frame, text=btn)
            new_btn.grid(row=row,column=0,padx=5,pady=5, sticky="ew")
        #Creating the new frame to hold appointments
        self.new_frame = None


    #Bring focus back to the main window after selecting a date
    def on_date_selected(self,event):
        self.main_frame.focus_force()

    #Listing appointments
    def list_appointments(self):

        fake_list = [('13/03/2025 10:00 AM', 1, 'Doc Ahmed', 1, 'Pat ali'),
                     ('13/03/2025 1:00 PM', 2, 'Doc Sara', 2, 'Pat Soha'),
                     ('13/03/2025 3:00 PM', 3, 'Doc Hima', 1, 'Pat Rabbab'),
                     ('13/03/2025 6:00 PM', 4, 'Doc Ahmed', 3, 'Pat Rana'),]

        fake_list = fake_list + fake_list + fake_list + fake_list +fake_list + fake_list
        #Check the button was clicked before to create the frame to hold appointments
        if not self.new_frame:
            self.new_frame = CTkScrollableFrame(master=self.left_frame)
            self.new_frame.grid(row=1,column=0,columnspan=2,sticky='nsew')
        else:
            for widget in self.new_frame.winfo_children():
                widget.destroy()
        #If list is not empty
        if fake_list:
            #List all appointments
            self.new_frame.columnconfigure([0,1,2,3,4,5],weight=1)
            self.new_frame.rowconfigure(0,weight=0)
            list_of_lbs= [('Date', 0),('Duration',1),('Doctor',2),('Room',3),('Patient',4),("",5)]
            for lbl,col in list_of_lbs:
                new_lbl = CTkLabel(self.new_frame, text=lbl)
                new_lbl.grid(row=0,column=col,padx=5,pady=5, sticky="w")
            row = 1
            for app in fake_list:
                self.new_frame.rowconfigure(row, weight=1)
                col = 0
                for atr in app:
                    new_lbl = CTkLabel(self.new_frame, text=atr)
                    new_lbl.grid(row=row, column=col, padx=5, pady=5, sticky="w")
                    col += 1
                rm_btn = CTkButton(master=self.new_frame,text = 'Cancel')
                rm_btn.grid(row=row, column=5, padx=5, pady=5, sticky="ew")
                row += 1
        else:
            self.new_frame = CTkFrame(master=self.left_frame)
            self.new_frame.grid(row=1,column=0,columnspan=2,sticky='nsew')

            #Alert user that there is no appointments to show
            self.new_frame.columnconfigure(0,weight=1)
            self.new_frame.rowconfigure(0,weight=1)
            new_lbl = CTkLabel(self.new_frame, text="No Appointments")
            new_lbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

            self.new_frame = None
