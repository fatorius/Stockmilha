#this module contains the stockmilha class
#an algorithm that plays the JOGO DO MILHAR with a good precision
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

from random import choices
from random import randint

class Stockmilha:

    def __init__(self):
        self.number = self.chooseNumber()
        self.candidateGuesses = self.generateValidNumbers()

    def evaluate(self, goal, shot):
        self.goal = goal
        self.shot = shot

        self.b = 0
        self.r = 0

        if not self.isNumberValid(self.shot):
            raise Exception("O número digitado é inválido")
        
        else:
            for pos, alg in enumerate(self.shot):
                if self.shot[pos] == self.goal[pos]:
                    self.b += 1
                elif alg in self.goal:
                    self.r += 1

        return {"b":self.b, "r":self.r}

    def evaluatePlayersGuess(self, hisShot):
        self.hisShot = hisShot

        return self.evaluate(self.number, self.hisShot)

    def makeAGuess(self):
        self.currentGuess = str(choices(self.candidateGuesses)[0])

        return self.currentGuess

    def updateCandidates(self, goodNumbers, regularNumbers):
        if not self.checkEvaluation(goodNumbers, regularNumbers):
            raise Exception("Esta avaliação não é válida")
        
        self.goodNumbers = goodNumbers
        self.regularNumbers = regularNumbers

        self.newCandidatesList = []

        for candidate in self.candidateGuesses:
            self.tempEvaluation = self.evaluate(self.currentGuess, str(candidate))

            if self.tempEvaluation["b"] == self.goodNumbers and self.tempEvaluation["r"] == self.regularNumbers:
                self.newCandidatesList.append(candidate)

        if len(self.newCandidatesList) == 0:
            pass
            #raise Exception("Foi detectado uma incoerência nas suas respostas, nenhum número se aplica")
        else:
            self.candidateGuesses = self.newCandidatesList

    def checkEvaluation(self, good, regular):
        self.tempGood = good
        self.tempRegular = regular

        if self.tempGood > 4 or self.tempRegular > 4:
            return False
        if self.tempGood + self.tempRegular > 4:
            return False
        if self.tempRegular == 4:
            return False
        if self.tempGood == 3 and self.tempRegular == 1:
            return False
        
        return True

    def isNumberValid(self, candidateNumber):
        self.candidateNumber = candidateNumber
        
        self.candidateNumberString = str(self.candidateNumber)

        if len(self.candidateNumberString) != 4:
            return False
        
        self.tempList = []

        for a in range(4):
            if self.candidateNumberString[a] in self.tempList:
                return False
            else:
                self.tempList.append(self.candidateNumberString[a])

        return True

    def generateValidNumbers(self):
        self.validNumbers = []

        for number in range(1023, 9877):
            if self.isNumberValid(number):
                self.validNumbers.append(number)

        return self.validNumbers

    def chooseNumber(self):
        self.validNumbers = self.generateValidNumbers()

        return str(choices(self.validNumbers)[0])