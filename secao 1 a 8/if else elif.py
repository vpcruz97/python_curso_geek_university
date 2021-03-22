"""
Estruturas condicionais:
if, else, elif
"""

idade = -2

if idade >= 0 and idade < 18:
    print(f'Menor de idade {idade}')
elif idade < 0:
    print(f'Voce não nasceu ainda')
else:
    print(f'Menor de idade')
