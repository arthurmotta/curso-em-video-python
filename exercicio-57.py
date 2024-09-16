"""Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
até ter um valor correto."""
correto = True
sexo = str(input('Qual é o seu sexo? [M/F] ').strip().upper()[0])

while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Qual é o seu sexo? [M/F] ').strip().upper()[0])

print('Sexo salvo com sucesso!')
