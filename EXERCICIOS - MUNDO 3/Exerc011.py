numeros = list()

while True:
    numeros.append(int(input(f'Digite o {len(numeros)+1}º número: ')))
    opcao = input('Deseja continuar? (S/N): ').strip().lower()[0]
    if opcao == 'n':
        break

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'''
-------------------------------------------------
Lista Original: {numeros}
Lista de Números Pares: {pares}
Lista de Números Impares: {impares}
-------------------------------------------------''')
