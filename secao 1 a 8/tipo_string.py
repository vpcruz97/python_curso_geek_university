"""
Tipo String

Em Python, um dado é consideraro do tipo string sempre que:
 - Estiver entre aspas simples
 - Estiver entre aspas duplas
 - EStiver entre aspas triplas sendo simples
 - EStiver entre aspas triplas sendo duplas
"""
nome = 'Geek University'
print(nome.upper()) # Retorna maisculo
print(nome.lower()) # Retorna minusculo
print(nome.split()) # Retorna uma lista das palavras semparadas
print(nome.split()[1]) # Retorna o recorte do indice
print(nome.split(" ")) # Retorna uma lista das palavras semparadas por um separador como argumento
letras = ['G','e','e','k',' ','U','n','i','v','e','r','s','i','t','y']
print(letras) # Retornando a lista
print(letras[0]) # Retornando um indice como argumento
print(letras[:4]) # Slice(recorte) de string [inicial:final]
print(letras[4:]) # Slice(recorte) de string [inicial:final]
print(letras[:]) # Slice(recorte) de string [inicial:final]
# Observa-se que não é necessario passar os argumentos inicial e final para obter os resultados
print(nome[::-1]) # Inverte as posicoes
print(nome.replace('e', 'u')) # Troca as letras do primeiro argumento pela letra inserida no segundo argumento

texto = "socorram me subino onibus em marrocos"
print(texto)
print(texto[::-1]) # Palindromo