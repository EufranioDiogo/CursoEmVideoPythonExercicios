def gerarValor():
    from random import randint

    return randint(0, 101)


from time import sleep

quantTentativas = 0
quantVitorias = 0

print('Vou chutar um número de 1 á 100 e você deve adivinhar, aceita Jogar? (Sim - S | Não - N)')
opcao = input(': ').strip().lower()[0]


while opcao != 's' and opcao != 'n':
    print('Digite novamente a sua resposta! Sim ou Não?')
    opcao = input(': ').strip().lower()[0]


if opcao == 'n':
    print('Foi bom enquanto durou a nossa conversa que pena :-(')
else:
    print('Pensando...')
    sleep(0.5)
    numeroSorteado = gerarValor()

    while True:
        print('-'*40)
        numeroLancado = int(input(f'''
************************************************************
                Digite -1 para terminar!
-------------------------------------------------------------
Quant. Tentativas: {quantTentativas}
Quant. Victorias: {quantVitorias}
------------------------------------------------------------
Digite um número inteiro positivo qualquer de 0 á 100:'''))
        if numeroLancado == -1:
            print('Jogo terminado por sua opção')
            break
        if numeroSorteado > numeroLancado:
            print(f'Você chutou muito em baixo aumenta mais relativamente')
        elif numeroSorteado < numeroLancado:
            print(f'Você lançou muito alto deve baixar um pouquinho')
        else:
            quantVitorias += 1
            print('*+'*20)
            print(f'Parabéns você acertou! Legal você é o Cara')
            print('*+*'*20)
            opcao = input('Dejesa continuar a jogar mas será sorteado outro valor de 1 á 100?(Sim | Não)').strip().lower()[0]
            while opcao != 's' and opcao != 'n':
                opcao = input('Dejesa continuar a jogar mas será sorteado outro valor de 1 á 100?(Sim | Não)').strip().lower()[0]

            if opcao == 'n':
                break
            numeroSorteado = gerarValor()

        quantTentativas += 1
