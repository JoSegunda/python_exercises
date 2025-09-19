"""Crie um programa que leia o nome de uma pessoa e diga se ela tem o nome 
SIlva"""

nome = str(input("Digite um nome: ")).lower()
print(f"Tem Silva no nome? {nome.__contains__("silva")}")