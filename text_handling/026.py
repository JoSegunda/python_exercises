"""Program que lê um nome e mostra o primeiro e último nome"""

nome = str(input("Digite seu nome: "))
nome = nome.split()

print(f"Primeiro: {nome[0]}")
print(f"Último: {nome[-1]}")
