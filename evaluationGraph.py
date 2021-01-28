#this is just a test to see how stockmilha discards candidates at each evaluation
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
import matplotlib.pyplot as plt

games = int(input("Digite a quantidade de jogos a serem jogados: \n"))

candidatesNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rodadasMedia = 0

for game in range(games):
    print("\r Jogo: {} de {}".format(game, games))

    stkm1 = stockmilha.Stockmilha()
    stkm2 = stockmilha.Stockmilha()

    rodadas = 0

    while (True):
        candidatesNum[rodadas] += len(stkm2.candidateGuesses)

        guess = stkm2.makeAGuess()
        evaluation = stkm1.evaluatePlayersGuess(guess)

        if evaluation["b"] == 4:
            rodadasMedia += rodadas

            break

        stkm2.updateCandidates(evaluation["b"], evaluation["r"])

        rodadas += 1

for pos, candidate in enumerate(candidatesNum):
    candidatesNum[pos] = candidate / games

print("CandidatesNum: ")
print(candidatesNum)
print("Media de rodadas = {}".format(rodadasMedia/games))

eliminationNum = []

for a in range(0, 9):
    eliminationNum.append(candidatesNum[a] - candidatesNum[a+1])

print("EliminationNum: {}".format(eliminationNum))

fig, axs = plt.subplots(2)
fig.suptitle('Candidatos após {} jogos \n Media de rodadas: {}'.format(games, rodadasMedia/games))
axs[0].plot(candidatesNum)
axs[0].set_title('Candidados restantes')
axs[1].bar(range(9), eliminationNum)
axs[1].set_title('Quantidade de eliminações')

plt.show()