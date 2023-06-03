import customtkinter


class App:

    def __init__(self, window: customtkinter.CTk):
        self.window = window
        self.window.geometry("300x600")
        self.window.resizable(False, False)
        self.window.wm_title("Data")

        App.login_Button(self=self)
        #App.register_Button(self=self)



    def button_Click():

        return print("Working")


    def login_Button(self):

        self.login = customtkinter.CTkButton(self.window, text="Login", command=App.button_Click, corner_radius=20)
        self.login.place(relx=0.5, rely=0.58, anchor="center")
        

    
    def register_Button(self):
        
        self.register = customtkinter.CTkButton(self.window, text="Register", command=App.button_Click, corner_radius=20)
        self.register.place(relx=0.5, rely=0.5, anchor="center")
    


    


if __name__ == "__main__":
    app = customtkinter.CTk()
    gui = App(window=app)
    app.mainloop()
    
    



