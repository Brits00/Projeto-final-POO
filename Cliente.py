from datetime import date,datetime

class Cliente:
    data_atual = datetime.now().strftime("%D")

    def __init__(self, nome: str, cpf: str, telefone: int, ano: int, mes: int, dia: int, genero: str, email: str, endereco: str) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__ano = ano
        self.__mes = mes
        self.__dia = dia
        self.__genero = genero
        self.__email = email
        self.__endereco = endereco

    
    def calcularIdade(self,birthDate): 
        days_in_year = 365.2425    
        age = int((date.today() - birthDate).days / days_in_year) 
        return age

                    
    #Getter and Setter methods
    #Nome
    def getNome(self):
        return self.__nome

    def setNome(self, nomecliente: str):
        self.__nome = nomecliente

    #CPF
    def getCPF(self):
        return self.__cpf

    def setCPF(self, cpfcliente: str):
        self.__cpf = cpfcliente

    #Telefone
    def getTelefone(self):
        return self.__telefone
    
    def setCPF(self, telefonecliente: str):
        self.__telefone = telefonecliente

    #DIA,MES,ANO
    def getDia(self):
        return self.__dia

    def setDia(self, diacliente: int):
        self.__dia = diacliente

    def getMes(self):
        return self.__mes

    def setMes(self, mescliente: int):
        self.__mes = mescliente
    
    def getAno(self):
        return self.__ano

    def setAno(self, anocliente: int):
        self.__ano = anocliente

    def getDatadeNascimento(self):
        return f'{self.__ano}/{self.__mes}/{self.__dia}'

    def setDatadeNascimento(self, ano: int,mes: int,dia: int):
        self.__ano, self.__mes, self.dia =  ano,mes,dia

    #Genero
    def getGenero(self):
        return self.__genero

    def setAno(self, generocliente: str):
        self.__genero = generocliente

    #Email
    def getEmail(self):
        return self.__email

    def setEmail(self, emailcliente: str):
        self.__email = emailcliente

    #Endereço
    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, enderecocliente: str):
        self.__endereco = enderecocliente
    
    def toString(self):
        return f"{self.__nome} tem {self.calcularIdade(date(self.__ano,self.__mes,self.__dia))} anos de idade."

    

    




          









