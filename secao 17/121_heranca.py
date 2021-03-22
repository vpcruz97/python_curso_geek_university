"""
Heranca
"""
class Pessoa:

    def __index__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__index__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__index__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__matricula}: {super().nome_completo()}'


cliente1 = Cliente('Vitor', 'Cruz', '123.456.789-10', 5000)
funcionario1 = Funcionario('Creed', 'Jhonson', '987.654.321-99', 1234)

print(funcionario1.nome_completo())
