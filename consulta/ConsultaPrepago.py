class Saldo:
    def __init__(self, nome, cpf, saldo):
        self.__nome = nome 
        self.__cpf = cpf
        self.__saldo = saldo

@property
def consultar_saldo(self):
    return self.__saldo 

@property 
def nome(self):
    return self.__nome 


@nome.setter
def nome(self, nome):
    self.__nome = nome

@property
def cpf(self):
    return self.__cpf

@cpf.setter
def cpf (self, cpf):
    self.__cpf = cpf

def __str__(self):
    return f'O saldo do cliente {self.__nome} é de {self.__saldo} reais'






        