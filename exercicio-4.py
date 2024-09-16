n = input("Digite algo: ")
print(
    "Qual é o tipo primitivo: {}\n".format(type(n)),
    "Só tem espaços? {}\n".format(n.isspace()),
    "É um número? {}\n".format(n.isnumeric()),
    "Está com letras maiusculas? {}\n".format(n.isupper())
)