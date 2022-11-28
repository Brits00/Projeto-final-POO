from cliente import Cliente
from pessoa import Pessoa
from Grafics.menu import *

#Instanciando Cliente.
p1 = Pessoa(app.getdata(),"XXX",1998,2,25,'M','Rua Sapotizeiro')
    
c1 = Cliente(p1.getNome(),p1.getCPF(),
            p1.getAno(),p1.getMes(),p1.getDia(),
            p1.getGenero(),p1.getEndereco(),
            '82999841529','joao@gmail.com')
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



