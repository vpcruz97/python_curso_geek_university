"""
try/except/else/finally

Toda entrada de deve ser tratada

# Executado somente se não acontecer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um num: '))
except ValueError:
    print('Voce nao digitou um valor válido')
else:
    print(f'Digitou o numero {num}')
finally:
    print('Executando o finally')
"""
# Exemplo mais complexo

def dividir(a: int, b: int):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        print('Não é possível o numerador por 0(denominador)')


num1 = int(input('Informe o 1o nunero(numerador): '))
num2 = int(input('Informe o 2o numero(denominador): '))
print(dividir(num1, num2))

# Metodo menos comum
# except (ValueError, ZeroDivisionError):
