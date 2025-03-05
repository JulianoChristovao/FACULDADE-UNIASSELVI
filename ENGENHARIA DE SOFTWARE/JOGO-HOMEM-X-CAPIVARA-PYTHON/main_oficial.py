import random #importado a biblioteca Randon qua fará o sorteamento das decisões no jogo

"""
ATUALIZAÇÃO 25/03 (Lucas): Arrumei alguns erros de identação do código e arrumei as estruturas sequenciais
que estavam bugando e deixando o código desnecessáriamente complexo, antes dentro dos laços haviam 2 estruturas sequenciais,
agora tá com apenas uma estrutura sequencial dentro de cada laço do while. Na parte da capivara menor a gente já pode pensar no 
combate, tava pensando em criar uma lista de d1 até d20 sendo d1 o ataque fraco e d20 o ataque forte, o código escolheria aleatoriamente
algum dessas 20 opções dentro da lista
"""

'''
ATUALIZAÇÃO 02/04 (Juliano): Fiz a segunda fase (somente a lógica, falta incluir os textos da fase 2). 
Também adicionei imagens de:
 - um guerreiro para a fase 1 e outro para a fase 2
 - uma Capivara mãe para a fase 1 e uma capivara filha para a fase 2
Obs: Falta incluir a história na fase 2, não tenho muita idéia para isto
'''
#--- Opções do Menu ---
print("\nBem vindo ao Jogo: Homem x Capivara!!!\n")
print("Pressione a tecla Q para sair ou a tecla I para iniciar")
menu = input().upper()  # Converte a entrada para maiúsculas para facilitar a comparação
while menu != "Q":
    if menu == "I":
# --- Código do Game ---
        def tabela(elemento, damage):
            damage = 0
            tabela_de_danos = [('e0', +0), ('e1', +1), ('e2', +2), ('e3', +3), ('e4', +4), ('e5', +5),
                       ('e6', +6), ('e7', +7), ('e8', +8), ('e9', +9), ('e10', +10),
                       ('e11', +11), ('e12', +12), ('e13', +13), ('e14', +14), ('e15', +15),
                       ('e16', +16), ('e17', +17), ('e18', +18), ('e19', +19), ('e20', +20)]
            elemento_aleatorio = random.choice(tabela_de_danos)
            elemento, damage = elemento_aleatorio
            return elemento, damage
        print(
            'Depois de muito tempo vivendo sob domínio tirânico das capivaras que ganharam consciência,\n'
            'a resistência humana vive sob constante ameaça do exército capivara que ronda quase todos os lugares,\n'
            'esses rebeldes humanos vivem em bunkers subterrâneos espalhados por vários lugares, eles funcionam como um grande sistema metroviário,\n'
            'mas diferente de um metrô normal, são usados trens manuais, normalmente feito artesanalmente de restos de metais e materiais do gênero, \n'
            'a comida e água é escassa, requerendo cooperação entre as partes rebeldes para se manterem, os coletores, como são chamadas as pessoas que \n'
            'vão para a superfície são essênciais na sobrevivência rebelde, e você é um desses coletores, que foi pego por guardas capivaras enquanto buscava por\n'
            'suprimentos. Você acorda dentro de uma cela suja e com um cheiro forte de sangue, você não sabe de onde vem esse cheiro, mas ouve barulhos de\n'
            'batidas e algo se partindo, você percebe que as condições do portão que prende você são precárias e decide arrombar a fechadura com uns\n'
            'grampos que escondeu no seu calçado, após algumas tentativas, você consegue escapar, tem dois caminhos, direita e esquerda...\n'
        )
 #       while True:

 #           escolha_corredor = input('Para qual lado você vai? ').lower()
        while True:
            escolha_corredor = input('Para qual lado você vai?  - nivel 1: ').lower()

            if escolha_corredor == 'direita':
                print(
                '\nVocê vai pela direita passando pelas outras celas e não vê nada além de corpos em decomposição, no final a sua esquerda você vê uma entrada\n'
                'ao espiar pela entrada você vê uma capivara grande, de uns 2 metros, usando um avental sujo de sangue e na mesa há pedaços de carne fresca,\n'
                'como ela está de costas para você, você pode tentar se esgueirar por trás dela, mas claro que há uma chance de dar errado')
            elif escolha_corredor == 'esquerda':
                print(
                '\nVocê decide ir para a esquerda e encontra uma porta de metal, infelizmente ela está trancada e é impossível de abrir usando grampos\n'
                ' sua única opção é ir pela direita, você vai pela direita passando pelas outras celas e não vê nada além de corpos em decomposição, no final a sua esquerda você vê uma entrada\n'
                'ao espiar pela entrada você vê uma capivara grande, de uns 2 metros, usando um avental sujo de sangue e na mesa há pedaços de carne fresca,\n'
                'como ela está de costas para você, você pode tentar se esgueirar por trás dela, mas claro que há uma chance de dar errado')
            else:
                print('Opção inválida, apenas direita ou esquerda. - nivel 1')
                continue

            print(
            '\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou... - nivel 1')

            while True:
                escolha_açougueiro = input('O que você decide fazer?   - nivel 1: ').lower()
                if escolha_açougueiro == 'esgueirar':
                    luck = random.random()  # Gera um numero entre 0 e 1
                    if luck < 0.3:
                        print(
                        '\nVocê tenta se esgueirar, mas o açougueiro percebe e joga o cutelo em você acertando a sua cabeça te matando instântaneamente - nivel 1')
                        print(
                            '⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              \n'
                            '⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            \n'
                            '⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀         \n'
                            '⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀           \n'
                            '⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀            \n'
                            '⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⠠⣀⠱⠘⣧⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡈⠀⢄⢸⡄             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡀⠃⠘⠂⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⡈⢘⡇             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡑⠣⠰⠀⢁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣸⠁             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠂⡀⢨⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⣾⡄⠀⠀⠀⠀⣀⠐⠁⡴⠁⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡈⡀⢠⣧⣤⣀⣀⡀⢀⡀⠀⠀⢀⣼⣀⠉⡟⠀⢀⡀⠘⢓⣤⡞⠁⠀⠀          \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡁⢁⣸⡏⠀⠀⠀⠀⠁⠀⠉⠉⠁⠹⡟⢢⢱⠀⢸⣷⠶⠻⡇⠀⠀⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠈⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠁⠀⠻⣧⠀⠀⣹⠁⠀⠀⠀             \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠚⠃⣰⣥⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠼⢙⡷⡻⠀⡼⠁⠀⠀⠀⠀            \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠿⡿⠕⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⠉⣹⣷⣟⣚⣁⡼⠁⠀⠀⠀⠀⠀           \n'
                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠁⠀⠀                          \n')
                        break
                    elif luck >= 0.3:
                        print(
                            '\nVocê consegue se esgueirar pelo açougueiro, abrindo a porta você encontra uma escada e decide subir, chegando no andar de cima\n'
                            'você percebe que está numa casa antiga no meio de uma cidade, está de noite e está tudo silencioso, você vê a porta da frente\n'
                            'e tenta abrir, mas está trancada, nisso você ouve passos vindo da direita, você se esconde debaixo de uma mesa e espera, e então \n'
                            'surge uma capivara menor, ela está desarmada e desatenta, parece estar procurando por algo, você pode imobilizar ela\n'
                            'com a sua panela...')

                        while True:
                            capivara_desatenta = input('\nO que você decide fazer? (lutar) - nivel 1: ').lower()
                            if capivara_desatenta == 'lutar':
                                print('\nVocê tenta golpear a capivara, mas ela está usando um tipo de placa por debaixo de sua roupa e acaba não fazendo efeito contra ela,\n'
                                    '\nela joga você pra trás e você não tem outra opção a não ser lutar contra ela... - nivel 1')
                                jogador_vida = 100
                                capivara_vida = 100
                                while jogador_vida > 0 and capivara_vida > 0:
                                    acao = input('Atacar ou passar a vez? - nivel 1: ')
                                    if acao.lower() == 'atacar':
                                        alvo = random.choice(['capivara', 'jogador'])
                                        elemento, damage = tabela(1, 2)
                                        if alvo == 'capivara':
                                            capivara_vida -= damage
                                            print(f'\nVocê atacou a capivara causando {damage} de dano - nivel 1')
                                            print(f' + A capivara possui {capivara_vida} de vida - nivel 1')
                                            print(f' - Você possui {jogador_vida} de vida\n')
                                        else:
                                            jogador_vida -= damage   
                                            print(f'\nA capivara atacou você causando {damage} de dano - nivel 1')
                                            print(f' - Você possui {jogador_vida} de vida - nivel 1')
                                            print(f' + A capivara possui {capivara_vida} de vida - nivel 1\n')
                                    elif acao.lower() == 'passar a vez':
                                        print('Você passou a vez. - nivel 1')
                                    else:
                                        print('Ação inválida. - nivel 1')
                                    if jogador_vida <= 0:
                                        print("\nVOCÊ PERDEU, FIM DE JOGO!!! - nivel 1\n")
                                        print(
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                            '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')  

                                        break
                                    if capivara_vida <= 0:
                                        print("\nVOCÊ VENCEU, VAI PARA A FASE 2!!! - nivel 1")
                                        #vai para a fase 2....
                    
                                        print(
                                            '████████████████████████████████████████████████████`▄▀▀███████████████████▓████\n'
                                            '███████████▓█▌███████████████████████████████████████╙██▄▀██████████████████████\n'
                                            '██████████████████████████████████████▀▀▄██████▄▄▄▄▀██▐███▄▀████████████████████\n'
                                            '████████████████████████████████████▓▄███████████████▄"╙███▌╙████████████████▌██\n'
                                            '██████████████████████████████████▀▄███████████████████ ╙███▄▀██████████████████\n'
                                            '█████████████████████████████████▌▐████████████████████▌j▐███C▀█████████████████\n'
                                            '█████████████████████████████████▌██████████████████████]▌▀███⌐█████████████████\n'
                                            '█████████████████████████████████▌██▀███████████████████]█ ████▐████████████████\n'
                                            '██████████████████████████████████▐███▀██▀▀███████╝▓█▐█▄╙██▐███~████████████████\n'
                                            '█████████████████████████████████╙████▐████% ███╙m███▐██▌▐█.███▀└███████████████\n'
                                            '████████████████████████████████▀▄▓████████▄▄█▄▄▄▄▄▄████]██\▄████m▀█████████████\n'
                                            '█████████████████████████████████╙████████████████████▀█r█⌐╠████ ▄ █████████████\n'
                                            '████████████████████████████████ ███████████████████████⌐█▌▄╙███⌐██ ████████████\n'
                                            '████████████████████████████████ ███████████████████████\█▄▀ ▄▄██▄▌ ████████████\n'
                                            '█████████████████████████████████Γ,█▀,▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀`▐▀█▐███████▐████████████\n'
                                            '█████████████████████████████████ █j██████████████████████ ▌███▀▀▄▄█████████████\n'
                                            '████████████████████████████████ ██▄▀█████████████████████ ██└██▀▀▌████████████\n'
                                            '███████████████████████████████ █████▄▄▀▀▀████████████▀▀▀▀▄▄▀ ▀████▌▐███████████\n'
                                            '██████████████████████████████"▄███████▀▓▀▄▄▐▄▄▄▌╓▐████▌]████"▄█▄▄▄█████████████\n')

                                        # Inicio da fase 2
                                        print('Após vencer a luta contra a capivara, você procura pelos cômodos da casa e encontra\n'
                                              'uma lareira, mas não é uma lareira comum, ela tem uma espécie de corrente\n'
                                              'bem pequena saindo dela, você decide investigar e encontra uma pequena alavanca,\n'
                                              'puxando ela abre do seu lado uma passagem secreta, você decide entrar e encontra uma\n'
                                              'escada e descendo nela, você avista outro corredor, mas esse é maior, e possui duas portas no final\n'
                                              'uma esquerda e outra direita...')
                                        while True:
                                            escolha_corredor = input('Para qual lado você vai? - Nivel 2 : ').lower()

                                            if escolha_corredor == 'direita':
                                                print('Indo pela direita você encontra uma espécie de depósito, parece que guardam enlatados lá, você decide\n'
                                                      'comer alguns desses enlatados e percebe que não há nada de muito interessante lá')
                                            elif escolha_corredor == 'esquerda':
                                                print('Indo pela esquerda você encontra uma sala muito grande, ela é toda branca e o seu piso é feito de quadrados\n'
                                                      'pretos e brancos, nela tem uma capivara muito maior que a que você encontrou lá na prisão, mas essa está usando uma\n'
                                                      'capa vermelha e fica balbuceando algumas coisas no idioma das capivaras, você tem duas opções, esgueirar por ela\n'
                                                      'sem ela perceber ou tentar imobilizá-la...')
                                            else:
                                                print('Opção inválida, apenas direita ou esquerda.')
                                                continue

                                            print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe um golpe na cabeça...')

                                            while True:
                                                escolha_açougueiro = input('O que você decide fazer? Nivel 2: ').lower()
                                                if escolha_açougueiro == 'esgueirar':
                                                    luck = random.random()  # Gera um numero entre 0 e 2
                                                    if luck < 0.8:
                                                        print('\nVocê tentou esgueirar, mas ela percebeu e quebrou a sua mente com o seu poder psíquico, agora você é um\n'
                                                              'zumbificado')
                                                        print(
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                                            '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')                                    
                                                        break
                                                    elif luck >= 0.8:
                                                        print('\nVocê conseguiu esgueirar por ela, entrando em uma sala menor você vê vestígios do que parece ser um\n'
                                                              'ritual, chegando ao centro você sente uma forte dor de cabeça, mas no meio dessa dor você vê com a visão\n'
                                                              'meio embaçada um buraco na parede, você decide entrar nesse buraco por não aguentar mais\n'
                                                              'porém quando você finalmente sai desse buraco você percebe que está no topo de uma montanha\n'
                                                              'com vista para a sua cidade, que está infestada de capivaras, você percebe que não\n'
                                                              'há nada que você ou alguém possa fazer, pois as capivaras conseguiram criar uma poderosa \n'
                                                              'máquina gigantes chamada CapiMachina, é simplesmente o fim da humanidade...')
                                                        #finaliza....
                                                        print('VOCÊ GANHOU!!!!')
                                                        print(                                                                                
                                                            '                     ╢▓█▓                                                       \n'
                                                            ''     
                                                            '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                                            ''
                                                            '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                                            ''
                                                            '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                                            ''
                                                            '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                                            ''
                                                            '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                                            ''
                                                            '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                                            ''
                                                            '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                                            ''
                                                            '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                                            ''
                                                            '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                                            ''
                                                            '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                                            ''
                                                            '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                                            ''
                                                            '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                                            ''
                                                            '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                                            ''
                                                            '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                                            ''
                                                            '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                                            ''
                                                            '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                                            ''
                                                            '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                                            ''
                                                            '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                                            ''
                                                            '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                                            ''
                                                            '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                                            ''
                                                            '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                                            ''
                                                            '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                                            ''
                                                            '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                                            ''
                                                            '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                                            ''
                                                            '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                                            ''
                                                            '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                                        break
                                                    break
                                                elif escolha_açougueiro == 'imobilizar':
                                                    luck = random.random()
                                                    if luck <= 0.7:
                                                        print('\nVocê tenta imobilizar ela mas ela quebra a sua mente, tornando você um zumbificado...')  
                                                        print(
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                                            '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
                                                        break

                                                    elif luck > 0.7:
                                                        print('\nVocê conseguiu imobilizar ela! Mas infelizmente ela não estava carregando nada de muito útil a não\n'
                                                              'ser um pingente que talvez valha alguma coisa no mercado negro, entrando em uma sala menor você vê vestígios do que parece ser um\n'
                                                              'ritual, chegando ao centro você sente uma forte dor de cabeça, mas no meio dessa dor você vê com a visão\n'
                                                              'meio embaçada um buraco na parede, você decide entrar nesse buraco por não aguentar mais\n'
                                                              'porém quando você finalmente sai desse buraco você percebe que está no topo de uma montanha\n'
                                                              'com vista para a sua cidade, que está infestada de capivaras, você percebe que não\n'
                                                              'há nada que você ou alguém possa fazer, pois as capivaras conseguiram criar uma poderosa \n'
                                                              'máquina gigantes chamada CapiMachina, é simplesmente o fim da humanidade...')
                                                        #finaliza....
                                                        print('VOCÊ GANHOU!!!!')
                                                        print(                                                                                
                                                            '                     ╢▓█▓                                                       \n'
                                                            ''     
                                                            '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                                            ''
                                                            '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                                            ''
                                                            '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                                            ''
                                                            '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                                            ''
                                                            '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                                            ''
                                                            '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                                            ''
                                                            '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                                            ''
                                                            '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                                            ''
                                                            '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                                            ''
                                                            '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                                            ''
                                                            '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                                            ''
                                                            '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                                            ''
                                                            '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                                            ''
                                                            '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                                            ''
                                                            '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                                            ''
                                                            '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                                            ''
                                                            '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                                            ''
                                                            '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                                            ''
                                                            '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                                            ''
                                                            '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                                            ''
                                                            '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                                            ''
                                                            '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                                            ''
                                                            '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                                            ''
                                                            '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                                            ''
                                                            '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                                            ''
                                                            '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                                        break

                                                    break
                                            break
                                    #print('Opção inválida, a sua única alternativa é lutar')
                                        break# Fase 1
                                break
                            else:
                                print('Opção inválida, a sua única alternativa é lutar')
                    break


                # FASE 1 IMOBILIZAR
                elif escolha_açougueiro == 'imobilizar':

                    luck = random.random()

                    if luck <= 0.7:
                        print(
                        '\nVocê tenta imobilizar o açougueiro mas ele é muito mais forte que você, jogando você no chão, pegando-lhe pelo pescoço e golpeando-lhe\n'
                        'na barriga, fazendo suas entranhas cair no chão enquanto você morre de dor e agonia')  
                        print(
                                '⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              \n'
                                '⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            \n'
                                '⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀         \n'
                                '⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀           \n'
                                '⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀            \n'
                                '⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⠠⣀⠱⠘⣧⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡈⠀⢄⢸⡄             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡀⠃⠘⠂⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⡈⢘⡇             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡑⠣⠰⠀⢁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣸⠁             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠂⡀⢨⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⣾⡄⠀⠀⠀⠀⣀⠐⠁⡴⠁⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡈⡀⢠⣧⣤⣀⣀⡀⢀⡀⠀⠀⢀⣼⣀⠉⡟⠀⢀⡀⠘⢓⣤⡞⠁⠀⠀          \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡁⢁⣸⡏⠀⠀⠀⠀⠁⠀⠉⠉⠁⠹⡟⢢⢱⠀⢸⣷⠶⠻⡇⠀⠀⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠈⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠁⠀⠻⣧⠀⠀⣹⠁⠀⠀⠀             \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠚⠃⣰⣥⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠼⢙⡷⡻⠀⡼⠁⠀⠀⠀⠀            \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠿⡿⠕⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⠉⣹⣷⣟⣚⣁⡼⠁⠀⠀⠀⠀⠀           \n'
                                '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠁⠀⠀                          \n')
                        break

                    elif luck > 0.7:
                        print(
                        '\nvocê conseguiu imobilizar o açougueiro, assim conseguindo pegar o seu cutelo, você percebe que esse cutelo é muito afiado e é\n'
                        'uma opção perfeita para se defender de inimigos, abrindo a porta ao lado você encontra uma escada e decide subir, chegando no andar de cima\n'
                        'você percebe que está numa casa antiga no meio de uma cidade, está de noite e está tudo silencioso, a iluminação é mais amena, ficando perfeito para se esconder no escuro, você vê a porta da frente\n'
                        'e tenta abrir, mas está trancada, nisso você ouve passos vindo da direita, você se esconde debaixo de uma mesa e espera, e então \n'
                        'surge uma capivara menor, ela está desarmada e desatenta, parece estar procurando por algo, você pode matar ela\n'
                        ' com o seu cutelo...')
                        while True:
                            capivara_desatenta = input('\nO que você decide fazer? (lutar) - nivel 1: ').lower()
                            if capivara_desatenta == 'lutar':
                                print('\nVocê tenta golpear a capivara, mas ela está usando um tipo de placa por debaixo de sua roupa e acaba não fazendo efeito contra ela,\n'
                                    '\nela joga você pra trás e você não tem outra opção a não ser lutar contra ela... - nivel 1')
                                jogador_vida = 100
                                capivara_vida = 100
                                while jogador_vida > 0 and capivara_vida > 0:
                                    acao = input('Atacar ou passar a vez? - nivel 1: ')
                                    if acao.lower() == 'atacar':
                                        alvo = random.choice(['capivara', 'jogador'])
                                        elemento, damage = tabela(1, 2)
                                        if alvo == 'capivara':
                                            capivara_vida -= damage
                                            print(f'\nVocê atacou a capivara causando {damage} de dano - nivel 1')
                                            print(f' + A capivara possui {capivara_vida} de vida - nivel 1')
                                            print(f' - Você possui {jogador_vida} de vida\n')
                                        else:
                                            jogador_vida -= damage   
                                            print(f'\nA capivara atacou você causando {damage} de dano - nivel 1')
                                            print(f' - Você possui {jogador_vida} de vida - nivel 1')
                                            print(f' + A capivara possui {capivara_vida} de vida - nivel 1\n')
                                    elif acao.lower() == 'passar a vez':
                                        print('Você passou a vez. - nivel 1')
                                    else:
                                        print('Ação inválida. - nivel 1')
                                    if jogador_vida <= 0:
                                        print("\nVOCÊ PERDEU, FIM DE JOGO!!! - nivel 1\n")
                                        print(
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                            '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')  
                                        break
                                    if capivara_vida <= 0:
                                        print("\nVOCÊ VENCEU, VAI PARA A FASE 2!!! - nivel 1")
                                        #vai para a fase 2....
                    
                                        print(
                                            '████████████████████████████████████████████████████`▄▀▀███████████████████▓████\n'
                                            '███████████▓█▌███████████████████████████████████████╙██▄▀██████████████████████\n'
                                            '██████████████████████████████████████▀▀▄██████▄▄▄▄▀██▐███▄▀████████████████████\n'
                                            '████████████████████████████████████▓▄███████████████▄"╙███▌╙████████████████▌██\n'
                                            '██████████████████████████████████▀▄███████████████████ ╙███▄▀██████████████████\n'
                                            '█████████████████████████████████▌▐████████████████████▌j▐███C▀█████████████████\n'
                                            '█████████████████████████████████▌██████████████████████]▌▀███⌐█████████████████\n'
                                            '█████████████████████████████████▌██▀███████████████████]█ ████▐████████████████\n'
                                            '██████████████████████████████████▐███▀██▀▀███████╝▓█▐█▄╙██▐███~████████████████\n'
                                            '█████████████████████████████████╙████▐████% ███╙m███▐██▌▐█.███▀└███████████████\n'
                                            '████████████████████████████████▀▄▓████████▄▄█▄▄▄▄▄▄████]██\▄████m▀█████████████\n'
                                            '█████████████████████████████████╙████████████████████▀█r█⌐╠████ ▄ █████████████\n'
                                            '████████████████████████████████ ███████████████████████⌐█▌▄╙███⌐██ ████████████\n'
                                            '████████████████████████████████ ███████████████████████\█▄▀ ▄▄██▄▌ ████████████\n'
                                            '█████████████████████████████████Γ,█▀,▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀`▐▀█▐███████▐████████████\n'
                                            '█████████████████████████████████ █j██████████████████████ ▌███▀▀▄▄█████████████\n'
                                            '████████████████████████████████ ██▄▀█████████████████████ ██└██▀▀▌████████████\n'
                                            '███████████████████████████████ █████▄▄▀▀▀████████████▀▀▀▀▄▄▀ ▀████▌▐███████████\n'
                                            '██████████████████████████████"▄███████▀▓▀▄▄▐▄▄▄▌╓▐████▌]████"▄█▄▄▄█████████████\n')

                                        # Inicio da fase 2
                                        print('Após vencer a luta contra a capivara, você procura pelos cômodos da casa e encontra\n'
                                              'uma lareira, mas não é uma lareira comum, ela tem uma espécie de corrente\n'
                                              'bem pequena saindo dela, você decide investigar e encontra uma pequena alavanca,\n'
                                              'puxando ela abre do seu lado uma passagem secreta, você decide entrar e encontra uma\n'
                                              'escada e descendo nela, você avista outro corredor, mas esse é maior, e possui duas portas no final\n'
                                              'uma esquerda e outra direita...')
                                        while True:
                                            escolha_corredor = input('Para qual lado você vai? - Nivel 2:  ').lower()

                                            if escolha_corredor == 'direita':
                                                print('Indo pela direita você encontra uma espécie de depósito, parece que guardam enlatados lá, você decide\n'
                                                      'comer alguns desses enlatados e percebe que não há nada de muito interessante lá')
                                            elif escolha_corredor == 'esquerda':
                                                print('Indo pela esquerda você encontra uma sala muito grande, ela é toda branca e o seu piso é feito de quadrados\n'
                                                      'pretos e brancos, nela tem uma capivara muito maior que a que você encontrou lá na prisão, mas essa está usando uma\n'
                                                      'capa vermelha e fica balbuceando algumas coisas no idioma das capivaras, você tem duas opções, esgueirar por ela\n'
                                                      'sem ela perceber ou tentar imobilizá-la...')
                                            else:
                                                print('Opção inválida, apenas direita ou esquerda.')
                                                continue

                                            print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela um golpe na cabeça...')

                                            while True:
                                                escolha_açougueiro = input('O que você decide fazer? Nivel 2: ').lower()
                                                if escolha_açougueiro == 'esgueirar':
                                                    luck = random.random()  # Gera um numero entre 0 e 2
                                                    if luck < 0.8:
                                                        print('\nVocê tentou esgueirar, mas ela percebeu e quebrou a sua mente com o seu poder psíquico, agora você é um\n'
                                                              'zumbificado')
                                                        print(
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                                            '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')                                    
                                                        break
                                                    elif luck >= 0.8:
                                                        print('\nVocê conseguiu esgueirar por ela, entrando em uma sala menor você vê vestígios do que parece ser um\n'
                                                              'ritual, chegando ao centro você sente uma forte dor de cabeça, mas no meio dessa dor você vê com a visão\n'
                                                              'meio embaçada um buraco na parede, você decide entrar nesse buraco por não aguentar mais\n'
                                                              'porém quando você finalmente sai desse buraco você percebe que está no topo de uma montanha\n'
                                                              'com vista para a sua cidade, que está infestada de capivaras, você percebe que não\n'
                                                              'há nada que você ou alguém possa fazer, pois as capivaras conseguiram criar uma poderosa \n'
                                                              'máquina gigantes chamada CapiMachina, é simplesmente o fim da humanidade...')
                                                        #finaliza....
                                                        print('VOCÊ GANHOU!!!!')
                                                        print(                                                                                
                                                            '                     ╢▓█▓                                                       \n'
                                                            ''     
                                                            '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                                            ''
                                                            '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                                            ''
                                                            '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                                            ''
                                                            '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                                            ''
                                                            '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                                            ''
                                                            '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                                            ''
                                                            '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                                            ''
                                                            '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                                            ''
                                                            '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                                            ''
                                                            '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                                            ''
                                                            '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                                            ''
                                                            '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                                            ''
                                                            '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                                            ''
                                                            '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                                            ''
                                                            '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                                            ''
                                                            '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                                            ''
                                                            '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                                            ''
                                                            '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                                            ''
                                                            '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                                            ''
                                                            '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                                            ''
                                                            '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                                            ''
                                                            '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                                            ''
                                                            '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                                            ''
                                                            '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                                            ''
                                                            '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                                            ''
                                                            '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                                        break
                                                    break
                                                elif escolha_açougueiro == 'imobilizar':
                                                    luck = random.random()
                                                    if luck <= 0.7:
                                                        print('\nVocê tenta imobilizar ela mas ela quebra a sua mente, tornando você um zumbificado...')  
                                                        print(
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n'
                                                            '⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                                                            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
                                                        break

                                                    elif luck > 0.7:
                                                        print('\nVocê conseguiu imobilizar ela! Mas infelizmente ela não estava carregando nada de muito útil a não\n'
                                                              'ser um pingente que talvez valha alguma coisa no mercado negro, entrando em uma sala menor você vê vestígios do que parece ser um\n'
                                                              'ritual, chegando ao centro você sente uma forte dor de cabeça, mas no meio dessa dor você vê com a visão\n'
                                                              'meio embaçada um buraco na parede, você decide entrar nesse buraco por não aguentar mais\n'
                                                              'porém quando você finalmente sai desse buraco você percebe que está no topo de uma montanha\n'
                                                              'com vista para a sua cidade, que está infestada de capivaras, você percebe que não\n'
                                                              'há nada que você ou alguém possa fazer, pois as capivaras conseguiram criar uma poderosa \n'
                                                              'máquina gigantes chamada CapiMachina, é simplesmente o fim da humanidade...')
                                                        #finaliza....
                                                        print('VOCÊ GANHOU!!!!')
                                                        print(                                                                                
                                                            '                     ╢▓█▓                                                       \n'
                                                            ''     
                                                            '                     ▓▓█▓            ▒▓▓█▓▓Ñ                                    \n'
                                                            ''
                                                            '                  ╢▓█▓▓▓       ▓▓███████▓███▓▓Ñ                                 \n'
                                                            ''
                                                            '                 ▓Ñ█▓██-    ▓█████▓█▓▓▓██▓██▓▓▓                                 \n'
                                                            ''
                                                            '                ╢▓▓█▓█▓     ▓██▓██▓▓▓▓▓███▓████                                 \n'
                                                            ''
                                                            '                 ▄████Ñ     ▐███████████████▓██▓                                \n'
                                                            ''
                                                            '          ▒▓██▓██████▀        ▓█████████████████                                \n'
                                                            ''
                                                            '         ╫█████████▓-         ▓████████████▌-                                   \n'
                                                            ''
                                                            '         ▐███▌▐███▓▀        ╢▓██▓█▓▓██████▌                                     \n'
                                                            ''
                                                            '        ╢████ ╢████ ╢▓▓▓▓███▓█████████████▓                                     \n'
                                                            ''
                                                            '        ▓███▌  ⌐`-▓▓▓▓██▓▓██▓▓███▓▓██████████▓▓╬                                \n'
                                                            ''
                                                            '       ▐████▌    ╢▓▓▓█████▀▓██Ñ ▐▀▓▓▓Ñ       ▐█▓▓▓Ñ                             \n'
                                                            ''
                                                            '       ▓▓████  ╢▓█████████╣▓█▓▓▓▓▓███▓██▓▓█▓█████▌▓▓Ñ                           \n'
                                                            ''
                                                            '      ╢▓█████ ▓▓▓███████████████████████████▓▓▓▓██▓╣▓                           \n'
                                                            ''
                                                            '      ▓██████████████████████████████████████ ▓▄▄█▓▓▓█                          \n'
                                                            ''
                                                            '      ▓████████████████████████████████████▓██████▓▓▓▓                          \n'
                                                            ''
                                                            '     ▓███████████-  ¬▐██████████████████████████▄`-▓▓███                        \n'
                                                            ''
                                                            '     ▀███████▀▀-      ▐███▓██████████████████████▓▓▓████▀                       \n'
                                                            ''
                                                            '      ▓█▀██▓-          ¬▓██████████████████████▌- ▓█████╣                       \n'
                                                            ''
                                                            '                        ▓███████████████████████▌▓ ▐███▓▓███╣                   \n'
                                                            ''
                                                            '                 ╢▓▓█▓    ▓████▌███▓█▌▓███████████- ⌐▓█▓▓█▀██╣                  \n'
                                                            ''
                                                            '                 ▐▓▓▓█▓   ▓███▄██████▌█████████▌█-    ▓██▓█▌█▌                  \n'
                                                            ''
                                                            '                  ▐▓███Ñ ▓▓██████████▌▓██████▓█▓█      ▀▓███▌▓Ñ                 \n'
                                                            ''
                                                            '                    ▓██▓Ñ████████████████████████        ▀████▓╣                \n'
                                                            ''
                                                            '                    ▓███▓██████████████████▌▓▌█▓▓          ▐████▓               \n'
                                                            ''
                                                            '                    ▓▓██▓██████████████████▓▓▌▓█▓╣           ▀███▓              \n'
                                                            ''
                                                            '                   ▓██▓████████████████████▓▓▓████▓ ╢         ╢████             \n')
                                                        break

                                                    break
                                            break
                                    #print('Opção inválida, a sua única alternativa é lutar')
                                        break# Fase 1
                                break
                            else:
                                print('Opção inválida, a sua única alternativa é lutar')
                    break
            break


    print("\nPressione a tecla Q para sair ou a tecla I para iniciar")
    menu = input().upper()