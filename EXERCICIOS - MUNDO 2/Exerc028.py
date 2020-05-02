ant = 0
suc = 1
aux = 0
result = f'{ant} → {suc}'
quantTermos = int(input('Digite a quant termos prentede ver: '))

for i in range(3, quantTermos + 1):
    aux = suc
    suc = ant + suc
    ant = aux
    result += ' → ' + str(suc)

print(result)
