from math import ceil

quantDias = int(input('Quantos dias o carro foi alugado: '))
quantKm = ceil(float(input('Quantos Km foram rodados: ')))

precoDias = quantDias * 60
precoKm = quantKm * 0.15

total = precoDias + precoKm
print(f'O alugue do carro equivale a: {total:.2f} AOA\nPreço pelos dias Alugados: {precoDias:.2f} AOA\nPreço pelos Km rodadaos: {precoKm:.2f} AOA')
