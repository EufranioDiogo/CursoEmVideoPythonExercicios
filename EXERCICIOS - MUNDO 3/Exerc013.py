pessoa = ['', 0.0]
listaPessoas = []
flag = 0
maiorPeso = 0.0
menorPeso = 0.0

while True:
    pessoa[0] = input(f'Digite o nome da {len(listaPessoas) + 1}: ')
    pessoa[1] = float(input(f'Digite o peso da {len(listaPessoas) + 1}: '))
    listaPessoas.append(pessoa)
    if flag == 0:
        maiorPeso = menorPeso = pessoa[1]
        flag = 1
    else:
        if listaPessoas[len(listaPessoas) - 1][1] > maiorPeso:
            maiorPeso = listaPessoas[len(listaPessoas) - 1][1]
        if listaPessoas[len(listaPessoas) - 1][1] < menorPeso:
            menorPeso = listaPessoas[len(listaPessoas) - 1][1]
    opcao = input('Deseja continuar? (S/N): ').strip().lower()[0]
    if opcao == 'n':
        break

pesadas = []
leves = []

for pessoa in listaPessoas:
    if pessoa[1] == maiorPeso:
        pesadas.append(pessoa)
    if pessoa[1] == menorPeso:
        leves.append(pessoa)
print(f'''
--------------------------------
Quant. Pessoas: {len(listaPessoas)}
Pessoas Mais Pessadas: {pesadas}
Pessoas Mais Leves: {leves}
-----------------------------------''')