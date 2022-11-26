from datetime import date
from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf: str, ano: int, mes: int, dia: int, genero: str, endereco: str, telefone: int, email: str) -> None:
        super().__init__(nome,cpf,ano,mes,dia,genero,endereco)
        self.__telefone = telefone
        self.__email = email
    
    def calcularIdade(self,birthDate): 
        days_in_year = 365.2425    
        age = int((date.today() - birthDate).days / days_in_year) 
        return age
         
    #Getter and Setter methods
    #Telefone
    def getTelefone(self):
        return self.__telefone
    
    def setTelefone(self, telefone: int):
        self.__telefone = telefone

    #Email
    def getEmail(self):
        return self.__email

    def setEmail(self, email: str):
        self.__email = email

      
    def toString(self):
        return f"{self.__nome} tem {self.calcularIdade(date(self.__ano,self.__mes,self.__dia))} anos de idade."

    

    




          









