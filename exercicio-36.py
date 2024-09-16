"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal nao pode exceder 30% do salário ou então o empréstimo será negado."""
valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Quantos anos será o financiamento: '))
prestacao = valor_casa / (anos * 12)
minimo = (salario * 30 / 100)
if prestacao <= minimo:
    print('Empréstimo negado. Prestação excede 30% do salário.')
else:
    print('Empréstimo concedido. A prestação mensal por {} anos será '
          'de R${:.2f} por mês.'.format(anos, prestacao))