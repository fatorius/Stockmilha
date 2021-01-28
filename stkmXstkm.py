#this is just a test to see how stockmilha performs playing against itself
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

def isPar(number):
    if number % 2 == 0:
        return True
    else:
        return False

games = int(input("Digite a quantidade de jogos a serem jogados: "))

stkm1Wins = 0
empates = 0.0
stkm2Wins = 0

rodadasMedia = 0

for game in range(games):
    stkm1 = stockmilha.Stockmilha()
    stkm2 = stockmilha.Stockmilha()

    rodadas = 0

    if isPar(game):
        while (True):
            rodadas += 1

            guess = stkm1.makeAGuess()
            evaluation = stkm2.evaluatePlayersGuess(guess)
            
            if evaluation["b"] == 4:
                guess = stkm2.makeAGuess()
                evaluation = stkm1.evaluatePlayersGuess(guess)

                if evaluation["b"] == 4:
                    empates += 1
                else:
                    stkm1Wins += 1

                break
            
            stkm1.updateCandidates(evaluation["b"], evaluation["r"])

            guess = stkm2.makeAGuess()
            evaluation = stkm1.evaluatePlayersGuess(guess)

            if evaluation["b"] == 4:
                stkm2Wins += 1

                break

            stkm2.updateCandidates(evaluation["b"], evaluation["r"])

    else:
        while (True):
            rodadas += 1

            guess = stkm2.makeAGuess()
            evaluation = stkm1.evaluatePlayersGuess(guess)

            if evaluation["b"] == 4:
                guess = stkm1.makeAGuess()
                evaluation = stkm2.evaluatePlayersGuess(guess)

                if evaluation["b"] == 4:
                    empates += 1
                else:
                    stkm2Wins += 1

                break

            stkm2.updateCandidates(evaluation["b"], evaluation["r"])

            guess = stkm1.makeAGuess()
            evaluation = stkm2.evaluatePlayersGuess(guess)
            
            if evaluation["b"] == 4:
                stkm1Wins += 1

                break
            
            stkm1.updateCandidates(evaluation["b"], evaluation["r"])

    rodadasMedia += rodadas

    print("\r Jogo {} - Stockmilha1: {} | Empates: {} | Stockmilha2: {} - {} Rodadas".format(game, stkm1Wins, empates, stkm2Wins, rodadas))

print("RESULTADO FINAL: STKM1 {} x STKM2 {}".format(stkm1Wins + (empates/2), stkm2Wins + (empates/2)))
print("Média de rodadas = {}".format(rodadasMedia/games))