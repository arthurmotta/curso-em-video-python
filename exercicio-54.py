"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import datetime

ano_atual = datetime.today().year
menores = 0
maiores = 0

for i in range(1, 8):
    ano = int(input('Em que ano a {}ª nasceu? '.format(i)))
    if ano_atual - ano > 21:
        maiores += 1
    else:
        menores += 1
print('Temos {} pessoas maiores de idade.'
      '\nE também {} pessoas menores de idade.'.format(maiores, menores))