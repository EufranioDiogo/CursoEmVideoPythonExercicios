matriz = [[], [], []]

for i in range(0, len(matriz)):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

somaPares = 0
somaVals3Coluna = 0
terceiraColuna = ''
flag = 0
maiorValor = 0

for i in range(0, len(matriz)):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if j == 2:
            terceiraColuna += str(matriz[i][j]) + '\n'
            somaVals3Coluna += matriz[i][j]
        if i == 1:
            if flag == 0:
                maiorValor = matriz[i][j]
                flag = 1
            else:
                if matriz[i][j] > maiorValor:
                    maiorValor = matriz[i][j]
        print(f'[ {matriz[i][j]} ]', end=' ')
    print('')

print(f'''
------------------------------------------
Soma de todos os valores pares: {somaPares}
Vals da 3ª coluna: {terceiraColuna}
Soma 3ª Coluna: {somaVals3Coluna}
Maior valor 2ª linha: {maiorValor}''')
