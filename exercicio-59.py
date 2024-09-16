"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep

menu = True
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

while menu:
    opcao = int(input('---- MENU ----\n'
                      '[1] - Somar\n'
                      '[2] - Multiplicar\n'
                      '[3] - Maior\n'
                      '[4] - Novos números\n'
                      '[5] - Sair do Programa\n'
                      'Digite a sua opção: '))

    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é: {}'.format(num1, num2, soma))
        sleep(1)
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicação entre {} x {} é: {}'.format(num1, num2, multiplicacao))
        sleep(1)
    elif opcao == 3:
        if num1 > num2:
            print('O valor {} é maior que o valor {}.'.format(num1, num2))
        else:
            print('O valor {} é maior que o valor {}.'.format(num2, num1))
        sleep(1)
    elif opcao == 4:
        num1 = int(input('Digite novamente o primeiro valor: '))
        num2 = int(input('Digite novamente o segundo valor: '))
        sleep(1)
    elif opcao == 5:
        print('Finalizando o programa...')
        sleep(1)
        print('Fim do programa.')
        menu = False
    else:
        print('Opção inválida. Tente novamente.')

