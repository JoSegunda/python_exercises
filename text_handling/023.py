# Crie um programa que leia o nome de uma cidade e diga se ela 
# começa ou não com o nome santo

nome = str(input("Digite o nome de uma cidade: ")).lower()
print(f"{nome.startswith("santo")}")