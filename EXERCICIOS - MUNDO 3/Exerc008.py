numeros = list()
i = 1

while True:
    numero = int(input(f'Digite o {i}º número: '))
    if not(numero in numeros):
        numeros.append(numero)
        i += 1
    else:
        print(f'Número {numero} já existente na lista')
    opcao = int(input('Deseja continuar?\n(Sim - 1 | Não - 0): '))
    if opcao == 0:
        break
print(f'Lista de Números Digitados: {sorted(numeros)}')
