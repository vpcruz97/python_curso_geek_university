"""
Operador Walrus

variavel := expressao

nome = 'Geek University'
print(nome)

print(nome := 'Geek University')
"""
# Python 3.7
# cesta = []
# fruta: str = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append('Informe a fruta: ')
#     fruta: str = input('Informe a fruta: ')

cesta = []
while (fruta := input('Informe a fruta: ') != 'jaca'):
    cesta.append(fruta)