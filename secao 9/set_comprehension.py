"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""

# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)  # {1, 2, 3, 4, 5, 6}

# Outro exemplo
numeros = {x ** 2 for x in range(11)}
print(numeros) # {0, 1, 64, 4, 36, 100, 9, 16, 49, 81, 25}

# Outro exemplo
numeros = {x: x ** 2 for x in range(11)}
print(numeros)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(type(numeros))  # <class 'dict'>

letras = {letra for letra in 'Geek University'}
print(letras)  # {' ', 'r', 'i', 'k', 'U', 'e', 'n', 'v', 'y', 'G', 't', 's'}
