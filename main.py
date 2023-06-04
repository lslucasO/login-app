import customtkinter
from PIL import ImageTk, Image

def app_Screen():
    global window, dados, lista_dados
    
    window = customtkinter.CTk()
    window.geometry("1280x720")
    window.resizable(False, False)
    window.wm_title("Banco de Dados")
    customtkinter.set_default_color_theme("dark-blue")

    dados = {}
    lista_dados = []


def submit():

    dados["email"] = email_entry.get()
    dados["senha"] = password_entry.get()

    lista_dados.append(dados.copy())
    print(lista_dados)


def img_1():

    img1 = Image.open("img/person1-removebg-preview.png").resize((250, 250))
    img_tk = ImageTk.PhotoImage(img1)
    img_label = customtkinter.CTkLabel(window, image=img_tk)
    img_label.place(relx=0.5, rely=0.3, anchor="center")


def frame():
    
    frame_1 = customtkinter.CTkFrame(window, width=350, height=500, corner_radius=20, border_width=3)
    frame_1.place(relx=0.5, rely=0.5, anchor="center")


def text_Section():

    text_label = customtkinter.CTkLabel(window, text="Fazer login", font=("Roboto", 30), text_color=("white"), fg_color="transparent")
    text_label.pack(padx=10, pady=20, anchor="center")


def login_Button():

    login_btn = customtkinter.CTkButton(window, text="Login", font=("Roboto", 14),width=160, corner_radius=20)
    login_btn.place(relx=0.5, rely=0.65 , anchor="center")


def register_Button():
    
    register_btn = customtkinter.CTkButton(window, text="Register", font=("Roboto", 14), command=submit, width=160, corner_radius=20, bg_color="transparent")
    register_btn.place(relx=0.5, rely=0.72, anchor="center")


def email_Input():
    global email_entry

    email_entry = customtkinter.CTkEntry(window, placeholder_text="Seu email", width=200, corner_radius=20)
    email_entry.place(relx=0.5, rely=0.5, anchor="center")
    
    
def password_Input():
    global password_entry

    password_entry = customtkinter.CTkEntry(window, placeholder_text="Sua senha", width=200, corner_radius=20, show="*")
    password_entry.place(relx=0.5, rely=0.56, anchor="center")



app_Screen()
frame()
img_1()
text_Section()
login_Button()
register_Button()
email_Input()
password_Input()


window.mainloop()




