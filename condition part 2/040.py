"""Leia duas notas de um aluno e calcule a sua média"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

avg = (nota1+nota2) / 2

if(avg < 5): print("\033[0;31;40mReprovado")
elif(avg >= 5 and avg <= 6.9): print("\033[0;34;40mRecuperação")
else: print("\033[1;32;40mAprovado")