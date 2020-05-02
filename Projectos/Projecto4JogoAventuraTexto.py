print('''
Gabriel, desde o momento do seu nascimento foi condenado a uma doença que tem uma difícil cura
e ao mesmo tempo muita cara, e seus familiares não têm capacidade financeira para fazer o
tratamento e poder salvar a vida de Gabriel com apenas 7 meses de vida!''')

resposta = input('''
Existem 2 possíveis saidas para está situação:
a)Deixar Gabriel com a doença.
b)Procurar uma forma de o salvar.

Digite a ou b: ''').strip().lower()[0]

if resposta == 'a':
    print(f'''
5 meses depois Gabriel acaba morrendo quase fazendo 1 ano, sua mãe de tanta dor suicida-se deixando assim seus 7 irmãos 
orfãos o pai não aguenta tanta responsabilidade e sentimentos obscuros entrega-se ao alcolismo capaz de passar o dia 
todo bebendo e deixando seus filhos com fome!

Você decidiu muito mau a culpa toda foi sua!''')
elif resposta == 'b':
    print('''
Pai de Gabriel sai para as ruas e começa a pedir ajuda, iluminado encontra 3 pessoas dispostas a ajudar:
a)Senhora Idosa se disponibiliza que pode pagar o tratamento, mas Gabriel deve ficar com ela durante o tratamento.
b)Jovem Empresario comovido, oferece pagar o tratamento mas pai de Gabriel tinha de trabalhar na sua empresa sem 
remuneração salarial durante 10 anos.
c)ONG de ajuda humanitária oferece pagar, mas a ONG após o tratamento tinha de levar Gabriel para ver se está tudo bem

Qual destas opções escolhes: a, b ou c''')
    resposta = input(': ').strip().lower()[0]

    if resposta == 'a':
        print(f'''
Senhora cumpre com o pagamento do tratamento, mas durante o período de tratamento que a senhora cuidava de Gabriel
ela tinha relações sexuais com Gabriel de apenas 7 meses, e por vezes o privava de alimentação por ter chorado muito a 
noite passada após as relações sexuais!

Quando a oferta é demais até o Santo desconfia!
''')
    elif resposta == 'b':
        print(f'''Pai de Grabiel Aceitou a proposta mas não sabia nuque estava a se colocar exactamente por não ter 
        lido correctamente a parte com letras pequenas do contrato, no contrato que Pai de Grabiel dizia que:

Eu pai de Grabiel Digo que: "Gabriel após o tratamento deveria, se manter em sua casa, mas seu pai seria obrigado a 
trabalhar pela empresa durante a sua vida, senão a guarda de Gabriel seria passada para o proprietário da empresa"

Muita atenção antes de assinar qualquer tipo de contrato.''')
    elif resposta == 'c':
        print('''A ONG cumpre com o combinado sem problemas alguns e faz uma proposta para pai e mãe de Grabiel.
        
Enquanto Gabriel está em tratamento porque não se mudarem para um país com maior qualidade de vida toda a família
 e com empregos já Garantidos, mas já não poderiam voltar para a sua terra de origem
 
 Depois de uma longa discussão entre o Pai e Mãe de Gabriel o Pai diz para a mãe tomar a Decisão:''')
        resposta = input('a) Sim, sair do país de origem e nunca mais voltar\nb) Não, permanecer no país de origem e não sair\na ou b:: ').strip().lower()[0]
        if resposta == 'a':
            print('''Após a partida da família de Grabiel, é chegada a noticia que a casa onde eles vivam com toda a família materna de Grabiel
sofreu um incêndio e que infelizmente todos morreram(Pais da mãe de Gabriel, irmãos e irmãs, inclusive sobrinhos primos de Gabriel):

Angela mãe de Gabriel de tanto sofrimento e dor entra em uma depressão severa e o Pai de Gabriel tem de tomar uma Decisão:
A ONG se apercebe de tal facto e diz que pode ajudar Angela mas será necessário parar o Tratamento de Gabriel

a)Parar o tratamento de Gabriel.
b)Continuar com o tratamento de Gabriel.''')
            resposta = input(': ').strip().lower()[0]
            if resposta in 'ab':
                if resposta == 'a':
                    print('''O tratamento de Gabriel é parado e o de Angela começa o seu tratamento
                    , 2 semanas se passaram e a recuperação de Angela tem sido bastante rapida e boa,
                    mas Grabiel a cada dia que passa seu estado piora e o seu pai foi alertado que 
                    Gabriel apenas possui 1 mês e meio devido o agravamento do seu quadro clinico
                    
                    Manuel pai de Gabriel se sente culpado por tal e fica a pensar em uma possível solução
                    e ele tem 2 novas opções:
                    
                    a)Envolver-se com uns caras que disseram que podiam ajudar na continuação do tratamento mas ele tinha de fazer um serviço(não especificando qual)
                    b)Ajoelhar e orar para DEUS porque realmente está complicado''')
                    resposta = input(': ').strip().lower()[0]

                    if resposta == 'a':
                        print('''Os caras que disseram que podiam ajudar Gabriel realmente ajudaram, e Manuel se sente extremamente agradecido
                        e pede muito obrigado por tal, mas eles dizem que Manuel ainda tinha de fazer um favor para eles que seria transportar
                        1.5 KG de Liamba para algumas localidades e estava tudo acertado!''')
                        resposta = input('''
                        a)Manuel recusa e diz que não se mete nisso seria melhorar acharem outro serviço
                        b)Manuel aceita e vai cumprir a missão
                        a ou b: ''').strip().lower()[0]
                        if resposta == 'a':
                            print('''Os caras deixam pai de Gabriel ir, 6 meses após do que tinha acontecido Gabriel e Angela estão recuperados
                            e a família se encontra feliz, Manuel sai para comprar gelados e um ramo de flores para Angela por tanta felicidade
                            quando Manuel volta encontra Gabriel e Angela mortos, não se sabe o que aconteceu e imagina a dor deste homem
                            o que você agora fara?''')
                            resposta = input('''
                            a) Ir a busca dos culpados e vingar-se
                            b) Chorar e se conformar de tal acto
                            c) Também matar-se
                            a, b ou c: ''').strip().lower()[0]
                            if resposta == 'a':
                                print("""Você vai busca dos culpados em uma perseguição sem limites, encontra alguns dos integrantes da Gangue dos
                                assassinos e obriga eles a dizerem quem foram os culpados da morte de Gabriel e Angela, eles se recusam e Manuel rapidamente
                                saca uma arma e dispara contra um dos elementos que foi mortalmente alvejado, o outro fica extremamente amedrontado e decidi
                                falar sobre o assunto e lhe é dito que os assassinos de Gabriel e Angela são dois elementos do Grupo de nomes: Ruan e El Chaco
                                e que após o ocorrido Ruan foi para Espanha e El Chaco foi para San Petersburgo e que ele já não soube de nada após a partida dos
                                dois elementos.
                                """)
                                resposta = input("""
                                Embarcar na jornada da Vingança?
                                a) Sim
                                b) Não
                                : """).strip().lower()[0]
                                if resposta == 'a':
                                    print('')
                                elif resposta == 'b':
                                    print('')
                                else:
                                    print('')
                            elif resposta == 'b':
                                print("""Você passa por uma longa jornada de tristeza profunda, onde seu coração não aguenta tanto sofrimento e acabe 
                                por secumbir depois de 2 meses!""")
                            else:
                                print("""Você continua se culpando pelo ocorrido, mas não tem coragem de se matar por isso acaba vivendo com a dor até 
                                o fim dos seus dias sem nunca mais conseguir se recompor!""")
                        elif resposta == 'b':
                            print('''Depois de ter cumprido a missão em 7 bairros faltava apenas 1 para Manuel terminar o serviço
                            neste mesmo bairro havia uma confusão de Gangs e Policiais, Manuel foi pego pela policia e revistado
                            e é encontrado com Liamba e de imediato um processo judicial começa após 3 semanas Manuel estava em uma
                            das prisões mais perigosas do mundo, e era abusado sexualmente Manuel adquiri o vírus do VIH e morre 2 meses
                            após, mãe de Gabriel ouve a notícia e agrava seu estado e Gabriel sem entender também é afectado pelo sofrimento
                            de sua mãe e eles acabam ficando desamparados e sem rumos em uma terra que não é sua!''')
                    elif resposta == 'b':
                        print('''Deus é pai e não é padastro! 
                        Manuel ganha uma oportunidade de emprego magnifica e graças a Deus ele é admitido e consegue pagar o pagamento do tratamento
                        de Gabriel e a família continua feliz graças a DEUS!
                        ''')
                elif resposta == 'b':
                    print(''''O tratamento de Gabriel continua e Angela encontra-se em depressão''')
                print('\n')
                print('='*20)
                resposta = input('Deseja continuar com a História? (Sim | Não)').strip().lower()[0]
                if resposta == 'n':
                    print('Bye Bye, foi bom enquanto durou')
                elif resposta == 's':
                    print("""Angela entra em estado de depressão nunca antes visto e por isto ela acaba ficando com""")