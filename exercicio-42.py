"""Refaça o exercício 35 dos triângulos, acrescentando o recurso
 de mostrar que tipo de triângulo será formado: Equilátero: todos os
 lados iguais. Isósceles: dois lados iguais. Escaleno: todos os lados
 diferentes"""

r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    if r1 == r2 == r3:
        print('Essas retas formam um triângulo equilátero. Todos os lados são iguais.')
    elif r1 != r2 != r3 != r1:
        print('Essas retas formam um triângulo escaleno. Todos os lados são diferentes.')
    else:
        print('Essas retas formam um triângulo isósceles. Pelo menos, dois lados são iguais.')
else:
    print('Essas retas não formam um triângulo.')