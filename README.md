# stockmilha
 o stockmilha é um algoritmo que joga o jogo do milhar com alta precisão

 o jogo do milhar consiste em adivinhar o número que o adversário escolheu
 com base em uma série de chutes e avaliações

 para mais detalhes sobre como jogar esse jogo, acesse: https://hugosouza.com/projetos/stockmilha/tutorial.html

 o stockmilha é capaz de adivinhar o número do do adversário com em média 4 chutes

 ## sobre o repositorio

 este repositório contém o módulo ```stockmilha.py```, que você pode usá-lo para implementar
 na sua propria interface de jogo para jogar com ele, ou você pode usar a interface que eu criei
 em ```game.py```
 
 além disso, nesse repositório também se encontram alguns experimentos para demonstrar a precisão do 
 stockmilha: ```stkmXstkm.py``` coloca o stockmilha para jogar contra ele mesmo e mostra o placar
 ```evaluationGraph.py``` demonstra graficamente a média de palpites eliminados a cada avaliação.
 
 ## documentação

 caso você queira inserir o módulo do ```stockmilha.py``` em algum programa, ou deseja alterar suas funcionalidades, escrevi aqui uma pequena documentação sobre ele:

 *a classe* ```Stockmilha```
 
 essa é a classe principal do arquivo.
 ela não precisa de nenhum parametro para ser inicializada

 quando o objeto do tipo ```Stockmilha``` é criado, ele automáticamente gera dois atributos:
 ```Stockmilha.number```: O número que dele, no qual o adversário deve adivinhar
 ```Stockmilha.candidateGuesses```: Uma lista com os números possíveis que o adversário pode ter escolhido

 quando é a vez do Stockmilha de fazer o seu palpite, o método ```Stockmilha.makeAGuess()```
 é utilizado para o Stockmilha escolher um número dentre os ```Stockmilha.candidateGuesses```
 e vai retorná-lo para que o adversário faça a avaliação do número

 depois que o adversário fizer a avaliação, o método ```Stockmilha.updateCandidates(int goodNumbers, int regularNumbers)```
 é utilizado para o Stockmilha eliminar membros do ```Stockmilha.candidateGuesses``` com base na avaliação
 do adversário, portanto os parametros ```goodNumbers``` e os ```regularNumbers``` representam
 a quantidade de números bons e números regulares no número retornado pelo método ```Stockmilha.makeAGuess()```

 quando for a vez do adversário fazer o palpite, o método ```Stockmilha.evaluatePlayersGuess(int hisShot)```
 é usado para retornar a avaliação do número do adversário. este método retorna um dicionário 
 com duas chaves: ```"b"``` e ```"r"```. ```"b"``` armazena a quantidade de números bons e 
 ```"r"``` armazena a quantidade de números regulares. 