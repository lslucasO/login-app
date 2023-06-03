import customtkinter

def app_Screen():
    global window, dados, lista_dados
    
    window = customtkinter.CTk()
    window.geometry("300x600")
    window.resizable(False, False)
    window.wm_title("Banco de Dados")

    dados = {}
    lista_dados = []


def submit():

    dados["email"] = email_entry.get()
    dados["senha"] = password_entry.get()

    lista_dados.append(dados.copy())
    print(lista_dados)


def text_Section():

    text_label = customtkinter.CTkLabel(window, text="Fazer login", font=("Roboto", 20))
    text_label.pack(padx=10, pady=180)


def login_Button():

    login_btn = customtkinter.CTkButton(window, text="Login",width=200, corner_radius=20)
    login_btn.place(relx=0.5, rely=0.7, anchor="center")


def register_Button():
    
    register_btn = customtkinter.CTkButton(window, text="Register", command=submit, width=200, corner_radius=20)
    register_btn.place(relx=0.5, rely=0.8, anchor="center")


def email_Input():
    global email_entry

    email_entry = customtkinter.CTkEntry(window, placeholder_text="Seu email", width=200, corner_radius=20)
    email_entry.place(relx=0.5, rely=0.5, anchor="center")
    
    
def password_Input():
    global password_entry

    password_entry = customtkinter.CTkEntry(window, placeholder_text="Sua senha", width=200, corner_radius=20, show="*")
    password_entry.place(relx=0.5, rely=0.6, anchor="center")



app_Screen()
text_Section()
login_Button()
register_Button()
email_Input()
password_Input()



window.mainloop()




