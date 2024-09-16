altura = float(input("Digite a altura da sua parede: "))
comprimento = float(input("Digite o comprimento da sua parede: "))
area = altura * comprimento
tinta = area / 2
print("Para uma area de {:.2f}m2, você precisará de {:.1f}ls de tinta".format(area, tinta))