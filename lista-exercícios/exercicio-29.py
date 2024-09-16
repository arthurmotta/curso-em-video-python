km = int(input('Digite a velocidade do carro: '))
if km > 80:
    multa = (km - 80) * 7
    print('Seu carro foi multado em R${} reais'.format(multa))
else:
    print('Seu carro nao foi multado.')