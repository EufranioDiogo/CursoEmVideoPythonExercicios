from random import randint

numeros = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))

maior = menor = numeros[0]

for number in numeros:
    if number > maior:
        maior = number
    if number < menor:
        menor = number

print(f'''
-------------------------------
Números Gerados: {numeros}
Menor: {menor}
Maior: {maior}
-------------------------------''')
