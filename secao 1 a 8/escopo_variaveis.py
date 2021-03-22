"""
Escopo de variaveis

Dois cassos de escopo:
1) Variaveis globais:
    -   Variaveis globais são reconhecidas, ou seja, seu escopop compreende, todo o programa
2) Variaveis locais:
    - Variaveis locais são reconhecidas apenas no bloco onde estão declaradas

Python: linguagem de tipagem dinâmica. Tipo inferido automaticamente ao atribuimos valores
É possível também aferir um tipo ao dado
"""
numeroNaoTipado: 1
print(1)

numeroTipado: int = 1
print(numeroTipado)

numero = 42
novo = 0

if numero > 10:
    novo = 0
    novo = numero + 10
    print(novo)

print(novo)

