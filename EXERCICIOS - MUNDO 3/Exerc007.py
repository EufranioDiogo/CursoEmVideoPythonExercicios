numeros = list()
flag = 0
maior = menor = 0

for i in range(0, 5):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))
    if flag == 0:
        maior = menor = numeros[i]
        flag = 1
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]

posMaior = ''
posMenor = ''
for i in range(0, 5):
    if numeros[i] == maior:
        posMaior += str(i) + ', '
    elif numeros[i] == menor:
        posMenor += str(i) + ', '
print(f'''
Maior Número: {maior} | Pos: {posMaior}
Menor Número: {menor} | Pos: {posMenor}
''')