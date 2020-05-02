ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é um ano bissexto!')
elif ano % 100 == 0 and ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto!')