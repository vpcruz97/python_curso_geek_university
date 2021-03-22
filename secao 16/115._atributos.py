"""
POO - Atributos

Atributos -> Representam características do objetos.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância; -> Declarados dentro do metodo construtor
    - Atributos de Classe; -> Declarado diretamente na classe
    - Atributos Dinâmicos -> Criados no runtime

-----------------------------

class Lampada:

    def __init__(self, voltagem, cor):
        # Atributos de instância
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligado(self):
        return self.__ligada

-----------------------------
Atributo publico:
self.atributo

Atributo privado:
self.__atributo

-----------------------------

class Lampada:

    def __init__(self, voltagem, cor):
        # Atributos de instância
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

"""


class Produto:
    # Atributo de classe
    # imposto: float
    imposto = 0.15

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto


p1 = Produto('Item1', 'Mercadoria', 100)
p2 = Produto('Item2', 'Mercadoria', 100)

print(p1.valor)
print(p2.valor)
p1.peso = 5
print(p1.peso)  # Atributo dinâmico

del p1.peso  # Atributo removido

