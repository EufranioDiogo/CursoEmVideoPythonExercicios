from random import randint
quantVictorias = 0

while True:
    print('=-'*10)
    print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^10}')
    print('=-'*10)
    numero = int(input('Diga um valor: '))
    opcao = input('Par ou Impar? [P/I]: ').strip().lower()[0]
    computador = randint(0, 100)
    if (opcao == 'p' and (numero + computador) % 2 == 0) or (opcao == 'i' and (numero + computador) % 2 != 0):
        print('Você VENCEU!')
        quantVictorias += 1
    else:
        print('Você PERDEU!')
        break

print(f'Durante o jogo você venceu {quantVictorias}')
