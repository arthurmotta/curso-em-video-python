"""Faça um programa que leia um número inteiro e diga se ele é ou não primo."""
n = int(input('Digite um número: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, total))
if total == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')














# if n <= 1:
#     print('O número {} não é primo.'.format(n))
# else:
#     e_primo = True
#
#     for i in range(2, n):
#         if n % i == 0:
#             e_primo = False
#             break
#
#     if e_primo:
#         print('O número {} é primo.'.format(n))
#     else:
#         print('O número {} não é primo.'.format(n))