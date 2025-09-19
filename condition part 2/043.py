""" faça um programa que calcule o IMC e mostre as informações consoante o e altura """
# from math import pow
peso = float(input("Digite o seu peso(kg): "))
altura = float(input("Digite a sua altura(m): "))

imc = peso / (pow(altura,2))

if(imc <= 18.5): print("Abaixo do peso.")
elif(imc <= 25): print("Peso Ideal.")
elif(imc <= 30): print("Acima do peso.")
elif(imc <= 30): print("Sobrepeso.")
elif(imc <= 40): print("Obesidade.")
else: print("Obesidade mórbida.")
