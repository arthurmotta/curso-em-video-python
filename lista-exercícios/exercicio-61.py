"""Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando uma estrutura while."""
termo = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão da PA: '))
contador = 10

while contador > 0:
    print('{} ➝ '.format(termo), end='')
    termo += razao
    contador -=1

print('Fim.')
