"""
Tipo Float

Tipo real, decimal

Casas decimais
OBS: O separador de casas decimais na programação é o ponto
"""

# Certo
valor = 1.44
print(valor)
print(type(valor)) # Tipo float

# É possível
valor1, valor2 = 1.00, 44.00 # Dupla atribuação
print(valor1, valor2)
print(type(valor1), type(valor2))

# Conversão de float para int
"""
Ao converter valores float para inteiros, perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
var = 5j
print(5j)
print(type(5j))