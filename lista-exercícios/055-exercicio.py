"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos."""
peso_maior = 0
peso_menor = 0

for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if peso > peso_maior:
        peso_maior = peso
    else:
        peso_menor = peso

print('O maior peso é de {}Kg.'
      '\nE o menor peso é de {}Kg.'.format(peso_maior, peso_menor))

