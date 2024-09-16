"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução mostre a média entre todos os valores e qual foi
o maior e menor entre os valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores."""
soma = contagem = menor_valor = maior_valor = 0
opcao = 's'

while opcao in 'Ss':
    numero = int(input('Digite um número inteiro: '))
    contagem += 1
    soma += numero

    if contagem == 1:
        maior_valor = numero
        menor_valor = numero
    else:
        if numero > maior_valor:
            maior_valor = numero
        if numero < menor_valor:
            menor_valor = numero
    opcao = str(input('Deseja continuar? [S/N]\n'))

media = soma / contagem
print('Você digitou {} números e a média entre eles foi: {}'
      '\nO maior valor foi {} e o menor foi {}.'.format(
      contagem , media, maior_valor, menor_valor))

# while opcao in 'Ss':
#     numero = int(input('Digite um número inteiro: '))
#     if numero > maior_valor:
#         maior_valor = numero
#     elif menor_valor == 0:
#         menor_valor = numero
#     elif numero < menor_valor:
#         menor_valor = numero
#
#     contagem += 1
#     soma += numero
#     opcao = str(input('Deseja continuar? [S/N]\n'))