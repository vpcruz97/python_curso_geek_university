"""
Dicionarios, tambpem conhecidos como mapas

Dicionarios são coleções tipo chave/valor
Dicionarios sao representaaos por {}

# Forma 1: Comum
estados = {
    'sp': 'Sao Paulo',
    'ba': 'Bahia',
    'rj': 'Rio de Janeiro'
}

print(estados)
print(type(estados))

# Forma 2: Menos comum
estados = dict(
    sp='Sao Paulo',
    ba='Bahia',
    rj='Rio de Janeiro'
)
print(estados)
print(type(estados))

#  Acessando elementos
#  Forma 1: Acessando via chave, tal como lista/tupla
#  Chaves inexistentes geram KeyError
print(estados['sp'])
print(estados['ba'])

#  Forma 2: Acessando(chaves) via get: Recomendado
print("Valor de SP: ", estados.get('sp'))
print("Valor de MG: ", estados.get('mg'))  # Retorna 'None' quando não identifica

amazonas = estados.get('am')
if amazonas:
    print('Encontrado')
else:
    print('Nao encontrado')


amazonas = estados.get('am', 'Nao encontrado')  # Pode ser passado 2o argumento para tratativa em caso de None
print(f'{amazonas}')

#  Adicionar elementos em um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}

#  Forma 1:
#  Mais comum
receita['abr'] = 350

#  Forma 2:
novoDado = {'mai': 500}
receita.update(novoDado)
print(receita)

#  Atualizando dados em um dicionario
#  Forma 1:
receita['mai'] = 550
print(receita)

#  Forma 2:
receita.update({'mai': 600})
print(receita)

#  Conclusão:
#  A forma de adicionar e atualizar dados é a mesma
#  Em dicionarios não é podemos ter chaves repetidas

# Forma 1 (Comum):
# Sempre devemos informar a chave. Quando o elemento não é encontrado, retorna erro
receita.pop('mar') # Retorna o valor da chave
print(receita)

#  Forma 2 (Menos comum):
del receita['fev']  # del: deletar | Deleta a chave e o valor, sem retornar o valor da chave, como pop()
print(receita)

"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Remover dados de um dicionario
