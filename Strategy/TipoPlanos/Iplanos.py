from abc import ABC, abstractmethod
from abc import ABC, abstractmethod, abstractclassmethod


class PlanosInterface(ABC):

    @abstractmethod
    def get_saldo(self) -> float:
        pass

    @abstractmethod
    def get_fatura(self) -> float:
        pass 
    
    @abstractmethod
    def get_adimplente(self) -> bool:
        pass

#import sys; print(sys.path)