num1 = float(input('Digite o 1º Número: '))
maior = menor = num1
num2 = float(input('Digite o 2º Número: '))
if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2
num3 = float(input('Digite o 3º Número: '))
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print(f'''
Maior Número: {maior}
Menor Número: {menor}
---------------------''')