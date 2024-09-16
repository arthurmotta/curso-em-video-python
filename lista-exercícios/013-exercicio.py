s = float(input("Digite seu salário: "))
a = s + (s * 15 / 100)
print("O seu salário de R${:.2f} com aumento de 15% é de R${:.2f}".format(s, a))