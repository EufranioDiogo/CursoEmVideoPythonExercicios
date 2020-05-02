from datetime import date

anoActual = date.today().year
pessoa = {'nome': '', 'idade': 0, 'carteiraTrabalho': ''}

pessoa['nome'] = input('Digite o seu nome: ').strip().title()
pessoa['idade'] = anoActual - int(input('Digite o seu ano de Nascimento: '))
pessoa['carteiraTrabalho'] = int(input('Digite os anos da Carteira de Trabalho: '))

if pessoa['carteiraTrabalho'] != 0:
    pessoa['anoContratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salário: '))
    pessoa['anoAposentadoria'] = pessoa['idade'] + 35 - (anoActual - pessoa['anoContratacao'])


for k, v in pessoa.items():
    print(f'{k}: {v}')


#print(f'''
#Nome: {pessoa["nome"]}
#Idade: {pessoa["idade"]}
#Carteira de Trabalho: {pessoa["carteiraTrabalho"]}''')

#if pessoa['carteiraTrabalho'] != 0:
#    print(f'''Ano de Contratação: {pessoa['anoContratacao']}
#Salário: {pessoa['salario']:.2f}
#Ano de Aposentadoria: {pessoa['anoAposentadoria']}
#''')
