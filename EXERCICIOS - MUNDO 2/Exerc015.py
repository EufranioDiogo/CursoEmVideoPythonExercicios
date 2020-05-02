numeros = list()
soma = 0

numeros.append(int(input('Digite o 1º Número: ')))
numeros.append(int(input('Digite o 2º Número: ')))
numeros.append(int(input('Digite o 3º Número: ')))
numeros.append(int(input('Digite o 4º Número: ')))
numeros.append(int(input('Digite o 5º Número: ')))
numeros.append(int(input('Digite o 6º Número: ')))

for i in range(0, len(numeros)):
    soma += numeros[i]

if soma % 2 == 0:
    print('Soma: '+soma)

