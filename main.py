from Cliente import *


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
    {p1.getEndereco()}
    {p1.toString()}'''
)




