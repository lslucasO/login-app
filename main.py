import customtkinter


class App:

    def __init__(self, window: customtkinter.CTk):
        self.window = window
        self.window.geometry("300x600")
        self.window.resizable(False, False)
        self.window.wm_title("Data")

        self.user_email = {
            "email"
        }

        App.text_Page(self=self)
        App.login_Entry(self=self)
        App.password_Entry(self=self)
        App.login_Button(self=self)
        App.register_Button(self=self)


    def login_Button(self):

        self.login_btn = customtkinter.CTkButton(self.window, text="Login", command=App.button_Click, corner_radius=20)
        self.login_btn.pack(padx=10, pady=10)
        

    def text_Page(self):

        self.text_label = customtkinter.CTkLabel(self.window, text="Fazer login", width=200, height=25)
        self.text_label.pack(padx=10, pady=100)

    
    def register_Button(self):
        
        self.register_btn = customtkinter.CTkButton(self.window, text="Register", command=App.button_Click, corner_radius=20)
        self.register_btn.pack(padx=10, pady=10)

    
    def login_Entry(self):

        self.login_entry = customtkinter.CTkEntry(self.window, placeholder_text="Seu email", width=200, corner_radius=20)
        self.login_entry.pack(padx=10, pady=10)
        

    
    def password_Entry(self):

        self.password_entry = customtkinter.CTkEntry(self.window, placeholder_text="Sua senha", width=200, corner_radius=20, show="*")
        self.password_entry.pack(padx=10, pady=10)
    


    def button_Click():

        return print("Working")


if __name__ == "__main__":
    app = customtkinter.CTk()
    gui = App(window=app)
    app.mainloop()
    
    



