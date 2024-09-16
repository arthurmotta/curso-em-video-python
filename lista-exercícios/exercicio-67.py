"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""
while True:
    n = int(input("Gostaria de ver a tabuada de qual número? "))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {i*n}')
print("Programa finalizado.")
