from customtkinter import *
from GUI import login

if __name__ == '__main__':
    root = CTk()
    root.rowconfigure([0],weight=1)
    root.columnconfigure([0,1],weight=1)
    #Creating app icon
    root.iconbitmap('Images/icon.ico')
    #Disable resizing
    root.resizable(False, False)
    #Getting info about screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    app_width =app_height = screen_width//2
    #Setting app position and geometry
    x_position = (screen_width - app_width) // 2
    y_position = (screen_height - app_height) // 2
    root.geometry(f"{x_position}+{y_position}")
    #Setting title
    root.title('Dentistry app')
    #Calling the Login page
    main_frame =CTkFrame(root)
    main_frame.grid(sticky="nsew")
    login.LoginPage(main_frame)
    #Running the app
    root.mainloop()