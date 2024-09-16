import math
angulo = int(input("Digite o valor do ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno é de {}, cosseno {} e tangente de {}".format(seno, cosseno, tangente))