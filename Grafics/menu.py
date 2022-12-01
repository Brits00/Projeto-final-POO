from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk

class Menu:
    def __init__(self) -> None:
        self.__menu = Tk()
        self.__title = self.__menu.title("Menu Inicial")
        self.__iconbitmap = self.__menu.iconbitmap(default='Grafics\img\logo.ico')
        self.__geometry = self.__menu.geometry("800x500+282+100")
        self.__size = self.__menu.wm_resizable(width=False,height=False)
        self.__dic = {
                        'João': {'Nome': 'João', 'CPF': 'XY', 'Ano': 1998, 'Mes': 2, 'Dia': 25, 'Genero': 'M'}
                        ,'Bel': {'Nome': 'Bel', 'CPF': 'XX', 'Ano': 2001, 'Mes': 6, 'Dia': 20, 'Genero': 'F'}
                        ,'Kyo': {'Nome': 'Kyo', 'CPF': 'XZ', 'Ano': 2000, 'Mes': 12, 'Dia': 10, 'Genero': 'M'}}

        self.background()
        self.button__Menu()


    def background(self):
        self.fundo = Image.open('Grafics/img/fundo.png').resize((800,500))
        self.fundo = ImageTk.PhotoImage(self.fundo)
        self.label_fundo = Label(self.__menu, image=self.fundo, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        self.label_fundo.place(x=0-2, y=0)

    def button__Menu(self):
        self.buttonConsult()
        self.buttonRegister()
        self.exit()

    def buttonConsult(self):
        self.Consult = Button(self.__menu, text="Consultar",width=15, bg="#3b3b3b", fg="white", font=("Arial Black",10),command=self.abrir_consulta)
        self.Consult.place(x=317, y=150)

    def buttonRegister(self):
        self.register = Button(self.__menu, text="Cadastrar", width=15, bg="#3b3b3b", fg="white",font=("Arial Black",10),command=self.abrir_cadastro)
        self.register.place(x=317, y=200)


    def exit(self):
        self.sair = Button(self.__menu, text="Sair da aplicação", bg="#3b3b3b", fg="white",font=("Arial Black",8), command= self.__menu.destroy)
        self.sair.place(x=10, y= 465)

    def final(self):
        self.__menu = self.__menu.mainloop()

########################################################################

    def button__Menu2(self):
        self.background2()
        self.buttonBack2()
        self.buttonsearchchoice()
    
    def buttonBack2(self):
        self.back = Button(self.__menu2, text="Voltar", bg="#3b3b3b", fg="white",font=("Arial Black",8), command= self.__menu2.destroy)
        self.back.place(x=10, y= 465)

    def background2(self):
        self.fundo2 = Image.open('Grafics/img/fundo2.png').resize((800,500))
        self.fundo2 = ImageTk.PhotoImage(self.fundo2)
        self.label_fundo2 = Label(self.__menu2, image=self.fundo2, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        self.label_fundo2.place(x=0-2, y=0)

    def abrir_consulta(self):
        self.__menu2 = Toplevel()
        self.__menu2.title('Menu de Consulta')
        self.__menu2.geometry("800x500+282+100")
        self.__menu2.wm_resizable(width=False,height=False)
        self.__menu2.transient(self.__menu)
        self.__menu2.focus_force()
        self.__menu2.grab_set()
        self.button__Menu2()

    def buttonsearchchoice(self):
        self.botaonome = Button(self.__menu2, text="Nome",width=10 ,bg="#3b3b3b", fg="white",font=("Arial Black",8),command=self.datasearchNome)
        self.botaonome.place(x=300, y= 140)
        self.botaocpf = Button(self.__menu2, text="CPF", width=10,bg="#3b3b3b", fg="white",font=("Arial Black",8),command=self.datasearchCPF)
        self.botaocpf.place(x=400, y= 140)

        self.labelradio = Label(self.__menu2, text="Selecione a consulta", bg="#3b3b3b", fg="white",font=("Arial Black",8),width=23)
        self.labelradio.pack()
        self.labelradio.place(x=300, y= 115)

    def entryconsultNome(self):
        self.buscanome = Entry(self.__menu2,bd=4,width=35)
        self.buscanome.place(x=285,y=190)
        self.buttonsearchNome

    def entryconsultCPF(self):
        self.buscacpf = Entry(self.__menu2,bd=4,width=35)
        self.buscacpf.place(x=285,y=190)
        self.buttonsearchCPF

    def buttonsearchNome(self):
        self.pesquisar = Button(self.__menu2, text="Consultar Nome",  width=20,bg="#3b3b3b", fg="white",font=("Arial Black",8), command=self.getdataNome)#responsavel por finalizar a consulta
        self.pesquisar.place(x=310, y= 230)
        self.getdataNome

    def buttonsearchCPF(self):
        self.pesquisar = Button(self.__menu2, text="Consultar CPF",  width=20,bg="#3b3b3b", fg="white",font=("Arial Black",8), command=self.getdataCPF)#responsavel por finalizar a consulta
        self.pesquisar.place(x=310, y= 230)
        self.getdataCPF

    def datasearchCPF(self):
        self.entryconsultCPF()
        self.buttonsearchCPF()
        selection = f"A consulta será feita por CPF"
        self.labelradio.config(text = selection)

    def datasearchNome(self):
        self.entryconsultNome()
        self.buttonsearchNome()
        selection = f"A consulta será feita por Nome"
        self.labelradio.config(text = selection)

    def getdataNome(self):
        nome = self.buscanome.get()
        aux = None
        for key in self.__dic.values():
            for cliente in key.values():
                if cliente == nome:
                    for dados in key.items():
                        print(*dados)
                    aux = key.values()
                    MessageBox.showinfo("Os dados consultados são: ",
                    self.__dic.get(nome))
                    break    
        if aux != None:
            pass               
        else:
            if nome == '':
                MessageBox.showwarning("Os dados consultados são: ",f"Consulta vazia")
            else:
                MessageBox.showerror("Os dados consultados são: ",f"Cadastro de {nome} não localizado")

    
    def getdataCPF(self):
        cpf = self.buscacpf.get()
        aux = None
        for key in self.__dic.values():
            for cliente in key.values():
                if cliente == cpf:
                    for dados in key.items():
                        print(*dados)
                    aux = key.values()
                    MessageBox.showinfo("Os dados consultados são: ",key.items())
                    break    
        if aux != None:
            pass               
        else:
            if cpf == '':
                MessageBox.showwarning("Os dados consultados são: ",f"Consulta vazia")
            else:
                MessageBox.showerror("Os dados consultados são: ",f"Cadastro de {cpf} não localizado")
        print(cpf)
        
########################################################################

    def button__Menu3(self):
        self.background3()
        self.buttonBack3()
        self.cadastrar()


    def buttonBack3(self):
        self.back = Button(self.__menu3, text="Voltar", bg="#3b3b3b", fg="white",font=("Arial Black",8), command= self.__menu3.destroy)
        self.back.place(x=10, y= 465)

    def background3(self):
        self.fundo3 = Image.open('Grafics/img/fundo3.png').resize((800,500))
        self.fundo3 = ImageTk.PhotoImage(self.fundo3)
        self.label_fundo3 = Label(self.__menu3, image=self.fundo3, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        self.label_fundo3.place(x=0-2, y=0)

    def abrir_cadastro(self):
        self.__menu3 = Toplevel()
        self.__menu3.title('Menu de Cadastro')
        self.__menu3.geometry("800x500+282+100")
        self.__menu3.wm_resizable(width=False,height=False)
        self.__menu3.transient(self.__menu)
        self.__menu3.focus_force()
        self.__menu3.grab_set()
        self.button__Menu3()

    def cadastrar(self):
        self.entryName()
        self.entryCPF()
        self.entryDatadeNascimento()
        self.entryGenero()
        self.entryEndereco()
        self.entryemail()
        self.entrytelefone()
        self.choiceplano()
        self.concluir()


    def entryName(self):
        self.cadastrarnome = Button(self.__menu3, text="Nome:",width=8, bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastrarnome.place(x=150, y= 150)
        self.inputnome = Entry(self.__menu3,bd=4,width=50,font=("Arial Black",8))
        self.inputnome.place(x=250, y= 150)
        
    def entryCPF(self):
        self.cadastrarcpf = Button(self.__menu3, text="CPF:",width=8,  bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastrarcpf.place(x=150, y= 185)
        self.inputcpf = Entry(self.__menu3,bd=4,width=50,font=("Arial Black",8))
        self.inputcpf.place(x=250, y= 185)

    def entryDatadeNascimento(self):
        self.cadastrardata = Button(self.__menu3, text="Data de nascimento:",width=15,  bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastrardata.place(x=150, y= 220)
        self.inputdia = Entry(self.__menu3,bd=4,width=6,font=("Arial Black",8))
        self.inputdia.place(x=285, y= 220)
        self.inputmes = Entry(self.__menu3,bd=4,width=6,font=("Arial Black",8))
        self.inputmes.place(x=340, y= 220)
        self.inputano = Entry(self.__menu3,bd=4,width=6,font=("Arial Black",8))
        self.inputano.place(x=395, y= 220)

    def entryGenero(self):
        self.cadastrargenero = Button(self.__menu3, text="Genero:",width=8,  bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastrargenero.place(x=455, y= 220)
        self.inputgenero = Entry(self.__menu3,bd=4,width=9,font=("Arial Black",8))
        self.inputgenero.place(x=535, y= 220)

    def entryEndereco(self):
        self.cadastrarend = Button(self.__menu3, text="Endereco:",width=8,  bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastrarend.place(x=150, y= 255)
        self.inputend = Entry(self.__menu3,bd=4,width=50,font=("Arial Black",8))
        self.inputend.place(x=250, y= 255)
        
    def entryemail(self):
        self.cadastraremail = Button(self.__menu3, text="email:",width=8,  bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastraremail.place(x=150, y= 290)
        self.inputemail = Entry(self.__menu3,bd=4,width=50,font=("Arial Black",8))
        self.inputemail.place(x=250, y= 290)

    def entrytelefone(self):
        self.cadastrartelefone = Button(self.__menu3, text="Telefone:",width=8,  bg="#3b3b3b", fg="white",font=("Arial Black",8))
        self.cadastrartelefone.place(x=150, y= 325)
        self.inputtelefone = Entry(self.__menu3,bd=4,width=50,font=("Arial Black",8))
        self.inputtelefone.place(x=250, y= 325)

    def choiceplano(self):
        self.pegarplano = StringVar()
        R1 = Radiobutton(self.__menu3, text="Prepago", variable=self.pegarplano, value='Prepago',command=self.plano).place(x=270,y=370)
        R2 = Radiobutton(self.__menu3, text="Controle", variable=self.pegarplano, value='Controle',command=self.plano).place(x=350,y=370)
        R3 = Radiobutton(self.__menu3, text="Pospago", variable=self.pegarplano, value='Pospago',command=self.plano).place(x=433,y=370)

    def plano(self):
        self.inputplano = "Você escolheu o plano " + str(self.pegarplano.get())
        self.label3 = Label(self.__menu3,text=self.inputplano,width=29,bg="#3b3b3b",fg="white",font=("Arial Black",8)).place(x=270,y=410)
        print(self.inputplano)
    
    def concluir(self):
        self.finalizar = Button(self.__menu3,text="Concluir Cadastro:",width=29,bg="#3b3b3b", fg="white",font=("Arial Black",8),command=self.getdados)
        self.finalizar.place(x=269, y= 440)

    def getdados(self):
        MessageBox.showinfo(
        'Dados do cadastro',f'''

        Nome:               {self.inputnome.get()}
        CPF:                {self.inputcpf.get()}
        Data de Nascimento: {self.inputdia.get()}/{self.inputmes.get()}/{ self.inputano.get()}
        Genero:             {self.inputgenero.get()}
        Endereco:           {self.inputend.get()}
        Email:              {self.inputemail.get()}
        Telefone:           {self.inputtelefone.get()}
        Plano:              {self.pegarplano.get()}''')


        self.__dic.setdefault(
            [self.inputnome.get()],
            {'Nome': self.inputnome.get(),
             'CPF': self.inputcpf.get(), 
             'Ano': self.inputano.get(), 
             'Mes': self.inputmes.get(), 
             'Dia': self.inputdia.get(), 
             'Genero': self.inputgenero.get()
        })

        print(self.__dic)
        self.__menu3.destroy()

    def getName(self):
        return self.__dic['Nome']

app = Menu()
app.final()

