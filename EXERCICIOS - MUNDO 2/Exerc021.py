nomes = []
sexos = []
idades = []
quantFemeninos = 0

for i in range(0, 4):
    nomes.append(input(f'Digite o nome da {i+1}º Pessoa: ').strip().title())
    sexos.append(input(f'Digite o sexo da {i+1}º Pessoa: ').lower().strip()[0])

    while sexos[i] != 'f' and sexos[i] != 'm':
        sexos[i] = input(f'Digite o sexo da {i+1}º Pessoa: ').lower().strip()[0]

    idades.append(int(input(f'Digite a idade da {i+1}º Pessoa: ')))

    if sexos[i] == 'f' and idades[i] < 20:
        quantFemeninos += 1

mediaIdade = 0

for idade in idades:
    mediaIdade += idade

mediaIdade /= 4

maiorIdade = idades[0]
indiceMaiorIdade = 0

for idade in (1, len(idades)):
    if idades[i] > maiorIdade:
        indiceMaiorIdade = i

nomeMaisVelho = nomes[indiceMaiorIdade]


print(f'''
---------------------------------
Média de Idade: {mediaIdade:.2f}
Nome do Mais Velho: {nomeMaisVelho}
Quant. Mulheres Menor que 20: {quantFemeninos}
---------------------------------''')
