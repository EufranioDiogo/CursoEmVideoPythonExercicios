aluno = {'nome': ' '.join(input('Digite o nome do aluno: ').strip().title().split()), 'media': 0.0, 'situacao': ''}

aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
while aluno['media'] < 0 or aluno['media'] > 10:
    aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'REPROVADO'
else:
    aluno['situacao'] = 'APROVADO'
print(f'Nome: {aluno["nome"]}\nMédia: {aluno["media"]:.2f}\nSituação: {aluno["situacao"]}')
