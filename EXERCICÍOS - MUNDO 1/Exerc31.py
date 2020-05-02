distancia = float(input('Quantos Km tem a sua Viagem: '))

if 0 < distancia <= 200:
    preco = distancia * 0.50
else:
     preco = distancia * 0.45
print(f'A viagem de {distancia} Km\nValor da Viagem é:  {preco:.2f}')