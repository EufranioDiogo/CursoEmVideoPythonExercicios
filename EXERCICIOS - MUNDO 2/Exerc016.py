nTermoPa = int(input('Digite o valor do primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(0, 10):
    print(f'{i+1}º Termo: {nTermoPa}')
    nTermoPa += razao
