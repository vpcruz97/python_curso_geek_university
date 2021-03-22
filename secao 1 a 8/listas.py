"""
Listas
Listas em Python funciona como vetores/matrizes (arrays) em outas lingaugens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado;

Dinâmico: Não possui tamanho fixo
    Ou seja, podemos criar a lista e simplesmente ir adicionando elementos
    Qualquer tipo de dado
    Listas são representadas por []
-----------------------------------------------------------------------------------------------

# Checando se elemento está contido em uma lista
num = 7
if num in lista1:
    print(f'Encontrei o número {num}')
else:
    print(f'Nao encontrei o numero {num}')

#  Podemos facilmente ordenar uma lista
lista1.sort() #  Sort permite ordenação da lista
print(lista1)

#   Podemos facilmente contar o numero de ocorrências de um valor em uma lista
print(lista1.count(1)) #  Conta o numero de elemntos passado como argumento
print(lista5.count('e'))

#  Adicionar elementos em listas
#  OBS.: Para adicionar elementos em listas, utilizamos a funcao append
#  OBS.: Só poderá ser adicionar um elemento por vez
#  lista1.append(12,34,56) // Erro
lista1.append(42) #  Elemento adicionado
print(lista1)
lista1.append([8, 3, 1]) # Adicinando uma lista dentro de outra lista
print(lista1)

if [8, 3, 1] in lista1:
    print('Lista encontrada')
else:
    print('Lista não encontrada')

lista1.extend([123,44,67]) #  Insere cada elemento na lista de forma adicional
print(lista1)

#  Podemos inserir um elemento na lista informando a posição do indice
#  OBS.: Nao substitui o valor inicial. O mesmo será deslocado para a direita da lista.
#  print(lista1[2])
lista1.insert(2, 'Novo valor')
print(lista1)

#  Podemos facilmente juntar duas listas
# lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

#  Reversão de listas
# lista1.reverse()
# lista2.reverse()

# Também permite a invesão de listas
print(lista1[::-1])
print(lista2[::-1])

#  Copiar uma lista
lista6 = lista2.copy() #  Permite a cópia de uma lista
print(lista6)

#  Retorna o número de elementos contidos na lista
print(len(lista1))

#  Removendo o último elemento de uma lista
#  OBS.: pop() não somente remove o últimmo elemento, mas o retorna
lista5.pop()
print(lista5)

#  Podemos remover um elemento pelo indice
#  Os elementos a direita deste indice serão deslocados p/ esquerda
#  Se não houver elemento no indice informado, haverá um erro
lista5.pop(2)
print(lista5)

#  Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

#  Podemos facilmente repetir elementos em uma lista
nova = [1,2,3]
print(nova)
nova *= 3
print(nova)

#  Podemos facilmente converter uma string para uma lista
#  Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#  Exemplo 2
curso = 'Programação,em,Python:,Essencial'
curso = curso.split(',')
print(curso)

#  Convertendo uma lista em string
lista6 = ['Programação','em', 'Python','Essencial']

#  Abaixo estamos concatenando cada elemento com espaço para gerar uma string
curso = ' '.join(lista6)
print(curso)

#  Iterando sobre listas
#  Exemplo 1 -> Utilizando o for
soma = 0
for elemento in lista4:
    soma += elemento
print(soma)

#  Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione produto ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


#  Encontrar um indice de um elemento na lista3
#  OBS.: caso não possua elemento na lista, retornará erro
#  Metodo .index() retorna o primeiro elemento da lista conforme argumento passado
print(lista1.index(7))

#  Buscando a partir de um range
#  Se não encontra o indice, gera erro
print(lista1.index(5, 4))

"""
lista1 = [1, 99, 4, 27, 15, 5, 3, 1, 7, 7, 7, 44, 42, 27]
lista2 = ['G','e','e','k',' ','U','n','i','v','e','r','s','i','t','y']
lista3 = []
lista4 = list(range(11)) #  Insere elementos do range dentro da lista
lista5 = list('Geek University') #  Insere individualmente cada elemento em uma lista
