"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o homem mais velho
e quantas mulheres tem menos de 20 anos."""
soma = 0
media = 0
nome_mais_velho = ''
idade_mais_velho = 0
menos_vinte = 0

for pessoa in range(1, 5):
    print('------ {}ª PESSOA ------'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    soma += idade
    media = soma / 4

    if sexo == 'm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    else:
        if idade < 20:
            menos_vinte += 1

print('A média de idade do grupo é de {} anos. '
      '\nO homem mais velho tem {} anos e seu nome é {}.'
      '\nAo todo, são {} mulheres com menos de 20 anos.'.format(media, idade_mais_velho, nome_mais_velho, menos_vinte))


# pessoa = ''
# media = 0
# idades = 0
# homem_mais_velho = 0
# mulheres_menos_vinte = 0
#
# for i in range(0, 4):
#     pessoa = str(input('Digite seu nome, idade e sexo: ')).split()
#     idades = idades + int(pessoa[1])
#     media = idades / 4
#     if pessoa[2] == 'masculino':
#         if int(pessoa[1]) > homem_mais_velho:
#             homem_mais_velho = int(pessoa[1])
#     else:
#         if int(pessoa[1]) < 20:
#             mulheres_menos_vinte = mulheres_menos_vinte + 1
#
# print(media, homem_mais_velho, mulheres_menos_vinte)


