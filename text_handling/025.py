"""Programa que lê a frase pelo teclado e mostre
Quantas vezes aparece a letra A em que posição aparece pela
primeira vez em que posição aparece na última"""

text = str(input("Digite um texto: ")).lower()
print(f"A letra 'A' aparece {text.count('a')} vezes na frase")
print(f"Aparece pela primeira vez na posição {text.find('a')}")
print(f"Aparece pela última vez na posição {text.rfind('a')}")