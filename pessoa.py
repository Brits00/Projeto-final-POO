from datetime import date

class MenuSingleton(type):
    __instances = {}
    def __call__(cls, *args,**kwds):
        if cls not in cls.__instances:
            instance = super().__call__(*args,**kwds)
            cls.__instances[cls] = instance

        return cls.__instances[cls]


class Pessoa(metaclass=MenuSingleton):
    def __init__(self, nome: str, cpf: str, ano: int, mes: int, dia: int, genero: str, endereco: str) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__ano = ano
        self.__mes = mes
        self.__dia = dia
        self.__genero = genero
        self.__endereco = endereco
    
    #Idade
    def calcularIdade(self,birthDate): 
        days_in_year = 365.2425    
        age = int((date.today() - birthDate).days / days_in_year) 
        return age

    #Data de nascimento
    def getDatadeNascimento(self):
        return f'{self.__ano}/{self.__mes}/{self.__dia}'

                  
    #Getter and Setter methods
    #Nome
    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    #CPF
    def getCPF(self):
        return self.__cpf

    def setCPF(self, cpf: str):
        self.__cpf = cpf

    #DIA
    def getDia(self):
        return self.__dia

    def setDia(self, dia: int):
        self.__dia = dia

    #MES
    def getMes(self):
        return self.__mes

    def setMes(self, mes: int):
        self.__mes = mes

    #Ano
    def getAno(self):
        return self.__ano

    def setAno(self, ano: int):
        self.__ano = ano
    

    #Genero
    def getGenero(self):
        return self.__genero

    def setGenero(self, genero: str):
        self.__genero = genero

    #Endereço
    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco: str):
        self.__endereco = endereco

   
    def toString(self):
        return f"{self.__nome} tem {self.calcularIdade(date(self.__ano,self.__mes,self.__dia))} anos de idade."

p1 = Pessoa('joao','xxx',1998,2,25,'M','Rua Sapotizeiro')
p2 = Pessoa('bel','yyy',2001,6,20,'F','AV Elvira')

print(p1.getNome())
print(p2.getNome())