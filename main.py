from cliente import Cliente
from pessoa import Pessoa
from Grafics.menu import *



#Instanciando Cliente.
p1 = Pessoa(app.dic['Nome'],app.dic['CPF'],app.dic['Ano'],app.dic['Mes'],app.dic['Dia'],app.dic['Genero'],app.dic['Endereco'])
    
c1 = Cliente(p1.getNome(),p1.getCPF(),
            p1.getAno(),p1.getMes(),p1.getDia(),
            p1.getGenero(),p1.getEndereco(),
            app.dic['Telefone'],app.dic['Email'])
#Obtendo dados do cliente:

print(f'''
Obtendo dados do Cliente

{c1.getNome()}
{c1.getCPF()}
{c1.getAno()}/{p1.getMes()}/{p1.getDia()}
{c1.getGenero()}
{c1.getEndereco()}
{c1.getTelefone()}
{c1.getEmail()}
''')



