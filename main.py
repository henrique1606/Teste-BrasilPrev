from classes import tipoJogador, Propriedade
import random
import statistics

#Contador para finalizar as simulacoes
i = 0
# Contadores
contTimeOut = 0
contTurnosPartida = []
vencedorPartida = []

while i<300:

    #Definicao dos tipos de jogadores
    jogador1 = tipoJogador(300,0,0,0,True, "impulsivo")
    jogador2 = tipoJogador(0,300,0,0,True, "exigente")
    jogador3 = tipoJogador(0,0,300,0,True, "cauteloso")
    jogador4 = tipoJogador(0,0,0,300,True, "aleatorio")

    # Definicao dos valores das propriedades
    vl1 = random.randint(50, 110)
    prop1 = Propriedade(vl1, vl1 * 0.3, "", False)
    vl2 = random.randint(50, 110)
    prop2 = Propriedade(vl2, vl2 * 0.1, "", False)
    vl3 = random.randint(50, 110)
    prop3 = Propriedade(vl3, vl3 * 0.1, "", False)
    vl4 = random.randint(50, 110)
    prop4 = Propriedade(vl4, vl4 * 0.1, "", False)
    vl5 = random.randint(50, 110)
    prop5 = Propriedade(vl5, vl5 * 0.1, "", False)
    vl6 = random.randint(50, 110)
    prop6 = Propriedade(vl6, vl6 * 0.1, "", False)
    vl7 = random.randint(50, 110)
    prop7 = Propriedade(vl7, vl7 * 0.1, "", False)
    vl8 = random.randint(50, 110)
    prop8 = Propriedade(vl8, vl8 * 0.1, "", False)
    vl9 = random.randint(50, 110)
    prop9 = Propriedade(vl9, vl9 * 0.1, "", False)
    vl10 = random.randint(50, 110)
    prop10 = Propriedade(vl10, vl10 * 0.1, "", False)
    vl11 = random.randint(50, 110)
    prop11 = Propriedade(vl11, vl11 * 0.1, "", False)
    vl12 = random.randint(50, 110)
    prop12 = Propriedade(vl12, vl12 * 0.1, "", False)
    vl13 = random.randint(50, 110)
    prop13 = Propriedade(vl13, vl13 * 0.1, "", False)
    vl14 = random.randint(50, 110)
    prop14 = Propriedade(vl14, vl14 * 0.1, "", False)
    vl15 = random.randint(50, 110)
    prop15 = Propriedade(vl15, vl15 * 0.1, "", False)
    vl16 = random.randint(50, 110)
    prop16 = Propriedade(vl16, vl16 * 0.1, "", False)
    vl17 = random.randint(50, 110)
    prop17 = Propriedade(vl17, vl17 * 0.1, "", False)
    vl18 = random.randint(50, 110)
    prop18 = Propriedade(vl18, vl18 * 0.1, "", False)
    vl19 = random.randint(50, 110)
    prop19 = Propriedade(vl19, vl19 * 0.1, "", False)
    vl20 = random.randint(50, 110)
    prop20 = Propriedade(vl20, vl20 * 0.1, "", False)

    casasTabuleiro = [prop1, prop2, prop3, prop4, prop5, prop6, prop7, prop8, prop9, prop10,
                      prop11, prop12, prop13, prop14, prop15, prop16, prop17, prop18, prop19, prop20]


    # Contadores dos jogadores
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0

    # Contadores
    contRodadas = 0
    contEliminados = 0
    compValores = []

    # Definicao de ordem dos jogadores no inicio de cada rodada
    ordem = []
    while len(ordem) != 4:
        od = random.randint(1, 4)
        if od not in ordem:
            ordem.append(od)

    # Flag ordem e jogadores
    jog = []
    z=0
    while z < 4:
        if ordem[z] == 1:
            jog.append(jogador1.nome)
        elif ordem[z] == 2:
            jog.append(jogador2.nome)
        elif ordem[z] == 3:
            jog.append(jogador3.nome)
        elif ordem[z] == 4:
            jog.append(jogador4.nome)
        z = z+1

    vencedor = ""
    turno = 0

    while contRodadas == 1000 or contEliminados == -3:
        for i in ordem:
            # Caso do jogador Impulsivo 1
            if ordem==1 and jogador1.status == True:
                dado = random.randint(1, 6)
                casaJog1 = dado + casaJog1

                # Caso passe do numero de casas, retornar a casa devida no tabuleiro e adicionar 100 de saldo
                if casaJog1 >= 20:
                    casaJog1 = (20 - casaJog1) * -1
                    jogador1.impulsivo = jogador1.impulsivo + 100

                if casasTabuleiro[casaJog1].comprada == False:
                    jogador1.impulsivo = jogador1.impulsivo - casasTabuleiro[casaJog1].ctoVenda
                    casasTabuleiro[casaJog1].comprar()
                    casasTabuleiro[casaJog1].proprietario = jogador1.nome

                    print(casasTabuleiro[casaJog1].proprietario)

                elif casasTabuleiro[casaJog1].comprada == True:
                    jogador1.impulsivo = jogador1.impulsivo - casasTabuleiro[casaJog1].aluguel

                    if casasTabuleiro[casaJog1].proprietario == jogador2.nome:
                        jogador2.exigente = jogador2.exigente + casasTabuleiro[casaJog1].aluguel
                    elif casasTabuleiro[casaJog1].proprietario == jogador3.nome:
                        jogador3.cauteloso = jogador3.cauteloso + casasTabuleiro[casaJog1].aluguel
                    else:
                        jogador4.aleatorio = jogador4.aleatorio + casasTabuleiro[casaJog1].aluguel

                # Verificacao se o jogador está com saldo negativo
                if jogador1.impulsivo<0:
                    jogador1.foraDoJogo()
                    contEliminados = contEliminados - 1
                    # Remocao das casas do jogador eliminado
                    for i in casasTabuleiro:
                        if casasTabuleiro[i].proprietario == jogador1.nome:
                            casasTabuleiro[i].proprietario = ""
                            casasTabuleiro[i].perder()

            # Caso do jogador Exigente 2
            if ordem[i] == 2 and jogador2.status == True:
                dado = random.randint(1, 6)
                casaJog2 = dado + casaJog2

                # Caso passe do numero de casas, retornar a casa devida no tabuleiro e adicionar 100 de saldo
                if casaJog2 >= 20:
                    casaJog2 = (20 - casaJog2) * -1
                    jogador2.exigente = jogador2.exigente + 100

                if casasTabuleiro[casaJog2].comprada == False:
                    if casasTabuleiro[casaJog2].aluguel > 50:
                        jogador2.exigente = jogador1.exigente - casasTabuleiro[casaJog2].ctoVenda
                        casasTabuleiro[casaJog2].comprar()
                        casasTabuleiro[casaJog2].proprietario = jogador2.nome

                    elif casasTabuleiro[casaJog2].comprada == True:
                        jogador2.exigente = jogador2.exigente - casasTabuleiro[casaJog2].aluguel

                        if casasTabuleiro[casaJog2].proprietario == jogador1.nome:
                            jogador1.impulsivo = jogador1.impulsivo + casasTabuleiro[casaJog2].aluguel
                        elif casasTabuleiro[casaJog2].proprietario == jogador3.nome:
                            jogador3.cauteloso = jogador3.cauteloso + casasTabuleiro[casaJog2].aluguel
                        else:
                            jogador4.aleatorio = jogador4.aleatorio + casasTabuleiro[casaJog2].aluguel

                # Verificacao se o jogador está com saldo negativo
                if jogador2.exigente < 0:
                    jogador2.foraDoJogo()
                    contEliminados = contEliminados - 1
                    # Remocao das casas do jogador eliminado
                    for i in casasTabuleiro:
                        if casasTabuleiro[i].proprietario == jogador2.nome:
                            casasTabuleiro[i].proprietario = ""
                            casasTabuleiro[i].perder()

            # Caso do jogador Cauteloso 3
            if ordem[i] == 3 and jogador3.status == True:
                dado = random.randint(1, 6)
                casaJog3 = dado + casaJog3

                # Caso passe do numero de casas, retornar a casa devida no tabuleiro e adicionar 100 de saldo
                if casaJog3 >= 20:
                    casaJog3 = (20 - casaJog3) * -1
                    jogador3.cauteloso = jogador3.cauteloso + 100

                if casasTabuleiro[casaJog3].comprada == False:
                    if jogador3.cauteloso - casasTabuleiro[casaJog3].ctoVenda >= 80:
                        jogador3.cauteloso = jogador3.cauteloso - casasTabuleiro[casaJog3].ctoVenda
                        casasTabuleiro[casaJog3].comprar()
                        casasTabuleiro[casaJog3].proprietario = jogador3.nome

                    elif casasTabuleiro[casaJog3].comprada == True:
                        jogador3.cauteloso = jogador3.cauteloso - casasTabuleiro[casaJog3].aluguel

                        if casasTabuleiro[casaJog3].proprietario == jogador1.nome:
                            jogador1.impulsivo = jogador1.impulsivo + casasTabuleiro[casaJog3].aluguel
                        elif casasTabuleiro[casaJog3].proprietario == jogador2.nome:
                            jogador2.exigente = jogador2.exigente + casasTabuleiro[casaJog3].aluguel
                        else:
                            jogador4.aleatorio = jogador4.aleatorio + casasTabuleiro[casaJog3].aluguel

                # Verificacao se o jogador está com saldo negativo
                if jogador3.cauteloso < 0:
                    jogador3.foraDoJogo()
                    contEliminados = contEliminados - 1
                    # Remocao das casas do jogador eliminado
                    for i in casasTabuleiro:
                        if casasTabuleiro[i].proprietario == jogador3.nome:
                            casasTabuleiro[i].proprietario = ""
                            casasTabuleiro[i].perder()

            # Caso do jogador Aleatorio
            if ordem[i] == 4 and jogador4.status == True:
                dado = random.randint(1, 6)
                casaJog4 = dado + casaJog4

            # Caso passe do numero de casas, retornar a casa devida no tabuleiro e adicionar 100 de saldo
                if casaJog4 >= 20:
                    casaJog4 = (20 - casaJog4) * -1
                    jogador4.aleatorio = jogador4.aleatorio + 100

                if casasTabuleiro[casaJog4].comprada == False:
                    aleatorio = random.randint(0, 1)
                    if aleatorio==1:
                        jogador4.aleatorio = jogador4.aleatorio - casasTabuleiro[casaJog4].ctoVenda
                        casasTabuleiro[casaJog4].comprar()
                        casasTabuleiro[casaJog4].proprietario = jogador4.nome

                    elif casasTabuleiro[casaJog4].comprada == True:
                        jogador4.aleatorio = jogador4.aleatorio - casasTabuleiro[casaJog4].aluguel

                        if casasTabuleiro[casaJog4].proprietario == jogador1.nome:
                            jogador1.impulsivo = jogador1.impulsivo + casasTabuleiro[casaJog4].aluguel
                        elif casasTabuleiro[casaJog4].proprietario == jogador2.nome:
                            jogador2.exigente = jogador2.exigente + casasTabuleiro[casaJog4].aluguel
                        else:
                            jogador3.cauteloso = jogador3.cauteloso + casasTabuleiro[casaJog4].aluguel

        turno = turno + 1
        contRodadas = contRodadas + 1

        compValores_lista = [(jogador1.impulsivo, jogador1.nome),(jogador2.exigente, jogador2.nome), (jogador3.cauteloso, jogador3.nome),(jogador4.aleatorio, jogador4.nome)]
        compValores = dict(compValores_lista)

        if contRodadas == 1000:
            '''
            compValoresOrdenados = sorted(compValores)
            if compValoresOrdenados[0] > compValoresOrdenados[1]:
                vencedor = compValoresOrdenados[0]
            elif compValoresOrdenados[0] == compValoresOrdenados[1]:
                for i in jog:
                    if compValoresOrdenados[0] == jog[i]:
                        vencedor == compValoresOrdenados[j]
                    elif compValoresOrdenados[1] == jog[i]:
                        vencedor == compValoresOrdenados[j]
            '''
            contTimeOut = contTimeOut + 1

        elif jogador1.status == False and jogador2.status == False and jogador3.status == False:
            vencedor = jogador4.nome
        elif jogador1.status == False and jogador2.status == False and jogador4.status == False:
            vencedor = jogador3.nome
        elif jogador4.status == False and jogador2.status == False and jogador3.status == False:
            vencedor = jogador1.nome
        elif jogador4.status == False and jogador1.status == False and jogador3.status == False:
            vencedor = jogador4.nome

    vencedorPartida.append(vencedor)
    contTurnosPartida.append(turno)
    i = i +1

## SAIDAS ##
print("O numero de partidas que terminaram por timeOut foram: " + str(contTimeOut))
mediaTurnos = statistics.mean(contTurnosPartida)
print("Uma partida em média demora: " + str(mediaTurnos) + " turnos")


