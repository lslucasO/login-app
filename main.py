import customtkinter, data, asyncio
from PIL import ImageTk, Image

widget = False
dados = {}
lista_dados = []


def app_Screen():
    global window, dados, lista_dados
    
    window = customtkinter.CTk()
    window.geometry("1280x720")
    window.resizable(False, False)
    window.wm_title("Banco de Dados")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")


def frame():
    
    frame_1 = customtkinter.CTkFrame(window, width=710, height=720, fg_color="white")
    frame_1.place(x=990, y=360, anchor="center")

    
def get_user():
    global widget
    
    if widget:
        registered_text.destroy()
        email_entry.delete(0,  len(email_entry.get()))
        widget = False
    else:
        registered_Text()
        clear_Data()

        dados["email"] = email_entry.get()
        dados["senha"] = password_entry.get()

        lista_dados.append(dados.copy())
        
        
def clear_Data():
    
    email_entry.delete(0,  len(email_entry.get()))
    password_entry.delete(0, len(password_entry.get()))





def img_World():

    img1 = Image.open("img/main_image-removebg-preview.png").resize((650, 650),Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img1)
    img_label = customtkinter.CTkLabel(master=window, image=img_tk, text="", bg_color="white")
    img_label.place(relx=0.75, rely=0.45, anchor="center")


def img_Person():

    img1 = Image.open("img/person1-removebg-preview.png").resize((300, 300),Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img1)
    img_label = customtkinter.CTkLabel(master=window, image=img_tk, text="")
    img_label.place(relx=0.25, rely=0.37, anchor="center")



def registered_Text():
    global registered_text, widget
    
    widget = True
    
    registered_text = customtkinter.CTkLabel(window, text="Registrado com sucesso!", font=("Roboto", 15), text_color="lightgreen")
    registered_text.place(relx=0.17, rely=0.87)  
    

def text_Section():

    text_label = customtkinter.CTkLabel(window, text="Crie ou entre na sua conta.", font=("Roboto", 40), text_color=("white"))
    text_label.place(relx=0.06, rely=0.1)



def login_Button():

    login_btn = customtkinter.CTkButton(window, text="Entrar", font=("Roboto", 17),width=220, corner_radius=20)
    login_btn.place(relx=0.25, rely=0.75 , anchor="center")


def register_Button():
    
        
    register_btn = customtkinter.CTkButton(window, text="Cadastrar", font=("Roboto", 17), command=get_user, width=220, bg_color="transparent",
                                           corner_radius=20)
    register_btn.place(relx=0.25, rely=0.81, anchor="center")



def email_Input():
    
    global email_entry

    email_entry = customtkinter.CTkEntry(window, placeholder_text="Seu email", width=250, corner_radius=20)
    email_entry.place(relx=0.25, rely=0.55, anchor="center")
      
    
def password_Input():
    global password_entry

    password_entry = customtkinter.CTkEntry(window, placeholder_text="Sua senha", width=250, corner_radius=20, show="*")
    password_entry.place(relx=0.25, rely=0.6, anchor="center")



def account_Checkbox():
    
    checkbox = customtkinter.CTkCheckBox(window, text="Lembrar de mim", width=100)
    checkbox.place(relx=0.16, rely=0.65)



app_Screen()
frame()
img_Person()
img_World()
text_Section()
email_Input()
password_Input()
register_Button()
login_Button()
account_Checkbox()


window.mainloop()




