totalGols = 0
partidasSemGols = 0
partidasComGols = 0

jogador = {'nome': input('Nome:').strip().title(), 'quantPartidas': 0, 'golsPartida': [], 'totalGols': 0}
jogador['quantPartidas'] = int(input('Quant Partidas Disputadas: '))
for i in range(0, jogador['quantPartidas']):
    jogador['golsPartida'].append(int(input(f'{i + 1}º Partida quantidade de Gols: ')))
    if jogador['golsPartida'][i] == 0:
        partidasSemGols += 1
    else:
        totalGols += jogador['golsPartida'][i]
        partidasComGols += 1
print(f'''
------------------------------------------
Nome: {jogador['nome']}
Quant Partidas: {jogador['quantPartidas']}
Acertos em Gols: {(partidasComGols/jogador['quantPartidas'])*100}%
Falhas em Gols: {(partidasSemGols/jogador['quantPartidas'])*100}%
Total Gols: {totalGols}
''')
print(f'O jogador {jogador["nome"]} teve o seguinte desempenho:')
for i in range(0, len(jogador['golsPartida'])):
    print(f'    => Na partida {i + 1}, fez {jogador["golsPartida"][i]} gols')
