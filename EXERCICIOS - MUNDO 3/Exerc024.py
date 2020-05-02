totalGols = 0
partidasSemGols = 0
partidasComGols = 0
jogadores = list()

while True:
    jogador = {'nome': input('Nome: ').strip().title(), 'quantPartidas': int(input('Quant Partidas Disputadas: ')),
               'golsPartida': [], 'totalGols': 0}
    for i in range(0, jogador['quantPartidas']):
        jogador['golsPartida'].append(int(input(f'{i + 1}º Partida quantidade de Gols: ')))
        if jogador['golsPartida'][i] == 0:
            partidasSemGols += 1
        else:
            totalGols += jogador['golsPartida'][i]
            partidasComGols += 1

    acertosGols = (partidasComGols / jogador['quantPartidas']) * 100
    falhasGols = (partidasSemGols / jogador['quantPartidas']) * 100
    jogador['acertosGols'] = acertosGols
    jogador['falhasGols'] = falhasGols
    jogadores.append(jogador.copy())

    opcao = input('Deseja continuar?(Sim | Não) ').strip().lower()[0]
    if opcao == 'n':
        break

while True:
    print('-'*40)
    print('Digite -1 para sair')
    cod = int(input('Mostrar dados de qual Jogador? '))
    if cod == -1:
        break
    if cod < 0 or cod > len(jogadores):
        print('Este cod não existe')
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}')
    for i in range(0, len(jogadores[cod]['golsPartida'])):
        print(f'    => Na partida {i + 1}, fez {jogadores[cod]["golsPartida"][i]} gols')
