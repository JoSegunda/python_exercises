"""Programa que lê um número e calcula o seu fatorial"""

fact = 1
n = int(input("Digite um número: "))
print(f"{n}! = ", end=" ")
while n != 0:
    print(f"{n} x " if n > 1 else f'{n} = ',end="")
    fact *= n
    n-= 1
    
print(f"{fact}")