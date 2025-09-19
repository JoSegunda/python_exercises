"""Programa wue deixa o utilizado adivinhar um número 
escolhido pelo computador até acertar"""
from random import randint

rad = randint(0,10)
n = 11
count = 0

while n != rad:
    n = int(input("Adivinhe o número: "))

    if(n != rad):
        print("ups, tente outra vez", end=" ")
        if(n < rad): print("desta vez tente Mais")
        elif(n > rad): print("desta vez tente Menos")
    count += 1
print(f"Número a adivinhar: {rad}")
print(f"Você acertou em {count} tentativas.")