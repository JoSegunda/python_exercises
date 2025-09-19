"""Faça um programa que leia um ano e mostre se ele é bissexto"""

ano = int(input("Digite um ano: "))

if (ano%4==0 & ano%100!=0 or ano%400==0):
    print("É Bissexto")
else:
    print("Não é bissexto")