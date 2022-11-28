from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk


class Menu:
    def __init__(self) -> None:
        self.menu = Tk()
        self.title = self.menu.title("Menu Inicial")
        self.iconbitmap = self.menu.iconbitmap(default='Grafics\img\logo.ico')
        self.geometry = self.menu.geometry("800x500+282+100")
        self.size = self.menu.wm_resizable(width=False,height=False)

        self.background()
        self.buttonMenu()


    def background(self):
        self.fundo = Image.open('Grafics/img/fundo.png').resize((800,500))
        self.fundo = ImageTk.PhotoImage(self.fundo)
        self.label_fundo = Label(self.menu, image=self.fundo, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        self.label_fundo.place(x=0-2, y=0)

    def buttonMenu(self):
        self.buttonConsult()
        self.buttonRegister()
        self.exit()

    def buttonConsult(self):
        self.Consult = Button(self.menu, text="Consultar",width=15, bg="#3b3b3b", fg="white", font=("Arial Black",10),command=self.abrir_consulta)
        self.Consult.place(x=317, y=150)

    def buttonRegister(self):
        self.register = Button(self.menu, text="Cadastrar", width=15, bg="#3b3b3b", fg="white",font=("Arial Black",10))
        self.register.place(x=317, y=200)


    def exit(self):
        self.sair = Button(self.menu, text="Sair da aplicação", bg="#3b3b3b", fg="white",font=("Arial Black",8), command= self.menu.destroy)
        self.sair.place(x=10, y= 465)
################
    def buttonMenu2(self):
        self.background2()
        self.buttonBack()
        self.buttonsearchchoice()
    
    def buttonBack(self):
        self.back = Button(self.menu2, text="Voltar", bg="#3b3b3b", fg="white",font=("Arial Black",8), command= self.menu2.destroy)
        self.back.place(x=10, y= 465)

    def buttonsearchchoice(self):
        self.var = StringVar()
        R1 = Radiobutton(self.menu2,text="Busca por Nome", bg="#3b3b3b", fg="white",font=("Arial Black",8),width=20, variable=self.var, value='Nome',command=self.datasearch)
        R2 = Radiobutton(self.menu2, text="Busca por CPF", bg="#3b3b3b", fg="white",font=("Arial Black",8),width=20, variable=self.var, value='CPF',command=self.datasearch)
        R1.pack(anchor = W )
        R2.pack(anchor = W )
        R1.place(x=300, y= 140)
        R2.place(x=300, y= 160)
        self.labelradio = Label(self.menu2, text="Selecione a consulta", bg="#3b3b3b", fg="white",font=("Arial Black",8),width=23)
        self.labelradio.pack()
        self.labelradio.place(x=300, y= 115)


    def buttonsearch(self):
        self.pesquisar = Button(self.menu2, text="Consultar",  width=20,bg="#3b3b3b", fg="white",font=("Arial Black",8), command=self.getdata)#responsavel por finalizar a consulta
        self.pesquisar.place(x=310, y= 230)

    def entryconsult(self,width=0):
        self.inputnome = Entry(self.menu2,bd=4,width=35)
        self.inputnome.place(x=285,y=190)
        self.buttonsearch

    def background2(self):
        self.fundo2 = Image.open('Grafics/img/fundo2.png').resize((800,500))
        self.fundo2 = ImageTk.PhotoImage(self.fundo2)
        self.label_fundo2 = Label(self.menu2, image=self.fundo2, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        self.label_fundo2.place(x=0-2, y=0)


    def final(self):
        self.menu = self.menu.mainloop()

    def abrir_consulta(self):
        self.menu2 = Toplevel()
        self.menu2.title('Menu de Consulta')
        self.menu2.geometry("800x500+282+100")
        self.menu2.wm_resizable(width=False,height=False)
        self.menu2.transient(self.menu)
        self.menu2.focus_force()
        self.menu2.grab_set()
        self.buttonMenu2()

        
    def datasearch(self):
        #nome = self.labelradio.get()
        #print(nome)
        self.entryconsult()
        self.buttonsearch()
        opcao = str(self.var.get())
        selection = f"A consulta será feita por {opcao}"
        self.labelradio.config(text = selection)

    
    def getdata(self):
        nome = self.inputnome.get()
        print(nome)
        





    
app = Menu()
app.final()


