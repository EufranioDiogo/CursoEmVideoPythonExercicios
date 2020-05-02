nota1 = float(input('Digite o valor da 1ª nota: '))
nota2 = float(input('Digite o valor da 2ª nota: '))

if -1 < nota1 < 11 and -1 < nota2 < 11:
    media = (nota1 + nota2) / 2

    if media < 5.0:
        print(f'Aluno REPROVADO com: {media:.2f} Vals')
    elif media < 6.9:
        print(f'Aluno em RECUPERAÇÃO com: {media:.2f} Vals')
    else:
        print(f'Aluno APROVADO com: {media:.2f} Vals')
else:
    print('As notas inseridas são invalidas!')
