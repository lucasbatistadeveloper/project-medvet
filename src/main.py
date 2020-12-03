from tkinter import *
from banco import *

root = Tk()

class Application(database):
    def __init__(self):
        self.root = root
        self.tela()
        self.frameLogin()
        self.widgetsLogin()
        self.montaTabelaCliente()
        self.montaTabelaAnimal()
        root.mainloop()

    def tela(self): #Config main screen
        self.root.title("APP Clínica Veterinária")
        self.root.geometry("375x667")
        self.root.configure(background="#ADD5C1")
        self.root.resizable(False, False)   
    
    def frameLogin(self):
        self.frameLogin = Frame(self.root, bd=4, background="#ADD5C1")
        self.frameLogin.place(relx=0.001, rely=0.0001, relwidth=1, relheight=1)
        
        self.imgLogin = PhotoImage(file="imgs/1.png")
        self.ImagemLogin = Label(self.frameLogin, image=self.imgLogin)
        self.ImagemLogin.place(relx=0.18, rely=0.05, relwidth=0.6, relheight=0.44)
        
        self.imgUser = PhotoImage(file="imgs/user.png")
        self.ImagemUser = Label(self.frameLogin, image=self.imgUser)
        self.ImagemUser.place(relx=0.1, rely=0.5, relwidth=0.1, relheight=0.07)
        
        self.imgPassword = PhotoImage(file="imgs/password.png")
        self.ImagemPassword = Label(self.frameLogin, image=self.imgPassword)
        self.ImagemPassword.place(relx=0.038, rely=0.6, relwidth=0.2, relheight=0.07)
        
        self.imgGit = PhotoImage(file="imgs/github.png")
        self.ImagemGit = Label(self.frameLogin, image=self.imgGit)
        self.ImagemGit.place(relx=0.1, rely=0.9, relwidth=0.2, relheight=0.1)

    def widgetsLogin(self):
        #Entry
        self.userEntry = Entry(self.frameLogin, fg="black", font=('Arial', 12, 'bold'), bg="#ADD5C1", justify=CENTER)
        self.userEntry.place(relx=0.26, rely=0.52)
        
        self.passwordEntry = Entry(self.frameLogin, fg="black", font=('Arial', 12, 'bold'), bg="#ADD5C1", justify=CENTER, show="*")
        self.passwordEntry.place(relx=0.26, rely=0.62)
        
        #Button
        self.loginButton = Button(self.frameLogin, text="Login", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black")
        self.loginButton.place(relx=0.34, rely=0.7, relwidth=0.3, relheight=0.05)
        
        self.registerButton = Button(self.frameLogin, text="Register", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black", command=self.frameRegister)
        self.registerButton.place(relx=0.34, rely=0.78, relwidth=0.3, relheight=0.05)
        
        #Label
        self.github = Label(self.frameLogin, text="github/lucasbatistadeveloper", bg="#ADD5C1", fg="black", font=('Arial', 10, 'bold'))
        self.github.place(relx=0.3, rely=0.925)

    def frameRegister(self):
        self.frameRegister = Frame(self.root, bd=4, background="#ADD5C1")
        self.frameRegister.place(relx=0.001, rely=0.0001, relwidth=1, relheight=1)
        
        self.imgRegister = PhotoImage(file="imgs/1.png")
        self.ImagemRegister = Label(self.frameRegister, image=self.imgRegister)
        self.ImagemRegister.place(relx=0.18, rely=0.05, relwidth=0.6, relheight=0.44)
        
        self.imgRegisterA = PhotoImage(file="imgs/2.png")
        self.ImagemRegister = Label(self.frameRegister, image=self.imgRegisterA)
        self.ImagemRegister.place(relx=0.15, rely=0.51, relwidth=0.20, relheight=0.142)
        
        self.imgRegisterB = PhotoImage(file="imgs/3.png")
        self.ImagemRegister = Label(self.frameRegister, image=self.imgRegisterB)
        self.ImagemRegister.place(relx=0.55, rely=0.505, relwidth=0.21, relheight=0.15)
        
        self.imgGitA = PhotoImage(file="imgs/github.png")
        self.ImagemGitA = Label(self.frameRegister, image=self.imgGitA)
        self.ImagemGitA.place(relx=0.1, rely=0.9, relwidth=0.2, relheight=0.1)
        
        self.widgetsRegister()
        
    def widgetsRegister(self):        
        #Button
        self.clienteButton = Button(self.frameRegister, text="Cliente", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black", command=self.frameCliente)
        self.clienteButton.place(relx=0.13, rely=0.67, relwidth=0.25, relheight=0.05)
        
        self.animalButton = Button(self.frameRegister, text="Animal", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black")
        self.animalButton.place(relx=0.53, rely=0.67, relwidth=0.25, relheight=0.05)
        
        self.returnButton = Button(self.frameRegister, text="Retornar ao login", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black", command=self.OcultarFrameRegister)
        self.returnButton.place(relx=0.28, rely=0.78, relwidth=0.35, relheight=0.05)
       
        #Label
        self.githubA = Label(self.frameRegister, text="github/lucasbatistadeveloper", bg="#ADD5C1", fg="black", font=('Arial', 10, 'bold'))
        self.githubA.place(relx=0.3, rely=0.925)
    
    def frameCliente(self):
        self.frameCliente = Frame(self.root, bd=4, background="#ADD5C1")
        self.frameCliente.place(relx=0.001, rely=0.0001, relwidth=1, relheight=1)
        
        self.widgetsCliente()
        
        self.imgCliente = PhotoImage(file="imgs/5.png")
        self.ImagemCliente = Label(self.frameCliente, image=self.imgCliente)
        self.ImagemCliente.place(relx=0.18, rely=0.05, relwidth=0.6, relheight=0.33)
        
        self.imgGitCliente = PhotoImage(file="imgs/github.png")
        self.ImagemGit = Label(self.frameCliente, image=self.imgGitCliente)
        self.ImagemGit.place(relx=0.1, rely=0.9, relwidth=0.2, relheight=0.1)
        
    def widgetsCliente(self):
        #Entry
        self.newUserEntry = Entry(self.frameCliente, fg="black", font=('Arial', 12, 'bold'), bg="#ADD5C1", justify=CENTER)
        self.newUserEntry.place(relx=0.23, rely=0.45)
        
        self.newPasswordEntry = Entry(self.frameCliente, fg="black", font=('Arial', 12, 'bold'), bg="#ADD5C1", justify=CENTER)
        self.newPasswordEntry.place(relx=0.23, rely=0.55)
        
        self.newPhoneEntry = Entry(self.frameCliente, fg="black", font=('Arial', 12, 'bold'), bg="#ADD5C1", justify=CENTER)
        self.newPhoneEntry.place(relx=0.23, rely=0.65)
        
        #Button
        self.CadastroButton = Button(self.frameCliente, text="Cadastrar", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black", command=self.criarCliente)
        self.CadastroButton.place(relx=0.27, rely=0.72, relwidth=0.4, relheight=0.05)
        
        self.returnCadastroButton = Button(self.frameCliente, text="Retornar ao login", font=('Arial', 10, 'bold'), background="#ADD5C1", fg="black", command=self.OcultarFrameCliente)
        self.returnCadastroButton.place(relx=0.27, rely=0.78, relwidth=0.4, relheight=0.05)
        
        #Label
        self.newUser = Label(self.frameCliente, text="Nome de usuário", bg="#ADD5C1", fg="black", font=('Arial', 10, 'bold'))
        self.newUser.place(relx=0.32, rely=0.4)
        
        self.newPassword = Label(self.frameCliente, text="Senha de usuário", bg="#ADD5C1", fg="black", font=('Arial', 10, 'bold'))
        self.newPassword.place(relx=0.31, rely=0.5)
        
        self.newPhone = Label(self.frameCliente, text="Telefone do usuário", bg="#ADD5C1", fg="black", font=('Arial', 10, 'bold'))
        self.newPhone.place(relx=0.3, rely=0.6)
        
        self.githubCliente = Label(self.frameCliente, text="github/lucasbatistadeveloper", bg="#ADD5C1", fg="black", font=('Arial', 10, 'bold'))
        self.githubCliente.place(relx=0.3, rely=0.925)
    
    def criarCliente(self):
        self.bdConnect()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, password_cliente, telefone) VALUES (?, ?, ?)""", 
        (self.newUserEntry.get(), self.newPasswordEntry.get(), self.newPhoneEntry.get()))

        self.conn.commit()
        self.bdDisconnect()
        
    def selectCliente(self):
        self.bdConnect()
        lista = self.cursor.execute(""" SELECT nome_cliente, password_cliente, telefone FROM clientes
        ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCli.insert("", END, values=i)
            
        self.bdDisconnect()
        
    def OcultarFrameRegister(self):
        self.frameRegister.place(relx=0.001, rely=0.0001, relwidth=0.0000001, relheight=0.000001)
    def OcultarFrameCliente(self):
        self.frameCliente.place(relx=0.001, rely=0.0001, relwidth=0.0000001, relheight=0.000001)
    
Application()