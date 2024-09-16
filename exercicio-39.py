""" Faça um programa que leia o ano de nascimento de um jovem
e informe, conforme a sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou
se já passou o tempo do alistamento. Seu programa deverá mostrar o tempo falta
e quanto tempo passado do prazo."""
from datetime import datetime

ano = int(input('Digite o ano do seu nascimento: '))
idade = datetime.now().year - ano

if idade < 18:
    print("Sua idade é de {} anos. \nVocê ainda terá que se alistar. \nFaltam {} anos.".format(idade ,18 - idade))
elif idade == 18:
    print("Sua idade é de {} anos. \nJá está na hora de se alistar.".format(idade))
else:
    print('Sua idade é de {} anos. \nSeu tempo de alistamento já passou há {} ano/anos.'.format(idade, idade - 18))
