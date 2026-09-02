from random import randint
from time import sleep
computador = randint(0, 5) ## faz o computador pensar 
print('-=-' * 20)
print('tente adivinha um numero entre 0 a 5')
print('-=-' * 20)

jogador = int(input('numero que o computador escolheu: '))
print('processando')
sleep(3)
if jogador == computador:
    print('parabens voce acertou')

else: jogador
print("voce errou")
