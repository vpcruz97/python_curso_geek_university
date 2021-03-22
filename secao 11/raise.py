"""
Levantando os proprios erros com raise
raise -> lança exceções (Palavra reservada)

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')

    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'brancos')
"""

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')

    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'brancos')