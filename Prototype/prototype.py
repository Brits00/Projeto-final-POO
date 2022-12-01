import copy 


class Telefone:
    def __init__(self, nome: str, cpf: str, telefone: int):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        

    def __str__(self):
        return f'{self.nome}, {self.cpf}, {self.telefone}'

class Numero:
    def __init__(self, cpf = 0, telefone = 0):
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return f'{self.cpf}, {self.telefone}'


class NumeroTelefone:
    numero_principal = Numero('',Telefone('João', '14567890841' , '82999786731'))
    numero_secundario = Numero('',Telefone('João', '14567890841' , '8299654312358'))

    @staticmethod
    def __new_numero(proto, nome, cpf, telefone):
        result = copy.deepcopy(proto)
        result.nome = nome
        result.cpf = cpf
        result.telefone.telefone = telefone
        return result

    @staticmethod
    def new_numero_principal_e(nome, cpf, telefone):
        return NumeroTelefone.__new_numero(
            NumeroTelefone.numero_principal, nome, cpf, telefone
            )

    @staticmethod
    def new_numero_secundario_e(nome, cpf, telefone):
        return NumeroTelefone.__new_numero(
            NumeroTelefone.numero_secundario, nome, cpf, telefone
            )


if __name__ == '__main__':
    joão = NumeroTelefone.new_numero_principal_e('João', 14567890841, '82997567841')
    joão2 = NumeroTelefone.new_numero_secundario_e('João', 14567890841, '82987117656')
    print(joão)
    print(joão2)