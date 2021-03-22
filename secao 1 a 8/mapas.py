"""
Mapas -> Conhecidos em Python como Dicionarios
Dicionarios em Python são representados por chaves

# Interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# acessando as chaves
for chave in receita.keys():
    print(receita[chave])

# acessando os valores
for chave in receita.values():
    print(chave)

# Desempacotamento de dicionarios
for chave, valor in receita.items():
    print(f'chave={chave}, valor={valor}')
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Soma*, Valor Máximo*, Valor Minimo*, Tamanho
# Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))