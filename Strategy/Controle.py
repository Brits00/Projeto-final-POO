from TipoPlanos.Iplanos import PlanosInterface

class Controle(PlanosInterface):
    def __init__(self, saldo: float, fatura: bool, adimplente: bool) -> None:
        self.__saldo = saldo
        self.__fatura = fatura 
        self.__adimplente = adimplente

    def get_saldo(self) -> float:
        return self.__saldo
     
    def get_fatura(self) -> bool:
        return self.__fatura
 
    def get_adimplente(self) -> bool: 
        return self.__adimplente