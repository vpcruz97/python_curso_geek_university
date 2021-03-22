"""
Dictionary Comprehension

Sintaxe:
{chave:valor for valor in iteravel}

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numeros = {1, 2, 3, 4, 5}
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

chaves = 'abcde'
valores = [1, 2, 3 , 4, 5]
mistura = {chaves[index]: valores[index] for index in range(0, len(chaves))}
print(mistura)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
"""

# Exemplo com logica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)  # {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}
