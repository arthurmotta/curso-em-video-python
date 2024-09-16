"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles, desconsiderando o 999."""
n = 0
soma = 0
numeros = -1

while n != 999:
    numeros += 1
    soma += n
    n = int(input('Digite um número inteiro ou 999 para sair do programa: '))

print('Você digitou {} números e a soma entre eles foi de {}.'.format( numeros, soma))


# n = int(input('Digite um número inteiro: '))
# soma = 0
# numeros = 0
#
# while n != 999:
#     numeros += 1
#     soma += n
#     n = int(input('Digite mais um número inteiro: '))
#
# print('Fim.', soma, numeros)

