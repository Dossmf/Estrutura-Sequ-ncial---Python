# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 # Vamos considerar a média 6.0

print("A média é: ", media)

if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")