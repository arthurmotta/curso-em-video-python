"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

totM20 = tot18 = totH = 0
while True:
    print('------ CADASTRE UMA PESSOA ------')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mMfF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    continuar = ' '
    while continuar not in 'sSnN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
            break

print(f'Total de pessoas com mais de 18 anos: {tot18}.\n'
      f'Ao todo temos {totH} homens cadastrados.\n'
      f'E temos {totM20} mulheres cadastradas em menos de 20 anos.')

# while True:
#     print('------ CADASTRE UMA PESSOA ------')
#     idade = int(input('Idade: '))
#     while True:
#         sexo = str(input('Sexo [M/F]: '))
#         if sexo in 'mf':
#             break
#     if idade > 18:
#         adultos += 1
#     if sexo == 'm':
#         homens += 1
#     if sexo == 'f' and idade < 20:
#         menos_vinte += 1
#     continuar = str(input('Quer continuar? [S/N]: '))
#     while continuar not in 'sn':
#         continuar = str(input('Quer continuar? [S/N]: '))
#     else:
#         if continuar == 'n':
#             break
#
# print(f'Total de pessoas com mais de 18 anos: {adultos}.\n'
#       f'Ao todo temos {homens} homens cadastrados.\n'
#       f'E temos {menos_vinte} mulheres cadastradas em menos de 20 anos.')