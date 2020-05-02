numeros = list()

while True:
    numeros.append(int(input(f'Digite o {len(numeros)+1}º número: ')))
    opcao = input('Deseja continuar? (S/N): ').strip().lower()[0]
    if opcao == 'n':
        break

print(f'''
--------------------------------------
Lista em forma Decrescente: {sorted(numeros, reverse=True)}
Quant. Números: {len(numeros)}
Val 5 in Lista de Números: {5 in numeros}''')
