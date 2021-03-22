"""
Any e All
-------------------------------

all() -> Retorna True se todos os elementos do iteravel forem verdadeiros, ou ainda
se o iteravel esta vazio
"""
# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # Retorna Falso devido ao 0 estar incluso
print(all([-1, 1, 2, 3, 4]))  # Retorna Verdadeiro devido ao não ter o valor 0