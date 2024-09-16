"""A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria
conforme a idade.
Até 9 anos: MIRIM | Até 14 anos: INFANTIL | Até 19 anos: JÚNIOR
Até 20 anos: SÊNIOR | Acima: MASTER """
from datetime import datetime

ano = int(input('Digite o ano do seu nascimento: '))
idade = datetime.now().year - ano

if idade <= 9:
    print('Você tem {} anos e se enquadra na categoria MIRIM.'.format(idade))

elif idade <= 14:
    print('Você tem {} anos e se enquadra na categoria INFANTIL.'.format(idade))

elif idade <=19:
    print('Você tem {} anos e se enquadra na categoria JÚNIOR.'.format(idade))

elif idade <= 20:
    print('Você tem {} anos e se enquadra na categoria SÊNIOR.'.format(idade))

else:
    print('Você tem {} anos e se enquadra na categoria MASTER.'.format(idade))