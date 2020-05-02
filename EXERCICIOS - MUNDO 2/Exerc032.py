numero = 0

while True:
    numero = int(input('Digite o número que pretende ver a tabuada(Digite -1 para PARAR): '))
    if numero < 0:
        break
    for i in range(1, 13):
        print(f'{i} x {numero} = {i * numero}')
    print('')
print('Programa terminado')
