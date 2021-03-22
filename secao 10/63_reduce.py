"""
Reduce

OBS.: A partir do Python3+ a funcao reduce() nao e mais integrada (built-in).
Agora temos que importar e utilizar a funcao através do modulo 'functools'
"""

# Exemplo
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
multi = lambda x, y:  x + y
res = reduce(multi, dados)
print(res)