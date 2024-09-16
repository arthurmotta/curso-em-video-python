"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo.
Desconsidere os espaços entre elas. Ex: Após a sopa, a sacada da casa, a torre da derrota"""
frase = str(input('Digite a frase: ')).replace(" ", "")
inverso = frase[::-1]
if frase == inverso:
    print('A frase é um palíndromo. \nOriginal: {} \nInverso: {}'.format(frase, inverso))

else:
    print('A frase não é um palíndromo. \nOriginal: {} \nInverso: {}'.format(frase, inverso))

# igual = False
#
# for i in range(len(frase)):
#     if frase[i] == inverso[i]:
#         igual = True
#     else:
#         igual = False
#         break
# if igual:
#     print('A frase é um palíndromo. \nOriginal: {} \nInverso: {}'.format(frase, inverso))
# else:
#     print('A frase não é um palíndromo. \nOriginal: {} \nInverso: {}'.format(frase, inverso))
