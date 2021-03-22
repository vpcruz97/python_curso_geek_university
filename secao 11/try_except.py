"""
O block try/except
"""
# Exemplo - Tratando erro especifico
try:
    len(ss)
except NameError as error:
    print(error, ': Você está utilizando uma função inexistente')
except TypeError as error:
    print(error.__hash__())
finally:
    print('Continuidade de execucao')