"""
List Comprehension

- Utilizando List Comprehension nos podemos gerar novas listas com dados processados e partir
de outro iteravel

# Sintaxe da List Comprehension
[ dado for in iteravel ]

Para entender melhor o que está acontecendo, devevemos dividir a expressão em duas partes:
 - Primeira parte: for numero in numeros
 - Segunda parte: numero * 10

 res = [numero/2 for numero in numeros]
print(res)


def funcao(valor):
    return valor*valor


res = [funcao(numero) for numero in numeros]
print(res)

# List comprehensions versos loop
# Loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrado = numero * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)

# List Comprehensions
print(
    [numero * 2 for numero in numeros]
)

"""
# Outros Exemplos
# Exemplo 1
nome = 'Geek University'
print(
    [cada_letra.upper() for cada_letra in nome]
)

# Exemplo 2
amigos = [
    'maria', 'julia', 'pedro', 'guilherme', 'vanessa'
]
print(
    [
        amigo.capitalize() for amigo in amigos
    ]
)

# Exemplo 3
print(
    [
        numero * 3 for numero in range(1, 10)
    ]
)

# Exemplo 4
print(
    [
        bool(valor) for valor in [0, [], '', True, 3.14]
    ]
)

# Exemplo 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

