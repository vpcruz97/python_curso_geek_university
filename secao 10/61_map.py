"""
Map

Com map, fazemos mapeamento de valores para função.
---------------------------------
import math


def area(r):
    # alcula a área de um ciruclo com raio 'r'
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
# areas = []
# for r in raios:
#     areas.append(area(r))
# print(areas)

# Forma 2: Map
# Map recebe dois parâmetros: primeiro é a funcao, depois o iteravel
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3: Map c/ Lambda
# OBS.: Apos utilizar a funcao map() depois da primeira utilizacao
# ele zera
print(list(map(lambda r: math.pi * (r ** 2), raios)))


# Para fixar - Map
# Temos dados iteraveis:
# dados: a1, a2, ..., an
# Temos uma funcao:
# Funcao: f(x)
# utilizamos a funcao map(f, dados) onde map() mapeara cada elemento dos dados
# e aplicara a funcao
# O Map Object: f(a1), f(a2)..., f(an)
"""
