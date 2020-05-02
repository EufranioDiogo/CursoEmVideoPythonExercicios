numeros = []

for i in range(0, 5):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))
    for j in range(0, len(numeros)):
        if numeros[i] < numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
            #print(f'Número {aux} adicionado na pos {j}')

print(f'Listagem Já Ordenada: {numeros}')
