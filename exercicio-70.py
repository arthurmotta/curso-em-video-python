"""Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""
total = totMil = mais_barato = cont = 0
nome_mais_barato = ''

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        totMil += 1

    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    continuar = ' '

    while continuar not in 'sSnN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
            break

print(f'--------- FIM DO PROGRAMA ---------\n'
      f'O total dos produtos deu R${total:.2f} reais.\n'
      f'Existem {totMil} produtos que custam mais de R$1000 reais.\n'
      f'O produto mais barato foi {nome_mais_barato} que custa R${mais_barato}.')