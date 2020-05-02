from random import randint
from time import sleep

print('Estou pensando em um número!')
sleep(2)
numeroSorteado = randint(0, 6)
print('Já escolhi um número agora tenta advinhar!\n')
numeroDigitado = int(input('Digite o número que acha que o computador sorteou: '))
if numeroSorteado == numeroDigitado:
    print(f'Você acertou!\nAmbos jogamos {numeroDigitado}')
else:
    print(f'Você Errou!\nEu joguei {numeroSorteado}, e você {numeroDigitado}')
print('Final do Jogo')
