from tkinter import *
from tkinter import messagebox
import BancoDeDados

class Jan2(Toplevel):

    #════════════════ Criaçao da janela ════════════════
    def __init__(self, original):
        self.frame_original = original
        Toplevel.__init__(self)
        self.title("NOME APP")
        #self.iconbitmap("CodigoLogin/icone.ico")
        self.configure_tela()
        self.widgets()

    def configure_tela(self):
        self.configure(bg='white')
        self.geometry('400x600')
        self.resizable(False, False)

    #════════════════ WIDGETS ════════════════

    def widgets(self):

        #════════════════ TEXTO CADASTRO ════════════════

        self.NomeCadastro = Label(self, text='CADASTRO', font=('Impact', 35), bg='White', fg='#00BFFF')
        self.NomeCadastro.place(x= 50, y=100, height=50, width=300) #.pack() .grod

        #════════════════ NOME ════════════════

        self.NomeLogin = Label(self, text='NOME:', font=('Impact', 14,),bg='White', fg='#00BFFF')
        self.NomeLogin.place(x= -40, y=210, height=50, width=300) #.pack() .grod

        self.EntryNome = Entry(self).place(x=142, y= 225, )

        #════════════════ EMAIL ════════════════

        self.EmailLogin = Label(self, text='EMAIL:', font=('Impact', 14), bg='White', fg='#00BFFF')
        self.EmailLogin.place(x= -40, y=245, height=50, width=300) #.pack() .grod)

        self.EntryEmail = Entry(self).place(x=142, y= 260, )

        #════════════════ SENHA ════════════════

        self.SenhaLogin = Label(self, text='SENHA:', font=('Impact', 14), bg= 'White', fg='#00BFFF')
        self.SenhaLogin.place(x= 82, y=287) #height=50, width=300) #.pack() .grod)

        self.EntrySenha = Entry(self).place(x=142, y= 292)

        #════════════════ BOTÕES ════════════════

        self.btn = Button(self, text='CRIAR', bg='white', fg='black', command=self.LoginFeito)
        self.btn.pack()
        self.btn.place(x=148, y= 350, height=30, width=100)

        self.btn = Button(self, text='VOLTAR', bg='white', fg='black', command=self.onClose)
        self.btn.pack()
        self.btn.place(x=148, y= 400, height=30, width=100)
    

    def LoginFeito(self):
        self.destroy()
        self.frame_original.show()

        Nome = self.EntryNome.get()
        Email = self.EntryEmail.get()
        Senha = self.EntrySenha.get()

        BancoDeDados.cursor.execute("""
        INSERT INTO Usuarios(Nome, Email, Senha) VALUES(?,?,?)
        """, (Nome, Email, Senha))
        BancoDeDados.conn.commit()
        messagebox.showinfo(title= 'Registro', messagebox='Conta criada com sucesso, faço o login')


    def onClose(self):
        self.destroy()
        self.frame_original.show()



class App:

    #════════════════ CRIAÇÃO JANELA ════════════════

    def __init__(self):
        self.root = root
        self.root.title("NOME APP")
        #self.root.iconbitmap("CodigoLogin/icone.ico")
        self.widgets()
        self.configure_tela()

        root.mainloop()

    def configure_tela(self):
        self.root.configure(bg='white')
        self.root.geometry('400x600')
        self.root.resizable(False, False)

    #════════════════ WIDGETS ════════════════

    def widgets(self):
        ola = Label(self.root,
         text='NOME APP',
         width=60, 
         height=60,
         font=('Impact', 35),
         bg='#FFFAF0', 
         fg='#00BFFF')
        ola.place(x= 50, y=120, height=50, width=300) #.pack() .grod

        ola = Label(self.root,
         text='NOME',
         width= 0, 
         height= 0,
         font=('Impact', 14,),
         bg='#FFFAF0', 
         fg='#00BFFF')
        ola.place(x= -40, y=210, height=50, width=300) #.pack() .grod

        ola = Label(self.root,
         text='SENHA',
         width=- 0, 
         height= 0,
         font=('Impact', 14),
         bg='#FFFAF0', 
         fg='#00BFFF')
        ola.place(x= -40, y=245, height=50, width=300) #.pack() .grod

        #════════════════ BOTÕES ════════════════

        self.btn_login = Button(
            self.root, 
            text='LOGAR-SE', 
            width=5, 
            height=5,
            bg='white', 
            fg='black',
            command=self.FuncaoLogin
           )
        
        self.btn_registre = Button(
            self.root, 
            text='CADASTRE-SE', 
            width=5, 
            height=5,
            bg='white', 
            fg='black',
            command=self.entra_jan2
            )

        self.login1 = Entry(self.root).place(x=140, y= 225)

        self.senha1 = Entry(self.root).place(x=140, y= 260)

        self.btn_login.pack()
        self.btn_login.place(x=148, y= 350, height=30, width=100)

        self.btn_registre.pack()
        self.btn_registre.place(x=148, y= 400, height=30, width=100)

    def entra_jan2(self):
        self.subFrame = Jan2(self)
        self.hide()


    def hide(self):
        self.root.withdraw()
    def show(self):
        self.root.update()
        self.root.deiconify()

    def FuncaoLogin(self):
        self.root.destroy()

    

# Programa Principal
root = Tk()
App()