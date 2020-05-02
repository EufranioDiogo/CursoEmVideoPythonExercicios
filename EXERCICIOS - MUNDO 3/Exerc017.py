from random import randint

numerosGerados = []
listaDeNumerosGerados = []
cont = 0

quantJogos = int(input('Digite a quantidade jogos vais jogar: '))

while quantJogos < 0 or quantJogos > 6:
    quantJogos = int(input('Digite a quantidade jogos vais jogar: '))

for i in range(0, quantJogos):
    while True:
        numero = randint(0, 61)
        if not(numero in numerosGerados):
            numerosGerados.append(numero)
            cont += 1
        if cont == 6:
            break
    cont = 0
    listaDeNumerosGerados.append(sorted(numerosGerados[:]))
    numerosGerados.clear()

for i in range(0, len(listaDeNumerosGerados)):
    print(f'{i+1}º Lista de Tentativas: {listaDeNumerosGerados[i]}')

