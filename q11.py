''' 
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre: 
- O produto do dobro do primeiro com metade do segundo .
- A soma do triplo do primeiro com o terceiro.
- O terceiro elevado ao cubo.
'''
numero1 = int(input('1º Número inteiro: '))
numero2 = int(input('2º Número inteiro: '))
numero3 = float(input('Número real: '))

print ('Soma:', ((2*numero1) * (numero2/2)))
print ('Produto:', (3 * numero1) + numero3)
print ('Cubo:', numero3**3)


