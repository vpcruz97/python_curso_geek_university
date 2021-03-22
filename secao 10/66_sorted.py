"""
Sorted

sorted() serve para ordernar iteraveis.
sort() modifica a lista
sorted() retorna uma nova lista, tupla
sorted() sempre retorna uma lista com os elementos ordenados

# Exemplo
numeros = 6, 1, 8, 2
print(sorted(numeros))
print(numeros)

numeros = [6, 1, 8, 2]

# Adicionando parâmentros ao sorted()
print(sorted(numeros, reverse=True))  # Ordenação do Máx ao Min
print(numeros)

usuarios = [
            {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
            {'username': 'carla', 'tweets': ['Eu amo meu gato']},
            {'username': 'jeff', 'tweets': []},
            {'username': 'bob123', 'tweets': []},
            {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
            {'username': 'gall', 'tweets': []}
]

# Ordenacao pelo username: ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))
# Ordenacao por numero de tweets
print(sorted(usuarios, key=lambda usuario: usuario['tweets'].__len__(), reverse=True))
"""

musicas = [
    {'titulo': 'Musica 1', 'tocou': 3},
    {'titulo': 'Musica 2', 'tocou': 2},
    {'titulo': 'Musica 3', 'tocou': 4},
    {'titulo': 'Musica 4', 'tocou': 32}
]

print("Menos tocada: ",
    sorted(
        musicas, key=lambda musica: musica['tocou']
    )
)

print("Mais tocada: ",
    sorted(
        musicas, key=lambda musica: musica['tocou'], reverse=True
    )
)