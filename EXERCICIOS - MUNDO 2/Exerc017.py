numero = int(input('Digite um número: '))

flagPrimo = 2

for i in range(2, numero):
    if numero % i == 0:
        flagPrimo += 1
        break
if numero == 1:
    print('O número 1 não é primo')
elif flagPrimo == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')