"""Crie um programa que faça o computador jogar
Jokenpô com você. (Pedra, papel e tesoura)"""
import random

jogador = int(input('Escolha uma opção:\n'
                  '(1) Pedra\n'
                  '(2) Papel\n'
                  '(3) Tesoura\n'))

computador = random.randint(1, 3)
print(computador)
if computador == jogador:
    print('Jogada igual. Jogue de novo.')
else:
    if computador == 1 and jogador == 3:
        print('Voce perdeu. Pedra amassa tesoura')
    elif computador == 2 and jogador == 1:
        print('Voce perdeu. Papel embrulha pedra')
    elif computador == 3 and jogador == 2:
        print('Voce perdeu. Tesoura corta papel')
    elif jogador == 1 and computador == 3:
        print('Ganhou. Pedra amassa tesoura')
    elif jogador == 2 and computador == 1:
        print('Ganhou. Papel embrulha pedra')
    elif jogador == 3 and computador == 2:
        print('Ganhou. Tesoura corta papel')