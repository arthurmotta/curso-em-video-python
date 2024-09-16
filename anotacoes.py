"""Utilizamos o passo para pular de x em x números
Entrada:
Início: 0
Fim: 20
Passo: 5
Saída:
0
5
10
15
20"""

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for i in range(inicio, fim+1, passo):
    #Para inverter a leitura do for basta trocar
    #inverter as posições de início e fim
    #e adicionando -1 no lugar do passo
    print(i)

#Utilizar flags no while
