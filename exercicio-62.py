"""Melhore o exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos."""
termo = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão da PA: '))
contador = 10
termos = 10

while contador > 0:
    print('{} ➝ '.format(termo), end='')
    termo += razao
    contador -= 1
    if contador == 0:
        print('Pausa.', end='')
        contador = int(input('\nDeseja acrescentar mais números na sequência?\n'))
        termos += contador
print('Progressão finalizada com {} termos mostrados.'.format(termos))
