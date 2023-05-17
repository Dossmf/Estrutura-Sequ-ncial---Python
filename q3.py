# Faça um Programa que peça dois números e imprima a soma.

numero1 = (input("Digite o primeiro número: "))
numero2 = (input("Digite o segundo número: "))

numero1int = float(numero1) # Usado o tipo Float da entrada caso o usuário 
numero2int = float(numero2) # digitar um número de ponto flutuante.

soma = numero1int + numero2int

print("A soma dos números é: ", soma)