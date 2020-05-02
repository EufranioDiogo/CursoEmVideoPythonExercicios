salario = float(input('Digite o seu sálario: '))

if salario > 1250.00:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print(f'''
Valor de Aumento: {aumento:.2f} AOA
Valor do Sálario Anterior: {salario:.2f} AOA
Valor do Novo Sálario: {salario + aumento:.2f} AOA''')
