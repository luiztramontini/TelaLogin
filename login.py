import customtkinter as ctk

#Configuração aparência
ctk.set_appearance_mode('dark')

#Criação das funcionalidades
def validar_login():
    email = campo_email.get()
    senha = campo_senha.get()

    if email == 'Luiz' or 'luiz' and senha == '12345':
        feedback_email.configure(text='Login feito com sucesso!', text_color='green')
    else:
        feedback_email.configure(text='Login incorreto', text_color='red')

#Criação da janela principal 
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#Criação dos campos 
#Label
label_email = ctk.CTkLabel(app, text='Email:')
label_email.pack(pady=10)
#Entry
campo_email = ctk.CTkEntry(app, placeholder_text='Digite seu email')
campo_email.pack(pady=10)
#Label
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=10)
#Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)
#Button
botao_acesso= ctk.CTkButton(app, text='Entrar', command=validar_login)
botao_acesso.pack(pady=10)
#Feddback Login 
feedback_email= ctk.CTkLabel(app, text='')
feedback_email.pack(pady=10)

#iniciar aplicação
app.mainloop()