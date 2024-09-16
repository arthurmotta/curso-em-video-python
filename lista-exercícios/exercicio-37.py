"""Escreva um programa que leia um número inteiro qualquer e peça
 para o usuário escolher qual será a base de conversão."""

n = int(input('Digite um número inteiro: '))
b = int(input('Escolha uma base de conversão: \n1 (Binário) \n2 (Octal) \n3 (Hexadecimal) \nSua opção: '))
if b == 1:
    print(bin(n))
elif b == 2:
    print(oct(n))
elif b == 3:
    print(hex(n))
else:
    print('Opção inválida. Tente novamente.')
