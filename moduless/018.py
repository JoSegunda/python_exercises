# faça um program que sorteie o número de alunos
from random import choice
a = str(input("Primeiro aluno: "))
b = str(input("Segundo aluno: "))
c = str(input("Terceiro aluno: "))

aluno = choice((a,b,c))
print(f"O {aluno} será o responsável por limpar o quadro.")