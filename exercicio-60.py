"""Faça um programa que leia um número qualquer e mostre sua fatorial"""
num = int(input('Digite um número para descobrir sua fatorial: '))
contador = num
fatorial = 1

print('{}! ='.format(num), end='')
while contador > 0:
    print(' {}'.format(contador), end='')
    print(' x' if contador > 1  else ' = ', end='')
    fatorial *= contador
    contador -=1
print('{}'.format(fatorial), end='')

# print('{}! ='.format(num), end='')
# for i in range(num, 0, -1):
#     print(' {}'.format(i), end='')
#     print(' = ' if i == 1 else ' x', end='')
#     fatorial = fatorial * i
#
# print('{}'.format(fatorial), end='')