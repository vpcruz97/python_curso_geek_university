"""
Tipo Booleano

2 constante: verdadeiro ou falso
Python: True -> verdadeiro // False -> Falso
São escritas em maiúsculo
"""

ativo = True
print(f"Variavel: {ativo}")
print("Tipo: ", type(True))

# Negacao(not)
"""
Fazendo a negacao, se o valor booleano for verdadeiro o resultado sera falso,
se for falso, o resultado será verdadeiro. Ou seja, retorna o contrário
"""
print("Not ativo: ", not ativo)

#Ou (or)
"""
É uma operacao binaria, ou seja,depende de dois valores.
Um dos dois deve ser verdadeiro
"""
print("True or False: ", True or False)

# E (and)
"""
Todos os valores devem voltar verdadeiro para retornar True
"""
print("True and False: ", True and False)
