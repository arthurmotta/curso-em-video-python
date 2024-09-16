import math
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
potencia_oposto = math.pow(cateto_oposto, 2)
potencia_adjacente = math.pow(cateto_adjacente, 2)
soma = potencia_oposto + potencia_adjacente
raiz = math.sqrt(soma)
print("O comprimento da hipotenusa desse triângulo retângulo é de {:.2f}".format(raiz))