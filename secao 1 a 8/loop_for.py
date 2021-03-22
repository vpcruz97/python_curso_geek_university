"""
Loop for

Loop -> Estrutura de repeticao
For -> Um tipo de estrutura

Java ex:
for(int i = 0; i < limitador; i++ {
    // code
}

# Python
for item in interavel:
    // code

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplo de iteraveis:
- String
- Lista
- Range

# Exemplo de for: 1
for letra in nome:
    print(letra)

print()
# Exemplo de for: 2
for num in lista:
    print(num)

print()
# Exemplo de for: 3 -> Iteracao sobre range
# range (valorInicial, valorFinal) -> O argumento final alcançará um numero antes do valor final)
for numero in range(1,10):
    print(numero)


for index, letra in enumerate(nome):
    print(f'{index}: {letra}')
OBS.: Quando não precisamos de um valor,podemos descartá-lo utilizando um underline _

n = 30
soma = 0
for n in range(0, n+1):
    print(f'Imprimindo {soma}')
    soma += 5

"""
# nome = 'Geek University'
# lista = [1,3,5,7,9]
# numeros = range(1,10)
#
# for letra in nome:
#     print(letra, end='-')
# "U+1F60D"
for x in range (3+1):
    for num in range(1,11):
        print('\U0001F60D' * num)