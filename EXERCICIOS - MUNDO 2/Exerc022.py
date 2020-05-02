sexo = 'l'

while sexo != 'f' and sexo != 'm':
    print('Digite o seu sexo: ', end='')
    sexo = input().strip().lower()[0]

print(f'Sexo Correcto: {sexo.upper()}')
