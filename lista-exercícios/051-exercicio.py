"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
termo = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão da PA: '))
decimo = termo + (10 -1) * razao
for i in range(termo, decimo + razao, razao):
    print('{} ➝ '.format(i), end='')
print('Fim.')

# for i in range(0, 10):
#     pa = termo + razao
#     termo = pa
#     print('{} ➝ '.format(pa), end='')
# print('Fim.')
