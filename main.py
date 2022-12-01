from cliente import Cliente
from pessoa import Pessoa
from Grafics.menu import * #Para usar a interface gráfica é só remover o comentário 
from Prototype.prototype import *


#Instanciando Pessoa com Singleton
p1 = Pessoa('João','XXX',1998,2,25,'M','Rua Sapotizeiro')
p2 = Pessoa('bel','yyy',2001,6,20,'F','AV Elvira')

print(p1.getNome(),p1.getCPF(),p1.getAno(),p1.getMes(),p1.getDia(),p1.getGenero(),p1.getEndereco())
print(p2.getNome(),p2.getCPF(),p2.getAno(),p2.getMes(),p2.getDia(),p2.getGenero(),p2.getEndereco())


#Instanciar o Cliente com Strategy
# c1 = Cliente(p1.getNome(),p1.getCPF(),p1.getAno(),p1.getMes(),p1.getDia(),p1.getGenero(),p1.getEndereco(),'829999999','Joao@gmail.com','PrePago')
# print(c1.getPlano())
# print(c1.getSaldopre())

c2 = Cliente(p1.getNome(),p1.getCPF(),p1.getAno(),p1.getMes(),p1.getDia(),p1.getGenero(),p1.getEndereco(),'829999999','Joao@gmail.com','Controle')
print(c2.getPlano())
print(c2.getSaldoControle())
print(c2.getAdimplente())



#Instanciando um novo cadastro com prototype.
pr1 = NumeroTelefone.new_numero_principal_e('João', 14567890841, '82997567841')
print(pr1)




