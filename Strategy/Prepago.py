from Strategy.TipoPlanos.Iplanos import PlanosInterface

class Prepago(PlanosInterface):

    def __init__(self,saldo: int) -> None:
        self.__saldo = saldo

    def get_saldo(self) -> int:
        return self.__saldo

    def get_adimplente(self) -> bool:
        return super().get_adimplente()

    def get_fatura(self) -> float:
        return super().get_fatura()

pre = Prepago(10)