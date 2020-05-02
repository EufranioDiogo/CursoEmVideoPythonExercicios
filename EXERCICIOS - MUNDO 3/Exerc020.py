from random import randint

jogadas = {'1º Jogadar': 0, '2º Jogadar': 0, '3º Jogadar': 0, '4º Jogadar': 0}

for i in jogadas.keys():
    jogadas[i] = randint(0, 7)
    print(f'{i} teve {jogadas[i]}')
jogadas = sorted(list(jogadas.items()))
print(jogadas)
