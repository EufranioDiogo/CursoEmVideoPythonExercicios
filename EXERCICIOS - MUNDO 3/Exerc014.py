listaNumeros = []
numerosPares = []
numerosImpares = []

listaNumeros.append(numerosPares)
listaNumeros.append(numerosImpares)

for i in range(0, 7):
    numero = int(input(f'Digite o {i + 1}º número: '))
    if numero % 2 == 0:
        listaNumeros[0].append(numero)
    else:
        listaNumeros[1].append(numero)
listaNumeros[0] = sorted(listaNumeros[0])
listaNumeros[1] = sorted(listaNumeros[1])
print(f'''
Lista Generica: {listaNumeros}
Números Pares: {numerosPares}
Números Impares: {numerosImpares}
''')