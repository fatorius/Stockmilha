#here you can play the JOGO DO MILHAR against stockmilha
#copyright (c) 2021 hugosouza

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

#email: contato@hugosouza.com 

import stockmilha

stockmilha = stockmilha.Stockmilha()

print("Você deseja começar (s/n)")
starter = input()

if starter != "s" and starter != "n":
    print("Valor inválido")

    while True:
        print("Você deseja começar (s/n)")
        starter = input()

        if starter == "s" or starter == "n":
            break

if starter == "s":
    playerStarts = True
else:
    playerStarts = False

if playerStarts:
    while True:

        #vez do jogador
        print('='*15)

        isGuessValid = False

        while not isGuessValid:
            playerGuess = input("Digite seu palpite: ")
            
            try:
                evaluation = stockmilha.evaluatePlayersGuess(playerGuess)
                isGuessValid = True
            except:
                print("Número digitado inválido, tente novamente")

        print("Stockmilha diz:")
        print("{} bons e {} regulares".format(evaluation["b"], evaluation["r"]))

        if evaluation["b"] == 4:
            print("Parabéns você acertou o número, porém como você começou, o Stockmilha tem a chance de empatar")

            #vez do stockmilha
            print('='*15)

            print("Stockmilha chuta: {}".format(stockmilha.makeAGuess()))

            isEvaluationValid = False

            while not isEvaluationValid:
                bons = int(input("Digite a quantidade de numeros bons: "))
                regulares = int(input("Digite a quantidade de numeros regulares: "))

                try:
                    stockmilha.updateCandidates(bons, regulares)
                    isEvaluationValid = True
                except:
                    print("Sua avaliação está incorreta, digite novamente")

                if bons == 4:
                    print("Stockmilha acertou seu número, jogo empatado")
                else:
                    print("Stockmilha errou o seu número. Jogo encerrado. Vitória para PLAYER")

            break

        #vez do stockmilha
        print('='*15)

        print("Stockmilha chuta: {}".format(stockmilha.makeAGuess()))

        isEvaluationValid = False

        while not isEvaluationValid:
            bons = int(input("Digite a quantidade de numeros bons: "))
            regulares = int(input("Digite a quantidade de numeros regulares: "))

            try:
                stockmilha.updateCandidates(bons, regulares)
                isEvaluationValid = True
            except:
                print("Sua avaliação está incorreta, digite novamente")

        if bons == 4:
            print("Stockmilha acertou o seu número, jogo encerrado. Vitória para Stockmilha")

            break

else:
    while True:
        #vez do stockmilha
        print('='*15)

        print("Stockmilha chuta: {}".format(stockmilha.makeAGuess()))

        isEvaluationValid = False

        while not isEvaluationValid:
            bons = int(input("Digite a quantidade de numeros bons: "))
            regulares = int(input("Digite a quantidade de numeros regulares: "))

            try:
                stockmilha.updateCandidates(bons, regulares)
                isEvaluationValid = True
            except:
                print("Sua avaliação está incorreta, digite novamente")

        if bons == 4:
            print("Stockmilha acertou o seu número, porém como ele começou adivinhando você tem uma chance para empatar")

            print('='*15)

            isGuessValid = False

            while not isGuessValid:
                playerGuess = input("Digite seu palpite: ")
                
                try:
                    evaluation = stockmilha.evaluatePlayersGuess(playerGuess)
                    isGuessValid = True
                except:
                    print("Número digitado inválido")

            print("Stockmilha diz:")
            print("{} bons e {} regulares".format(evaluation["b"], evaluation["r"]))

            if evaluation["b"] == 4:
                print("Parabéns, você adivinhou o número do Stockmilha, jogo empatado")
            else:
                print("Você errou, o número correto era {}, vitória para Stockmilha".format(stockmilha.number))

            break

        #vez do jogador
        print('='*15)

        isGuessValid = False

        while not isGuessValid:
            playerGuess = input("Digite seu palpite: ")
            
            try:
                evaluation = stockmilha.evaluatePlayersGuess(playerGuess)
                isGuessValid = True
            except:
                print("Número digitado inválido")

        print("Stockmilha diz:")
        print("{} bons e {} regulares".format(evaluation["b"], evaluation["r"]))

        if evaluation["b"] == 4:
            print("Parabéns você acertou o número, jogo encerrado. Vitória para PLAYER")

            break
    