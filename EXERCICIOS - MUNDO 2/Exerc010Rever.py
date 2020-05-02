from random import randint
from time import sleep

print('''
PEDRA PAPEL TESOURA
FAZ A SUA ESCOLHA

Pedra   ~ 1
Papel   ~ 2
Tesoura ~ 3
: ''')
print('Sou o seu adversário vou escolher dê-me uma das opções')
computador = randint(1, 4)
homem = input('Digite a sua jogada: ')

if homem == '1' or homem == '2' or homem == '3':
    if computador == '1':
        if homem == '1':
            print('Empate')
        elif homem == '2':
            print('Vencêu')
        elif homem == '3':
            print('Perdeu')
    elif computador == '2':
        if homem == '2':
            print('Empate')
        elif homem == '3':
            print('Vencêu')
        elif homem == '1':
            print('Perdeu')
    if computador == '3':
        if homem == '3':
            print('Empate')
        elif homem == '1':
            print('Vencêu')
        elif homem == '2':
            print('Perdeu')
