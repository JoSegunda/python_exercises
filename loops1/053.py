"""Crie um programa que leia uma frase qualquer e diga 
se é palindromo"""
text = str(input("Digite uma frase: ")).lower().strip()
newText = text.replace(" ", "")
reversedText = ""
for i in range(len(newText)-1,-1,-1):
    reversedText += newText[i]
if(reversedText == newText):print("É Palíndromo")
else:print("Não é Palíndromo")