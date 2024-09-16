"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando a flag 999)."""
valor = quantidade = soma = 0
while True:
    valor = int(input("Digite um valor (999 para sair): "))
    if valor == 999:
        break
    soma = soma + valor
    quantidade = quantidade + 1
print(f'Você digitou {quantidade} valores e a soma entre eles foi {soma}.')