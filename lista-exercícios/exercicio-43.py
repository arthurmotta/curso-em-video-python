"""Desenvolva uma lógica que leia o peso e altura de uma pessoa
 calcule seu IMC e mostre seu status, conforme a tabela abaixo:
 Abaixo de 18,5: Abaixo do peso
 Entre 18.5 e 25: Peso ideal
 25 até 30: Sobrepeso
 30 até 40: Obesidade
 Acima de 40: Obesidade mórbida"""

peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é de {:.1f}kg/m2. Você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.1f}kg/m2. Você está no peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.1f}kg/m2. Você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.1f}kg/m2. Sua classificação é de obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.1f}kg/m2. Sua classificação é de obesidade mórbida.'.format(imc))