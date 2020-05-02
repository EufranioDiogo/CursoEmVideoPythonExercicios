numero = 0
soma = 0
maior = menor = 0
flag = 0
opcao = 1
quantNumeros = 0

while opcao != 0:
    numero = int(input(f'Digite {quantNumeros + 1}º número: '))

    if flag == 0:
        maior = menor = numero
        flag = 1

    if flag == 1:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    soma += numero
    quantNumeros += 1
    opcao = int(input('''Deseja continuar?
    1 - Sim
    0 - Não
    : '''))

media = soma / quantNumeros
print(f'Soma: {soma}\nMédia: {media:.2f}\nQuant. Números: {quantNumeros}')
