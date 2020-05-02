from math import pow, sqrt, hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

h = sqrt((pow(co, 2) + pow(ca, 2)))

print(f'Valor Hipotenusa = {h}')
