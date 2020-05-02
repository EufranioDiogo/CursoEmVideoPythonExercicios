idade = 0
sexo = 'undefined'
maiores18 = 0
quantHomens = 0
quantMulheresMaior20 = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo(f/m): ').strip().lower()[0]
    if idade > 18:
        maiores18 += 1
    if sexo == 'm':
        quantHomens += 1
    if sexo == 'f' and idade > 20:
        quantMulheresMaior20 += 1
    opcao = input('Pretende continuar(s/n): ').strip().lower()[0]
    if opcao == 'n':
        break

print(f'''
-------------------------------
Quant. Pessoas Maior 18: {maiores18}
-------------------------------
Quant Homes: {quantHomens}
-------------------------------
Quant Mulheres Maiores que 20: {quantMulheresMaior20}''')
