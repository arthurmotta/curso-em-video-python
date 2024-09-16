salario = float(input('Digite o seu salário: '))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
    print('Você terá um aumento de 10%: R${:.2f}'.format(salario))
else:
    salario = salario + (salario * 15 / 100)
    print('Você terá um aumento de 15%: R${:.2f}'.format(salario))