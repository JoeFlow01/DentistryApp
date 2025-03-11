from tkinter import *
from GUI import login

if __name__ == '__main__':
    root = Tk()
    root.iconbitmap('Images/icon.ico')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width//2}x{screen_height//2}")
    root.title('Dentistry app')
    main_frame = Frame()
    main_frame.pack(expand=True)
    login.LoginPage(main_frame)
    root.mainloop()