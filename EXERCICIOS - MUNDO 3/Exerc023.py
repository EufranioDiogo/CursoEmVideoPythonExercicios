pessoa = {'nome': '', 'sexo': '', 'idade': 0}
pessoas = list()
mulheres = []
pessoasIdadeAcimaMedia = []
somaIdades = 0

while True:
    print('Para terminar o programa digite -1 em Nome')
    pessoa['nome'] = input('Nome: ').strip().title()
    if pessoa['nome'] == '-1':
        break
    pessoa['sexo'] = input('Sexo(Masculino | Femenino): ').strip().lower()[0]
    while pessoa['sexo'] != 'm' and pessoa['sexo'] != 'f':
        pessoa['sexo'] = input('Sexo(Masculino | Femenino): ').strip().lower()[0]

    pessoa['idade'] = int(input('Idade: '))

    while pessoa['idade'] < 0 or pessoa['idade'] > 100:
        pessoa['idade'] = int(input('Idade: '))

    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa.copy())
    somaIdades += pessoa['idade']

    pessoas.append(pessoa.copy())

mediaIdades = somaIdades / len(pessoas)

for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > mediaIdades:
        pessoasIdadeAcimaMedia.append(pessoas[i])

print(f'''
-----------------------------------------------------------
Quant Pessoas: {len(pessoas)}
Média de Idade: {mediaIdades}
Lista Mulheres: {mulheres}
Pessoas Acima da Média de Idade: {pessoasIdadeAcimaMedia}
-----------------------------------------------------------''')
