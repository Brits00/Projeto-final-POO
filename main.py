from cliente import Cliente
from pessoa import Pessoa
from Grafics.menu import *




#Instanciando Cliente.
p1 = Pessoa(app.getName(),app.getName(),app.getName(),app.getName(),app.getName(),app.getName(),app.getName())
p2 = Pessoa('bel','yyy',2001,6,20,'F','AV Elvira')
print(p1.getNome(),p1.getCPF(),p1.getAno(),p1.getMes(),p1.getDia(),p1.getGenero(),p1.getEndereco())
print(p2.getNome(),p2.getCPF(),p2.getAno(),p2.getMes(),p2.getDia(),p2.getGenero(),p2.getEndereco())
# c1 = Cliente(p1.getNome(),p1.getCPF(),
#             p1.getAno(),p1.getMes(),p1.getDia(),
#             p1.getGenero(),p1.getEndereco(),
#             app.getTelefone(),app.getEmail())
# #Obtendo dados do cliente:

# print(f'''
# Obtendo dados do Cliente

# {c1.getNome()}
# {c1.getCPF()}
# {c1.getAno()}/{p1.getMes()}/{p1.getDia()}
# {c1.getGenero()}
# {c1.getEndereco()}
# {c1.getTelefone()}
# {c1.getEmail()}
# ''')


