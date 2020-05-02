quant50 = 0
quant20 = 0
quant10 = 0
quant1 = 0
valSacado = 0

while True:
    valSacado = int(input('Quanto pretende sacar?\n: '))
    while valSacado <= 0:
        valSacado = int(input('Valor Inválido!\nQuanto pretende sacar?\n: '))
    if valSacado > 50:
        quant50 = valSacado // 50
        valSacado = valSacado - (quant50*50)
    if valSacado > 20:
        quant20 = valSacado // 20
        valSacado = valSacado - (quant20 * 20)
    if valSacado > 10:
        quant10 = valSacado // 10
        valSacado = valSacado - (quant10 * 10)
    quant1 = valSacado
    print(f'''
---------------------------------------------------
Quant 50: {quant50} 
Quant 20: {quant20}
Quant 10: {quant10}
Quant 1:  {quant1}
--------------------------------------------------''')
    opcao = input('Deseja continuar?(s/n): ').strip().lower()
    if opcao == 'n':
        break
print('FINAL')