"""
Debugging
"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as error:
        return f'Erro: {error}'

print(dividir(4, 7))
