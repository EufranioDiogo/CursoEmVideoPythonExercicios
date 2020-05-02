nTermoPa = int(input('Digite o valor do primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
quantTermos = int(input('Digite o número de termos que quer ver: '))
result = ''

while quantTermos <= 0:
    quantTermos = int(input('Digite o número de termos que quer ver: '))

opcao = 1
i = 0

while opcao != 0:
    while i < quantTermos:
        result += f'{i+1}º Termo: {nTermoPa}\n'
        nTermoPa += razao
        i += 1
    opcao = int(input('''
    Deseja continuar a calcular a quant. termos ou mostrar o resultado!
    Mostrar Resultado - 0
    Continuar Calcular - 1
    : '''))

    if opcao == 1:
        i = quantTermos
        quantTermos = int(input('Mais quantos termos quer adicionar: '))
        while quantTermos <= 0:
            quantTermos = int(input('Mais quantos termos quer adicionar: '))
        quantTermos += i

print(result)
