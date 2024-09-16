"""Refaça o exercício 09, mostrando a tabuada de um número que o usuário escolher
só que agora usando um laço for"""
n = int(input("Informe um número: "))
for i in range(1,11):
    print("{} x {} =".format(n, i), i * n)