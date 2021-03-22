"""
Ranges:
- Precisamos conhecer loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops

Ranges são utiilziados para gerar sequencias numericas, nao de forma aleartoria
mas sim, de maneira especificada

Formas gerais:

# Forma 1
range(valor_de_parada)
OBS.: valor_de_parada não inclusa (inicio padrao 0, e passo de 1 em 1)
for num in range(11):
    print(num)

# Forma 2
range(valorInicio, valorParada)
for num in range(5, 11):
    print(num)

# Forma 3
OBS.: passo é especificado
for num in range(0, 11, 2):
    print(num)

# Forma 4
range(valorInverso, valorParda, passo)

"""

for num in range(10, -1, -1):
    print(num, end=" ")


