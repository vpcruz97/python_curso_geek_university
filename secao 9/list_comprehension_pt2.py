"""
List comprehension

Podemos adicionar estruturas condicionais logicas
"""

# Exemplos
# 1

numeros = list(range(1, 11))
print(type(numeros))
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refator
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)


# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)