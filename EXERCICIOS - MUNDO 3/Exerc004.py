numeros = (int(input('1º Número: ')), int(input('2º Número: ')), int(input('3º Número: ')), int(input('4º Número: ')))
quantNumeros9 = 0
numerosPares = ''

for numero in numeros:
    if numero == 9:
        quantNumeros9 += 1
    if numero % 2 == 0:
        numerosPares += numero + ', '

firstIndexOf3 = numeros.index(3)

print(f'''
----------------------------------
Quant. Vezes Apareceu o Valor: {quantNumeros9}
Primeiro número 3: {firstIndexOf3}
Números Pares Encontrados: {numerosPares}''')
