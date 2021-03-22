"""
Generators
- Tuple Comprehension -> Generators


# Exemplo
nomes = ['Carlos', 'Carla', 'Camila', 'Claudio', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))  # True

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))

print()
print('-' * 10)
print()

# Generators -> Tipo mais performático
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))


# Funcionalidade: Retorna quantidade de bytes em memório do elemento passado
# como parãmetro
from sys import getsizeof

print(getsizeof('Geek'))  # Num. de bytes em mem.: 53

from sys import getsizeof

# Gerando una lista de numeros
# List Comprehension
list_comp = getsizeof([x * 10 for x in range (1000)])

# Set Comprehension
list_set = getsizeof({x * 10 for x in range(1000)})

# Dictionary Comprehension
list_dict = getsizeof({x: x * 10 for x in range(1000)})

# Generator
gen = getsizeof(x * 10 for x in range(1000))

print("Consumo de memoria: ")
print(f'List_comp: {list_comp}')
print(f'List_set: {list_set}')
print(f'List_dict: {list_dict}')
print(f'Generator: {gen}')

"""

# Iterando com Generators
gen = (x * 10 for x in range(10))
print(gen, type(gen), sep=' - ')
print()

for num in gen:
    print(num)
