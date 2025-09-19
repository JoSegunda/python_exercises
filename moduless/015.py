# Crie um programa que leia um número real e mostre a sua porção inteira
from math import trunc

num = float(input("Digite um número: "))
print(f"Parte inteira de {num} é {trunc(num)}")