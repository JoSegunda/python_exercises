"""Programa qu lẽ inteiro e mostra o maior, menor e a média"""
from math import inf
min = inf
max = 0
count = 0
sum = 0
condition = "s"
value = 0
while condition not in "nN":
    value = int(input("Digite um valor: "))
    condition = str(input("Deseja continuar [S / N]? "))
    sum += value
    count += 1
    if(value < min):
        min = value
    if(value > max):
        max = value
print(f"A média entre eles é {sum / count}")
print(f"maior valor: {max}, menor valor: {min}")