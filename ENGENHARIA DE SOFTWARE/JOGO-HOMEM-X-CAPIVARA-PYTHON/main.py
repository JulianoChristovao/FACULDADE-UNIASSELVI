import random #importado a biblioteca Randon qua fará o sorteamento das decisões no jogo


#--- Opções do Menu ---
print("\nBem vindo ao Jogo: Homem x Capivara!!!\n")
print("Pressione a tecla Q para sair ou a tecla I para iniciar")
menu = input().upper()  # Converte a entrada para maiúsculas para facilitar a comparação
while menu != "Q":
    if menu == "I":

# --- Código do Game ---
        print('texto apresentação nivel 1')
        while True:
            escolha_corredor = input('Para qual lado você vai? - Nivel 1 ').lower()

            if escolha_corredor == 'direita':
                print('Texto apresentação direita - Nivel 1 ')
            elif escolha_corredor == 'esquerda':
                print(
                'Texto apresentação esquerda - Nivel 1')
            else:
                print('Opção inválida, apenas direita ou esquerda.')
                continue

            print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou... Nivel 1 ')

            while True:
                escolha_açougueiro = input('O que você decide fazer? Nivel 1').lower()
                if escolha_açougueiro == 'esgueirar':
                    luck = random.random()  # Gera um numero entre 0 e 1
                    if luck < 0.3:
                        print('\nTexto que morreu ao esgueirar - Nivel 1 ')
                        break
                    elif luck >= 0.3:
                        print('\nTexto que conseguiu esgueirar - Nivel 1 ')
                    #vai para a fase 2....
                    

                    


                    # Inicio da fase 2
                    print('texto apresentação nivel 2')
                    while True:
                        escolha_corredor = input('Para qual lado você vai? - Nivel 2 ').lower()

                        if escolha_corredor == 'direita':
                            print('Texto apresentação direita - Nivel 2 ')
                        elif escolha_corredor == 'esquerda':
                            print('Texto apresentação esquerda - Nivel 2')
                        else:
                            print('Opção inválida, apenas direita ou esquerda.')
                            continue

                        print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou... Nivel 2 ')

                        while True:
                            escolha_açougueiro = input('O que você decide fazer? Nivel 2').lower()
                            if escolha_açougueiro == 'esgueirar':
                                luck = random.random()  # Gera um numero entre 0 e 2
                                if luck < 0.3:
                                    print('\nTexto que morreu ao esgueirar - Nivel 2 ')
                                    break
                                elif luck >= 0.3:
                                    print('\nTexto que conseguiu esgueirar - Nivel 2 ')
                                #vai para a fase 3....
                                print('vai para a fase 3')
                                break
                            elif escolha_açougueiro == 'imobilizar':
                                luck = random.random()
                                if luck <= 0.7:
                                    print('\nTexto que morreu ao imobilizar - Nivel 2 ')  
                                    
                                elif luck > 0.7:
                                    print('\nTexto que conseguiu imobilizar - Nivel 2 ')
                                    #vai para a fase 3....
                                    print('vai para a fase 3')
                                break
                        break



                    
                    
                    break# Fase 1







                    
                # FASE 1 IMOBILIZAR
                elif escolha_açougueiro == 'imobilizar':

                    luck = random.random()

                    if luck <= 0.7:
                            print('\nTexto que morreu ao imobilizar - Nivel 1 ')  
                                  
                    elif luck > 0.7:
                        print('\nTexto que conseguiu imobilizar - Nivel 1 ')
                        #vai para a fase 2....
                        print('vai para a fase 2')




                        print('texto apresentação nivel 2')
                        while True:
                            escolha_corredor = input('Para qual lado você vai? - Nivel 2 ').lower()

                            if escolha_corredor == 'direita':
                                print('Texto apresentação direita - Nivel 2 ')
                            elif escolha_corredor == 'esquerda':
                                print('Texto apresentação esquerda - Nivel 2')
                            else:
                                print('Opção inválida, apenas direita ou esquerda.')
                                continue

                            print('\nVocê pode esgueirar por ela sem fazer barulho ou tentar imobilizar ela dando-lhe uma panelada na cabeça com uma panela que encontrou... Nivel 2 ')

                            while True:
                                escolha_açougueiro = input('O que você decide fazer? Nivel 2').lower()
                                if escolha_açougueiro == 'esgueirar':
                                    luck = random.random()  # Gera um numero entre 0 e 2
                                    if luck < 0.3:
                                        print('\nTexto que morreu ao esgueirar - Nivel 2 ')
                                        break
                                    elif luck >= 0.3:
                                        print('\nTexto que conseguiu esgueirar - Nivel 2 ')
                                    #vai para a fase 3....
                                    print('vai para a fase 3')
                                    break
                                elif escolha_açougueiro == 'imobilizar':
                                    luck = random.random()
                                    if luck <= 0.7:
                                        print('\nTexto que morreu ao imobilizar - Nivel 2 ')  
                                        
                                    elif luck > 0.7:
                                        print('\nTexto que conseguiu imobilizar - Nivel 2 ')
                                        #vai para a fase 3....
                                        print('vai para a fase 3')
                                    break
                            break





                        break
            break

    print("\nPressione a tecla Q para sair ou a tecla I para iniciar")
    menu = input().upper()
    

print("Você saiu do jogo")
