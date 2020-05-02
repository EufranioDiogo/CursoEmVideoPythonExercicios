idades = [int(input('Idade 1: ')), int(input('Idade 2: ')), int(input('Idade 3: ')), int(input('Idade 4: ')), int(input('Idade 5: '))]

maiores = menores = 0


for idade in idades:
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f'Quant Maiores de Idades: {maiores}\nQuant Menores de Idades: {menores}')
