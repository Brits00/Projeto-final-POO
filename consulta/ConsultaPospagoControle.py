class Consulta:
    def __init__(self, nome: str, cpf: str, saldo: float, fatura:float , adimplente: bool) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__fatura = fatura 
        self.__adimplente = adimplente
        

@property 
def consultar_saldo(self):
    return self.__saldo

@property 
def nome(self):
    return self.__nome


@nome.setter 
def nome(self, nome):
    return self.__nome

@property
def cpf (self):
    return self.__cpf 

@cpf.setter
def cpf(self,cpf):
    return self.__cpf

def __str__(self):
    return f'O saldo do cliente {self.__nome} é de {self.__saldo} reais'

def consulta_fatura(self):
    return self.__fatura 

    
def __str__(self):
    f'A fatura do cliente {self.__nome} é de {self.__fatura}'

sim = 'Sim'
nao = 'Não'
situação_fatura = str(input('A fatura do cliente está em débito?'))
print(situação_fatura)
if situação_fatura == 'Sim':
    adimplente = False
    f'O cliente não está adimplente'

elif situação_fatura == "Não":
    adimplente = True
    f'O cliente está adimplente'

def consultar_adimplencia(self):
    return adimplente 
    
def __str__(self):
    f'O cliente {self.__nome} está adimplente? {adimplente}'












