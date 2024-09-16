km = float(input("Digite a quantidade de km rodados: "))
dias = float(input("Digite a quantidade de dias alugados: "))
aluguel = (km * 0.15) + (dias * 60)
print("O total a pagar é de R${:.2}".format(aluguel))