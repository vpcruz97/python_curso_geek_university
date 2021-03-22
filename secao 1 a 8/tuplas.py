"""
Tuplas (tupla)

Tuplas são bastante parecidas com listas
Existem basicaments duas diferenças básicas:
1 - As tuplas são representadas por parênteses()
2 - As tuplas são imútaveis: isso significa que ao se criar uma tupla ela não pode mudar.
    Toda operação em uma tupla gera uma nova tupla

#  CUIDADO:AS TUPLAS SÃO REPRESENTADAS POR PARENTESES, MAS VEJA:
tupla1 = (1, 2, 3, 4, 5, 6,)
print(type(tupla1))

# Tupla criada sem utilização dos parenteses
tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))

#  CUIDADO: Tuplas com 1 elemento
tupla3 = (4)  # Nao considerara o elemento interno como sendo parte de uma tupla
print(type(tupla3))

tupla4 = (4,)  # Representa tupla por conter o separador ','
print(type(tupla4))

#  Conclui-se que tuplas são definidias pelos parentes e o separador ',' ao lado direito dos elementos

#  Gerando uma tupla a partir de um range
tupla = tuple(range(11))
print(type(tupla))

#  Desempacotamento de tupla
#  Gera erro se colocarmos um numero diferente de elementos para desempacotar
tupla = ('Geek University', 'Programação em Python Essencial',)
escola, curso = tupla
print(escola, ": ", curso)

#  Metodos de Adição e remoçãop de elementos não existem, dado o fato das tuplas são imutaveis

# Soma, valor maximo, valor minimo, tamanho
# OBS.: Calculos gerados apenas se os valores forem inteiros ou reais
# tupla = tuple(range(1,7))
tupla = 1,2,3,4,5,6
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#  Concatenação de tuplas
tupla1 = 1,2,3
tupla2 = 4,5,6
tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 += tupla2 #  Tuplassao imutaveis, mas podemos sobrescrever seu valor
print(tupla1)

# Verificar se determinado elemento esta contido na tupla
tupla = 1,2,3
print(3 in tupla)


tupla = 1,2,3
for n in tupla:
    print( n)

for i, n in enumerate(tupla):
    print(f'{i}) {n} |', end=" ")

#  Contando elementos de uma tupla
tupla = 'a','b','c','d','e','a','b'
print(tupla.count('a'))
print(tupla.count('b'))
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplsa sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses  = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'

# Slicing
# tupla[inicio:fim:passo]
tres = meses[5:8]
print(tres, ": ", type(tres))
"""

