import random
num = int(input('Adivinhe o número secreto. Digite um número: '))
num_secreto = random.randrange(0, 6)
if num == num_secreto:
    print('Você acertou!')
else:
    print('Você errou! O número secreto é {}'.format(num_secreto))