from Cliente import *
from datetime import date,datetime


#str(input('Digite o nome do Cliente: '))
#Instanciando Cliente.
p1 = Cliente('João',"XXX",'82999841529',1998,2,25,'M','jjvbsilva@hotmail.com','Rua Sapotizeiro')

#Obtendo dados do cliente:

print(f'''
{p1.getNome()}
{p1.getCPF()}
{p1.getTelefone()}
{p1.getDatadeNascimento()}
{p1.getGenero()}
{p1.getEmail()}
{p1.getEndereco()}'''
)

#print(p1.getNome())
#print(p1.cpf)
#print(p1.telefone)
#print(date.today() - p1.data)
#print(f"{p1.getNome()} tem {p1.calcularIdade(date(p1.getAno(),p1.getMes(),p1.getDia()))} anos de idade.")

#p1.setNome('Bel')


#print(f"{p1.getNome()} tem {p1.calcularIdade(date(2001,6,20))} anos de idade.")


