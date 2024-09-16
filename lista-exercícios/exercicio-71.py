"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

saque = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break

print(f'Você receberá {n50} notas de 50, {n20} de 20, {n10} de 10 e {n1} de 1.')

# while True:
#     total = total + 1
#     valor = valor - 50
#     if valor < 50:
#         print(f'Total de {total} cédulas de R$50')
#         break
# total = 0
# while True:
#     total = total + 1
#     valor = valor - 20
#     if valor < 20:
#         print(f'Total de {total} cédulas de R$20')
#         break
# total = 0
# while True:
#     total = total + 1
#     valor = valor - 10
#     if valor < 10:
#         print(f'Total de {total} cédulas de R$10')
#         break
# total = 0
# while True:
#     total = total + 1
#     valor = valor - 1
#     if valor < 1:
#         print(f'Total de {total} cédulas de R$1')
#         break