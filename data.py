import customtkinter
from PIL import ImageTk, Image

widget = False
dados = {}
lista_dados = []



def delete_LoginFrame():

    frame_login.destroy()
 
 
def get_user():
    global widget
    
    if widget:
        registered_text.destroy()
        widget = False
    else:
        registered_Text()
        
        dados["email"] = email_entry.get()
        dados["senha"] = password_entry.get()

        lista_dados.append(dados.copy())
        print(lista_dados)
        
        clear_Data()
            
        
def clear_Data():
        
    email_entry.delete(0,  len(email_entry.get()))
    password_entry.delete(0, len(password_entry.get()))



def planeta_Frame():
    
    
    frame_planeta = customtkinter.CTkFrame(window, width=710, height=720, fg_color="white")
    frame_planeta.place(x=990, y=360, anchor="center")
    
        
        
    def img_Planeta():
    
        img1 = Image.open("img/planeta.png").resize((650, 650),Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img1)
        img_label = customtkinter.CTkLabel(master=frame_planeta, image=img_tk, text="", bg_color="white")
        img_label.place(relx=0.5, rely=0.45, anchor="center")   

   
    img_Planeta()
   

def login_Frame():
    global frame_login
    
    frame_login = customtkinter.CTkFrame(window, width=710, height=720)
    frame_login.place(x=290, y=360, anchor="center")
    
    
    def img_Pessoa():
        
        img1 = Image.open("img/pessoa.png").resize((300, 300),Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img1)
        img_label = customtkinter.CTkLabel(master=frame_login, image=img_tk, text="")
        img_label.place(relx=0.55, rely=0.37, anchor="center")
        
    
    def text_Section():

        text_label = customtkinter.CTkLabel(frame_login, text="Crie ou entre na sua conta.", font=("Roboto", 40), text_color=("white"))
        text_label.place(relx=0.2, rely=0.1)
        
        
    def email_Input():
        global email_entry

        email_entry = customtkinter.CTkEntry(frame_login, placeholder_text="Seu email", width=250, corner_radius=20)
        email_entry.place(relx=0.55, rely=0.55, anchor="center")
        
        
    def password_Input():
        global password_entry

        password_entry = customtkinter.CTkEntry(frame_login, placeholder_text="Sua senha", width=250, corner_radius=20, show="*")
        password_entry.place(relx=0.55, rely=0.6, anchor="center")
        
        
    def login_Button():

        login_btn = customtkinter.CTkButton(frame_login, text="Entrar", font=("Roboto", 17),width=220, corner_radius=20)
        login_btn.place(relx=0.55, rely=0.75 , anchor="center")


    def register_Button():
        
            
        register_btn = customtkinter.CTkButton(frame_login, text="Cadastrar", font=("Roboto", 17), command=delete_LoginFrame, width=220, bg_color="transparent", corner_radius=20)
        register_btn.place(relx=0.55, rely=0.81, anchor="center")    
        
        
    


    def account_Checkbox():
        
        checkbox = customtkinter.CTkCheckBox(frame_login, text="Lembrar de mim", width=100)
        checkbox.place(relx=0.38, rely=0.65)
    
    
        
        
    text_Section()
    img_Pessoa()
    login_Button()
    register_Button()
    email_Input()
    password_Input()
    account_Checkbox()        


def main_Screen():
    global email_entry, password_entry
    
    
    def app_Screen():
        global window
        
        window = customtkinter.CTk()
        window.geometry("1280x720")
        window.resizable(False, False)
        window.wm_title("Banco de Dados")
        customtkinter.set_default_color_theme("dark-blue")


    def registered_Text():
        global registered_text, widget
        
        widget = True
        
        registered_text = customtkinter.CTkLabel(window, text="Registrado com sucesso!", font=("Roboto", 15), text_color="lightgreen")
        registered_text.place(relx=0.17, rely=0.87)  
        
    


    app_Screen()
    planeta_Frame()
    login_Frame()
    
    window.mainloop()
    



main_Screen()
