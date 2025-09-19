# faça um programa que leia o nome dos quatros alunos e mostra a ordem sorteada
from random import shuffle
a = str(input("Primeiro aluno: "))
b = str(input("Segundo aluno: "))
c = str(input("Terceiro aluno: "))
d = str(input("Quarto aluno: "))

order = [a,b,c,d]
shuffle(order)

print(f"Ordem das apresentações: {order}")