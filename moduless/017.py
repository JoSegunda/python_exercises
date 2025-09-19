#Programa que lê um ângulo qualquer e mostre na o valor do seno
#coseno e tangente deste ângulo
from math import sin, cos, tan, radians
angulo = float(input("Digite o valor do ângulo: "))
angulo = radians(angulo)
print(f"O seno é {sin(angulo) :.2f}")
print(f"O cosseno é {cos(angulo) :.2f}")
print(f"A tangente {tan(angulo) :.2f}")