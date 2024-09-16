"""Melhore o exercício 28 onde o computador vai "pensar" em um número
 entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
 acertar, mostrando no final quantos palpites foram necessários
 para vencer."""
import random
num_secreto = random.randrange(0, 10)
acertou = False
tentativas = 0

while not acertou:
    num = int(input('Adivinhe o número secreto entre 0 a 10. Digite um número: '))
    tentativas += 1
    if num == num_secreto:
        tentativas += 1
        print('Você acertou com {} tentativas!'
              '\nNúmero secreto: {}'.format(tentativas, num_secreto))
        acertou = True
    else:
        print('Você errou! Tente novamente.')
