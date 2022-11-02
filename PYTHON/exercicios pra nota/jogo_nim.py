def ModoDeJogo():
    modoDeJogoSelecionado = 0
    modosDeJogo = ["jogar uma partida isolada", "jogar um campeonato"]
    
    print("Bem-vindo ao jogo do NIM! Selecione um modo de jogo:\n")
    for chave, modo in enumerate(modosDeJogo):
        print("{} - {}".format(chave + 1, modo))

    while modoDeJogoSelecionado > len(modosDeJogo) or modoDeJogoSelecionado < 1:
        modoDeJogoSelecionado = int(input("Qual modo você deseja jogar? "))
    
    print("Você selecionou o modo: {}\n".format(modosDeJogo[modoDeJogoSelecionado -1]))
    
    return modoDeJogoSelecionado    
      
def computador_escolhe_jogada(n, m):
    pecasRestantesNoJogo = n
    limiteDePecasRemovidas = m
    escolhaDoComputador = 0

    if pecasRestantesNoJogo <= limiteDePecasRemovidas:
        escolhaDoComputador = pecasRestantesNoJogo
    else:
        for i in range(1, (limiteDePecasRemovidas + 1)):
            if(pecasRestantesNoJogo - i) % (limiteDePecasRemovidas + 1) == 0:
               escolhaDoComputador = i
               
    if escolhaDoComputador == 0:
        escolhaDoComputador = limiteDePecasRemovidas
        
    return escolhaDoComputador

def usuario_escolhe_jogada(n, m):
    pecasRestantesNoJogo = n
    limiteDePecasRemovidas = m
    escolhaDoJogador = 0

    if pecasRestantesNoJogo >= limiteDePecasRemovidas:
        limiteDePecasRemovidasNaJogada = limiteDePecasRemovidas
    else:
        limiteDePecasRemovidasNaJogada = pecasRestantesNoJogo

    while escolhaDoJogador > limiteDePecasRemovidasNaJogada or escolhaDoJogador < 1:
        escolhaDoJogador = int(input("Quantas peças você vai tirar? "))

    return escolhaDoJogador

def partida():
    computadorVenceu = True
    turnoDoComputador = False
    limiteDePecasPorJogada = 0

    totalDePecas = int(input("Quantas peças?"))
    
    while limiteDePecasPorJogada < 1:
        limiteDePecasPorJogada = int(input("Limite de peças por jogada? "))
        
    if totalDePecas % (limiteDePecasPorJogada + 1) == 0:
        print("Voce começa!\n")
        turnoDoComputador = False
    else:
        print("O Computador começa!/n")
        turnoDoComputador = True

    while totalDePecas > 0:
        if turnoDoComputador:
            pecasRetiradas = computador_escolhe_jogada(totalDePecas, limiteDePecasPorJogada)
            print("O computador tirou {} peças(s).".format(pecasRetiradas))
        else:
            pecasRetiradas = usuario_escolhe_jogada(totalDePecas, limiteDePecasPorJogada)
            print("Você tirou {} peças(s).".format(pecasRetiradas))

        totalDePecas = totalDePecas - pecasRetiradas

        if totalDePecas > 1:
            print("Agora restam {} peças no tabuleiro.\n".format(totalDePecas))
        elif totalDePecas == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            
        turnoDoComputador = not turnoDoComputador
        
    if not turnoDoComputador:
        print ("O computador ganhou!")
    else:
        computadorVenceu = False
        print("Você ganho!")
        
    return(computadorVenceu)


def campeonato():
    numeroDaRodada = 1
    pontosDoComputador = 0
    pontosDoUsuario = 0
    
    while numeroDaRodada < 4:
        print("**** Rodada {} ****\n.".format(numeroDaRodada))
        
        if partida():
            pontosDoComputador += 1
        else:
            pontosDoUsuario += 1
            
        numeroDaRodada += 1

    print("Placar: Você {} X {} Computador".format(pontosDoUsuario, pontosDoComputador))

def main():
    modoDeJogo = ModoDeJogo()
    
    partida() if modoDeJogo == 1 else campeonato ()
    
main ()

