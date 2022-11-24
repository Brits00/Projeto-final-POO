from TipoPlanos.Iplanos import PlanosInterface

class Pospago(PlanosInterface):
    def __init__(self, saldo: int, fatura: int, adimplente: bool) -> None:
        self.__saldo = saldo
        self.__fatura = fatura
        self.__adimplente = adimplente
    
    def get_saldo(self) -> float:
        return self.__saldo
        
    def get_fatura(self) -> int:
        return self.__fatura
            
    def get_adimplente(self) -> bool:
        return  self.__adimplente
