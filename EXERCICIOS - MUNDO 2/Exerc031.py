soma = 0
numero = 0
quantNumeros = 0

while True:
    numero = int(input('Digite um número(Digite 999 para parar): '))
    if numero == 999:
        break
    soma += numero
    quantNumeros += 1
print(f'Soma: {soma}\nQuant. Números: {quantNumeros}')
