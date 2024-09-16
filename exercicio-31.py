km = int(input('Digite a quantidade de km da viagem: '))
if km <= 200:
    passagem = km * 0.50
    print('A passagem  para uma viagem de {}km sai por R${:.2f} reais'.format(km, passagem))
else:
    passagem = km * 0.45
    print('A passagem  para uma viagem de {}km sai por R${:.2f} reais'.format(km, passagem))