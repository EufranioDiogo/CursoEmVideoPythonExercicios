from math import ceil

print('=*='*20)
print(f'{"Programa para Calcular Multas":^10}')
print('=*='*20)
velocidade = float(input('Digite a velocidade: '))

if velocidade > 80.0:
    multa = (velocidade - 80) * 7.00
    print(f'''Você foi multado por excesso de velocidade!
    , está a {velocidade - 80} Km\h em Excesso
    , Valor Multa: 7,00 AOA / Km\h em Execesso
    , Valor Total: {ceil(multa):.2f} AOA
    , Boa Viagem e reduza a velocidade!''')
else:
    print('Boa Viagem')