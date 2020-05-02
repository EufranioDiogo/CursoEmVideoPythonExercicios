nTermoPa = int(input('Digite o valor do primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i = 0

while i < 10:
    print(f'{i+1}º Termo: {nTermoPa}')
    nTermoPa += razao
    i += 1
