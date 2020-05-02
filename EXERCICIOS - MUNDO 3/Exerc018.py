aluno = ['', 0, 0, '']
listaAlunos = []

while True:
    print(f'{len(listaAlunos) + 1}º Aluno')
    aluno[0] = input('Digite o nome: ').strip().title()
    aluno[1] = float(input(f'Nota 1: '))
    aluno[2] = float(input(f'Nota 2: '))

    while aluno[1] < 0 or aluno[1] > 20:
        print('Digite novamente o valor da NOTA 1')
        aluno[1] = float(input(f'Nota 1: '))
    while aluno[2] < 0 or aluno[2] > 20:
        print('Digite novamente o valor da NOTA 2')
        aluno[2] = float(input(f'Nota 2: '))
    if (aluno[1] + aluno[2])/2 > 9:
        aluno[3] = 'APROVADO'
    else:
        aluno[3] = 'REPROVADO'
    listaAlunos.append(aluno[:])

    opcao = input('Deseja continuar a adicionar Alunos? (S/N): ').strip().lower()
    if opcao == 'n':
        break

for aluno in listaAlunos:
    print(f'''
-------------------------------------------------
Nome: {aluno[0]}
Nota 1: {aluno[1]:.2f}
Nota 2: {aluno[2]:.2f}
Média: {(aluno[1] + aluno[2])/2}
Status: {aluno[3]}
------------------------------------------------''')

while True:
    opcao = input('Deseja apresentar um aluno em especifico? Se sim digite o seu número senão digite -1\n: ')
    opcao = int(opcao) - 1

    if opcao > len(listaAlunos) - 1:
        print('ERROR Out of Index')
    elif opcao == -1:
        break
    elif opcao < 0:
        print('Invalid Index')
    else:
        print(f'''
        -------------------------------------------------
        Nome: {listaAlunos[opcao][0]}
        Nota 1: {listaAlunos[opcao][1]:.2f}
        Nota 2: {listaAlunos[opcao][2]:.2f}
        Média: {(listaAlunos[opcao][1] + listaAlunos[opcao][2]) / 2}
        Status: {listaAlunos[opcao][3]}
        ------------------------------------------------''')
