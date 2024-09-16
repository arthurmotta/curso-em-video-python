p = float(input("Digite o preço do produto R$"))
f = p - (p * 5 / 100)
print("O valor do produto com desconto de 5% é de R${:.2f}".format(f))