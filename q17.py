# Faça um Programa para uma loja de tintas. O programa deve pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
# litros, que custam R$ 25,00.
# • Informe ao usuário as utilidades de tinta a serem compradas e os respectivos preços em 3
#situações:
# • comprar apenas latas de 18 litros;
# • comprar apenas galões de 3,6 litros;
# • misture latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
# arredonde os valores para cima, isto é, considere latas cheias.

tamanho  =  float ( input ( 'Entre com o tamanho da área: ' ))

litros  =  tamanho  /  6
latas  =  litros  /  18

if  latas  %  18  !=  0 :
    latas  +=  1
preço  =  latas  *  80

galões  =  litros  /  3.6
if  galões  %  3.6  !=  0 :
    galões  +=  1
preco2  =  galões  *  25

# mistura de latas e galões
mistura_lata  =  int ( litros  /  18.0 )
mistura_galao  =  int (( litros  - ( mistura_lata  *  18 )) /  3.6 )

if  litros  - ( mistura_lata  *  18 ) %  3.6  !=  0 :
    mistura_galao  +=  1

print ( 'Apenas latas de 18 litros: %d'  %  latas , 'preço: %d'  %  preço )
print ( 'Apenas galões de 3.6 litros: %d'  %  galões , 'preço: %d'  %  preco2 )
print ( 'Mistura: %d latas e %d galões = %.2f'  % (
    mistura_lata , mistura_galao , (( mistura_lata  *  80 ) + ( mistura_galao  *  25 ))))