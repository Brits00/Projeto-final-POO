from TipoPlanos.Iplanos import PlanosInterface

class Prepago(PlanosInterface):

    def __init__(self,saldo: float) -> None:
        self.__saldo = saldo

    def get_saldo(self) -> float:
        return self.__saldo