#Crie um programa que mostra o nome completo de uma pessoa
#E mostre o nome com todas as letras maiúsculas, minúsculas, quantas letras
#sem espaços e quantas letras tem o primeiro nome

name = str(input("Digite o seu nome: ")).strip()

print(f"Nome em maiíusculas: {name.upper()}")
print(f"Nome em minúsculas: {name.lower()}")
print(f"Número de letras: {len(name.replace(" ",""))}")
nameList = name.split(" ")
print(f"O primeiro nome tem {len(nameList[0])}")