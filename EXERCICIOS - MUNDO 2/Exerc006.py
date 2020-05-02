print('-'*32)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-'*32)

nome = ' '.join(input('Digite o nome do Atleta: ').strip().title().split())
idade = int(input('Digite a sua idade: '))

print('\n\nFICHA DO ATLETA:')
print(f'Atleta: {nome}')
if idade > -1:
    if idade < 10:
        print('CATEGORIA: MIRIM')
    elif idade < 15:
        print('CATEGORIA: INFANTIL')
    elif idade < 20:
        print('CATEGORIA: JUNIOR')
    elif idade < 21:
        print('CATEGORIA: SÊNIOR')
    else:
        print('CATEGORIA: MASTER')
else:
    print(f'{idade} é uma idade incorrecta!')
