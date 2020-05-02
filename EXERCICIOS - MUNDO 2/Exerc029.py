soma = 0
quantNumeros = 0
numero = 1

while numero != 999:
    numero = int(input('Digite um número: '))
    soma += numero
    quantNumeros += 1

print(f'Soma: {soma}\nQuant. Números: {quantNumeros}')
