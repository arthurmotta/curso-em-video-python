"""Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:
A vista dinheiro/cheque: 10% de desconto
A vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros"""

preco = float(input('Preço das compras: R$'))
condicao = int(input('Formas de pagamento: '
                     '\n(1) - A vista dinheiro/cheque'
                     '\n(2) - A vista cartão'
                     '\n(3) - 2x no cartão'
                     '\n(4) - 3x ou mais no cartão'
                     '\nOpção: '))

if condicao == 1:
    preco_din = preco - (preco * 10 / 100)
    print('Para o pagamento a vista dinheiro/cheque '
          'com 10% de desconto: R${:.2f}'.format(preco_din))
elif condicao == 2:
    preco_cartao = preco - (preco * 5 / 100)
    print('Para o pagamento a vista cartão '
          'com 5% de desconto: R${:.2f}'.format(preco_cartao))
elif condicao == 3:
    print('Parcela no cartão '
          'em 2x com juros: R${:.2f} mensais '
          '\nTotal com juros R${:.2f}'.format(preco / 2,preco))
elif condicao == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco_tres = preco + (preco * 20 / 100)
    print('Parcela no cartão '
          'em {}x com juros: R${:.2f} mensais'
          '\nTotal com juros R${}'.format(parcelas, preco_tres / parcelas, preco_tres))
else:
    print('Entrada errada. Tente novamente.')
