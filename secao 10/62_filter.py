"""
Filter

filter() -> filtra dados de uma determinada colecao

import statistics


# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando media de dados utilizando a funcao mean()
media = statistics.mean(dados)  # 2.183333333333333

# filter() recebe dois parametros: funcao, iteravel
# Apos usado a primeira vez, ele zera
res = filter(lambda x: x > media, dados)
print(list(res))  # [2.7, 4.1, 4.3]

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res = filter(None, paises)
res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

A diferenca entre map() e filter() é
map() -> recebe dis parametros, uma funcao e um iteravel e
retorna um objeto mapeando a funcao para cada elemento iteravel

filter() -> recebe dois parametros, uma funcao e um iteravel e
retorna um objeto filtrando apenas os elemento sde acordo com a funcao
# Exemplo mais complexo

usuarios = [
            {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
            {'username': 'carla', 'tweets': ['Eu amo meu gato']},
            {'username': 'jeff', 'tweets': []},
            {'username': 'bob123', 'tweets': []},
            {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
            {'username': 'gall', 'tweets': []}
]
# Filtrar os usuarios que estao inativos

# Forma 1:
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2:
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""
# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua insturtora é {nome}',
                 filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
