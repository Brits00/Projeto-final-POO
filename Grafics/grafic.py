from tkinter import *

def prin():
    texto = 1 + 1
    downbotao['text'] = texto + 1

janela = Tk()
janela.title('Menu inicial')
janela.geometry('1368x768+0+0')

img_fundo = PhotoImage(file=r'C:\Users\jjvbs\Documents\GitHub\Projeto-final-POO\Grafics\fundo.png')

# Consulta = Label(janela, text = "Consultar cadastro")
# Consulta.grid(column = 0,row = 0)

botao = Button(janela, text='Clique aqui', command=prin)#'COLOQUE AQUI O GET(importante: não use parenteses)')
botao.grid(column=0,row=1)

downbotao = Label(janela,text='')
downbotao.grid(column=0, row=2)

lab_fundo = Label(janela, image=img_fundo)
lab_fundo.grid(column=0,row=1)


janela.mainloop()


