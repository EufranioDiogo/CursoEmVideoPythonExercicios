pesos = [int(input('Peso 1: ')), int(input('Peso 2: ')), int(input('Peso 3: ')), int(input('Peso 4: ')), int(input('Peso 5: '))]
maiorPeso = menorPeso = pesos[0]

for peso in pesos:
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso

print(f'Maior Peso: {maiorPeso}\nMenor Peso: {menorPeso}')
