import customtkinter
from PIL import ImageTk, Image


def app_Screen():
    global window, dados, lista_dados
    
    window = customtkinter.CTk()
    window.geometry("1280x720")
    window.resizable(False, False)
    window.wm_title("Banco de Dados")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    dados = {}
    lista_dados = []


def submit():

    dados["email"] = email_entry.get()
    dados["senha"] = password_entry.get()

    lista_dados.append(dados.copy())
    print(lista_dados)


def background_img():

    img_bg = Image.open("img/background.jpg").resize((1920, 1080), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img_bg)
    img_label = customtkinter.CTkLabel(window, image=img_tk)
    img_label.pack()


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


def frame():
    
    frame_1 = customtkinter.CTkFrame(window, width=710, height=720, fg_color="white")
    frame_1.place(x=990, y=360, anchor="center")


def text_Section():

    text_label = customtkinter.CTkLabel(window, text="Crie ou entre na sua conta.", font=("Roboto", 40), text_color=("white"))
    text_label.place(relx=0.06, rely=0.1)


def text_Img():
  
    text_img = customtkinter.CTkLabel(window, text="Um app fácil de se usar\nCrie sua conta agora mesmo", font=("Roboto", 30), text_color="black", bg_color="white")
    text_img.place(relx=0.75, rely=0.73, anchor="center")


def login_Button():

    login_btn = customtkinter.CTkButton(window, text="Login", font=("Roboto", 17),width=220, corner_radius=20)
    login_btn.place(relx=0.25, rely=0.68 , anchor="center")


def register_Button():
    
    register_btn = customtkinter.CTkButton(window, text="Register", font=("Roboto", 17), command=submit, width=220, corner_radius=20, bg_color="transparent")
    register_btn.place(relx=0.25, rely=0.75, anchor="center")


def email_Input():
    global email_entry

    email_entry = customtkinter.CTkEntry(window, placeholder_text="Seu email", width=250, corner_radius=20)
    email_entry.place(relx=0.25, rely=0.55, anchor="center")
    
    
def password_Input():
    global password_entry

    password_entry = customtkinter.CTkEntry(window, placeholder_text="Sua senha", width=250, corner_radius=20, show="*")
    password_entry.place(relx=0.25, rely=0.6, anchor="center")




app_Screen()
#background_img()
frame()
img_Person()
img_World()
text_Section()
login_Button()
register_Button()
#text_Img()
email_Input()
password_Input()


window.mainloop()




