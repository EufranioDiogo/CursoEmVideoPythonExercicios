numero = int(input('Digite o número que pretende calcular o factorial: '))
fat = 1
print(f'{numero}! = ', end='')
for i in range(numero, 1, -1):
    print(f'{i}', end=' x ')
    fat *= i
print(f'1', end=f' = {fat}')
