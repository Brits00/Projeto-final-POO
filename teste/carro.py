from acelerador import Acelerador
from freio import Freio

class Carro:
    def __init__(self):
        self.__acelerador = Acelerador()
        self.freio = Freio()
    
    def pegarAcelerador(self):
        return self.__acelerador