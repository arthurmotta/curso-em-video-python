"""Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o"""
soma = 0
numeros = 0

for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        numeros += 1

print('Você informou {} números pares. \nA soma entre eles é de: {}'.format(numeros, soma))