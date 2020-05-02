equipes = ('Petro de Luanda', '1º de Agosto', 'Académica do Lobito', 'Libolo', 'Desportivo da Huíla', 'Bravos do Maquis',
           'Sagrada Esperança', 'Interclube', 'Sporting de Cabinda', 'Wiliete', 'Cuando Cubango', 'Caála',
           'Ferroviário do Huambo', 'Progresso', 'Santa Rita', '1º de Maio Benguela', 'Barcelona', 'Real Madrid', 'Juventos',
           'Manchester')

print(f'''TOP 5: {equipes[:6]}
Ultimos 4 colocados:  {equipes[16:]}
Ordem Alfabética: {sorted(equipes)}
Posição da Académica do Lobito: {equipes.index('Académica do Lobito')}''')
