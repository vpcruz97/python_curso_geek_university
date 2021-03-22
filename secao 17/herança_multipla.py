"""
POO -> Herança multipla

Possibilidade de herança de múltiplas classes

# Ex1: Multiderivacao Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Direta(Base1, Base2, Base3):
    pass


# Ex2: Mutiderivacao Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Indireta(Base3):
    pass


"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


    def retornar_nome(self):
        return f'{self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{Animal.retornar_nome(self)} esta nadando'


class Terreste(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{Animal.retornar_nome(self)} está andando'


class Pinguim(Aquatico, Terreste):

    def __init__(self, nome):
        super().__init__(nome)

    def acoes(self):
        acoes = f'{super().nadar()}, {super().andar()}'
        return acoes

    def cumprimentar(self):
        return super(Pinguim, self).cumprimentar()


