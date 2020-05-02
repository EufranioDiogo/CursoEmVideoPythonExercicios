from math import sqrt, ceil

num = int(input('Digite um número: '))

raiz = sqrt(num)

print(f'Raiz quadrada de {num} = {ceil(raiz)}(Resultado Arredondado) - {raiz:.2f}(Resultado não Arredondado)')
