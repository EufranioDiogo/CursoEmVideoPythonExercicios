from random import randint

minVal = int(input('Digite o número mínimo que o seu dado pode alcançar: '))
while minVal <= 0:
    print('Valor incorrecto para o valor mínimo deve ser um número positivo maior que 0')
    minVal = int(input('Digite novamente o número mínimo que o seu dado pode alcançar: '))

maxVal = int(input('Digite o número máximo que o seu dado pode alcançar: '))

while maxVal <= minVal:
    print(f'Valor incorrecto para o valor máximo deve ser um número positivo maior que {minVal}')
    maxVal = int(input('Digite novamente o número máximo que o seu dado pode alcançar: '))

print(f'''
----------------------------------------------
O número a ser sorteado é: {randint(minVal, maxVal + 1)}''')
