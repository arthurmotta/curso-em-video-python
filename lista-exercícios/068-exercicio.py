"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
import random
v = 0
while True:
    n = int(input("Digite um valor: "))
    computador = (random.randrange(0, 10))
    soma = computador + n
    escolha = ' '
    while escolha not in 'pPiI':
        escolha = input("Par ou Ímpar: [P/I] ").strip().upper()[0]
    print(f'Você jogou {n} e o computador {computador}. Total de {soma}. ', end='')
    print('Deu par' if soma % 2 == 0 else 'Deu ímpar')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu.')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você venceu.')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar de novo!')
print(f'Fim de jogo! Você venceu {v} vezes.')

    # if soma % 2 == 0:
    #     flag = 'p'
    # else:
    #     flag = 'i'
    # if flag == escolha:
    #     print(f'Você jogou {n} e o computador {computador}. Total de {soma} DEU PAR.' if flag == 'p'
    #           else f'Você jogou {n} e o computador {computador}. Total de {soma} DEU ÍMPAR.')
    #     print('Você venceu. Vamos jogar novamente...')
    # else:
    #     print(f'Você jogou {n} e o computador {computador}. Total de {soma} DEU PAR.' if flag == 'p'
    #           else f'Você jogou {n} e o computador {computador}. Total de {soma} DEU ÍMPAR.')
    #     print('Você perdeu.')
    #     break

