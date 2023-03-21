from random import randint

# Inicializa variáveis
continuar_jogando = 'S'
pontuacao = 0

# Loop principal do jogo
while continuar_jogando.lower() == 's':

    # Define opções do jogo
    opcoes = ['Pedra', 'Papel', 'Tesoura']

    # Gera jogada da máquina
    jogada_maquina = randint(0, 2)

    # Solicita entrada do usuário e valida
    jogada_usuario = -1
    while jogada_usuario not in [0, 1, 2]:
        jogada_usuario = int(input("""Faça sua escolha:
        [0] Pedra
        [1] Papel
        [2] Tesoura\n"""))
    
    # Exibe jogadas e determina resultado
    print(f'Você escolheu: {opcoes[jogada_usuario]}')
    print(f'O computador escolheu: {opcoes[jogada_maquina]}')
    
    if jogada_maquina == jogada_usuario:
        print('EMPATE')
    elif jogada_maquina == 0 and jogada_usuario == 1:
        print('Você ganhou e ganhou 1 ponto!')
        pontuacao += 1
        print(f'Você tem {pontuacao} pontos!')
    elif jogada_maquina == 0 and jogada_usuario == 2:
        print('Você perdeu e perdeu 1 ponto!')
        pontuacao -= 1
        print(f'Você tem {pontuacao} pontos!')
    elif jogada_maquina == 1 and jogada_usuario == 0:
        print('Você perdeu e perdeu 1 ponto!')
        pontuacao -= 1
        print(f'Você tem {pontuacao} pontos!')
    elif jogada_maquina == 1 and jogada_usuario == 2:
        print('Você ganhou e ganhou 1 ponto!')
        pontuacao += 1
        print(f'Você tem {pontuacao} pontos!')
    elif jogada_maquina == 2 and jogada_usuario == 0:
        print('Você ganhou e ganhou 1 ponto!')
        pontuacao += 1
        print(f'Você tem {pontuacao} pontos!')
    elif jogada_maquina == 2 and jogada_usuario == 1:
        print('Você perdeu e perdeu 1 ponto!')
        pontuacao -= 1
        print(f'Você tem {pontuacao} pontos!')

    # Solicita continuação do jogo e valida
    continuar_jogando = input('Deseja continuar? [S] - Sim [N] - Não')
    while continuar_jogando.lower() not in ['s', 'n']:
        continuar_jogando 
