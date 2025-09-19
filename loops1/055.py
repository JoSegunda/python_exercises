"""Leia o peso de 5 pessoas e calcule o maior entre eles"""
from math import inf
menor = inf
maior = 0
print(menor)
for i in range(0, 5):
    peso = float(input("Digite o peso: "))
    if(peso > maior):
        maior = peso
    if(menor > peso):
        menor = peso
print(f"Maior Peso: {maior}")
print(f"Menor Peso: {menor}")