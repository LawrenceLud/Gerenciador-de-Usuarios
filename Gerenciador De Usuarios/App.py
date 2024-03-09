from Usuarios import Usuarios
from tkinter import *
from tkinter import messagebox

class Application:
    def __init__(self, master=None):
        self.fonte = ("Arial", 10)

        self.container_principal = Frame(master, bg="#F0F0F0")
        self.container_principal.pack(expand=True, fill="both")

        self.container1 = Frame(self.container_principal, bg="#F0F0F0")
        self.container1.pack(pady=(20, 10))

        self.container2 = Frame(self.container_principal, bg="#F0F0F0")
        self.container2.pack(pady=5)

        self.container3 = Frame(self.container_principal, bg="#F0F0F0")
        self.container3.pack(pady=5)

        self.container4 = Frame(self.container_principal, bg="#F0F0F0")
        self.container4.pack(pady=5)

        self.container5 = Frame(self.container_principal, bg="#F0F0F0")
        self.container5.pack(pady=5)

        self.container6 = Frame(self.container_principal, bg="#F0F0F0")
        self.container6.pack(pady=5)

        self.container7 = Frame(self.container_principal, bg="#F0F0F0")
        self.container7.pack(pady=5)

        self.container8 = Frame(self.container_principal, bg="#F0F0F0")
        self.container8.pack(pady=5)

        self.titulo = Label(self.container1, text="Gerenciamento de Usuários", font=("Arial", 16, "bold"), bg="#F0F0F0")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="ID:", font=self.fonte, bg="#F0F0F0")
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2, width=10, font=self.fonte)
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, bg="#F0F0F0")
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, bg="#F0F0F0")
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, bg="#F0F0F0")
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, bg="#F0F0F0")
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6, width=25, font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, bg="#F0F0F0")
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7, width=25, font=self.fonte, show="*")
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=10, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT, padx=5)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=10, command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT, padx=5)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=10, command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT, padx=5)

        self.lblmsg = Label(self.container_principal, text="", font=("Arial", 10, "italic"), bg="#F0F0F0")
        self.lblmsg.pack(pady=10)

    def inserirUsuario(self):
        user = Usuarios(nome=self.txtnome.get(), telefone=self.txttelefone.get(), email=self.txtemail.get(), usuario=self.txtusuario.get(), senha=self.txtsenha.get())

        mensagem = user.insertUser()
        messagebox.showinfo("Resultado", mensagem)

        if "sucesso" in mensagem.lower():
            self.limpar_campos()

    def alterarUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get(), nome=self.txtnome.get(), telefone=self.txttelefone.get(), email=self.txtemail.get(), usuario=self.txtusuario.get(), senha=self.txtsenha.get())

        mensagem = user.updateUser()
        messagebox.showinfo("Resultado", mensagem)

        if "sucesso" in mensagem.lower():
            self.limpar_campos()

    def excluirUsuario(self):
        idusuario = self.txtidusuario.get()
        if not idusuario:
            messagebox.showerror("Erro", "Por favor, informe o ID do usuário a ser excluído.")
            return

        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir o usuário com ID {}?".format(idusuario))
        if resposta:
            user = Usuarios(idusuario=idusuario)
            mensagem = user.deleteUser()
            messagebox.showinfo("Resultado", mensagem)

            if "sucesso" in mensagem.lower():
                self.limpar_campos()

    def buscarUsuario(self):
        idusuario = self.txtidusuario.get()
        if not idusuario:
            messagebox.showerror("Erro", "Por favor, informe o ID do usuário a ser buscado.")
            return

        user = Usuarios()
        mensagem = user.selectUser(idusuario)

        if "sucesso" in mensagem.lower():
            self.txtidusuario.delete(0, END)
            self.txtidusuario.insert(0, user.idusuario)

            self.txtnome.delete(0, END)
            self.txtnome.insert(0, user.nome)

            self.txttelefone.delete(0, END)
            self.txttelefone.insert(0, user.telefone)

            self.txtemail.delete(0, END)
            self.txtemail.insert(0, user.email)

            self.txtusuario.delete(0, END)
            self.txtusuario.insert(0, user.usuario)

            self.txtsenha.delete(0, END)
            self.txtsenha.insert(0, user.senha)
        else:
            messagebox.showerror("Erro", mensagem)

    def limpar_campos(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

root = Tk()
root.title("Gerenciamento de Usuários")
root.geometry("400x300")
root.resizable(False, False)
Application(root)
root.mainloop()
