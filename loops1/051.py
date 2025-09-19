"""Programa que lê o primeiro termo e a razão de uma progressão aritmética e mostre os 10 primeiros 
termos da progressão"""
termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
for i in range(1,11):
    print(f"{termo1}", end=" -> ")
    termo1 += razao
print("Fim")