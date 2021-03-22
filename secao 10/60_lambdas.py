"""
Utilizando Lambdas

Funcoes Lambdas são funções anõnimas, ou, sem nome

# Expressão Lambda
lambda x: 3 * x + 1

# Utilizacao
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' rocky ', 'balboa  '))

# Ordenando nomes pelo sobrenome
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke',
           'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells',
           'Leigh Brackett']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""
