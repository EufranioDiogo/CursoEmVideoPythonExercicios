from random import randint
from time import sleep

numeroSorteado = randint(0, 11)
numeroDigitado = -1
quantPalpites = 0

print('Estou pensando em um número!')
sleep(2)
print('Já escolhi um número agora tenta advinhar!\n')


while numeroDigitado != numeroSorteado:
    numeroDigitado = int(input('Digite o número que acha que o computador sorteou: '))
    if numeroSorteado != numeroDigitado:
        print(f'Você Errou! TENTE NOVAMENTE')
    quantPalpites += 1

print(f'Você acertou!\nAmbos jogamos {numeroDigitado}\nQuant Palpites: {quantPalpites}')
print('Final do Jogo')
